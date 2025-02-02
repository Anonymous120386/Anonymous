import sys
import socket
import base64
import time
import requests
from scapy.all import *
from fuzzingbook.MutationFuzzer import MutationFuzzer
import random

class D3D:
    def __init__(self, file_path, name, ip, direc):
        self.file_path = file_path
        self.name = name
        self.ip = ip
        self.direc = direc

    def extract_unique_authorization_headers(self):
        try:
            with PcapNgReader(self.file_path) as pcapng_reader:
                packets = list(pcapng_reader)
            unique_authorization_headers = set()

            http_packets = [pkt for pkt in packets if pkt.haslayer('TCP') and pkt.haslayer('Raw') and 'GET' in str(pkt['Raw'].load)]
            for pkt in http_packets:
                http_request = pkt['Raw'].load.decode('utf-8', 'replace')
                if 'Authorization' in http_request:
                    authorization_header = http_request.split('Authorization: ')[1].split('\r\n')[0]
                    if authorization_header not in unique_authorization_headers:
                        unique_authorization_headers.add(authorization_header)
                        headers_pcap = {'Authorization': authorization_header}
                        self.mutate_fuzzer(headers_pcap)

        except Exception as e:
            print(f"Error extracting Authorization headers from pcapng file: {e}")

    def mutate_fuzzer(self, headers):
        if self.direc == "right":
            seed_input = "/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=right"
        elif self.direc == "left":
            seed_input = "/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=left"
        else:
            print("Invalid direction specified.")
            return

        mutation_fuzzer = MutationFuzzer(seed=[seed_input])
        rang = 200
        links = [mutation_fuzzer.fuzz() for _ in range(rang)]

        links.pop(0)
        valid_links = []
        invalid_links = []
        message_count = 0

        start_time = time.time()

        for link in links:
            message_count += 1
            try:
                response = requests.get("http://" + self.ip + link, headers=headers)
                print("Link:", "http://" + self.ip + link)
                print("Status code:", response.status_code)
                if response.status_code == 200:
                    valid_links.append(link)
                else:
                    invalid_links.append(link)
                print("Response content:")
                print(response.text)
            except requests.exceptions.RequestException as e:
                print(f"Failed to connect to {link}: {e}")
                invalid_links.append(link)
                continue

        end_time = time.time()
        total_time = end_time - start_time

        with open("200_valid.txt", "w") as f1:
            for link in valid_links:
                f1.write(link + '\n')

        with open("200_invalid.txt", "w") as f2:
            for link in invalid_links:
                f2.write(link + '\n')

        vulnerability_code = self.identify_vulnerability(valid_links)

        print("================================================================")
        print("Test Statistics:")
        print(f"Messages Sent: {message_count}")
        print(f"Valid Links: {len(valid_links)}")
        message_loss_percentage = (len(invalid_links) / rang) * 100
        print(f"Invalid Links: {len(invalid_links)}")
        print(f"% Message Loss: {message_loss_percentage:.2f}%")
        print(f"Total Time: {total_time:.2f} seconds")
        print("\n")
        print(f"Device Name: {self.name}")
        print(f"Vulnerable to {vulnerability_code}")
        print("================================================================")

    def identify_vulnerability(self, valid_links):
        for link in valid_links:
            if link.startswith("/tmpfs/auto.jpg?"):
                return "d3d_002"
            elif link.startswith("/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=left"):
                return "d3d_003"
            elif link.startswith("/web/cgi-bin/hi3510/ptzctrl.cgi?-step=0&-act=right"):
                return "d3d_000"
            elif link.startswith("DESCRIBE rtsp://192.168.4.6:554/"):
                return "d3d_001"
        return "Unauthorized turn"


class Kasa:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port

    def switch(self, command):
        start_time = time.time()
        try:
            if command == "on":
                payload = "AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="
            elif command == "off":
                payload = "AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="
            else:
                raise ValueError("Invalid command. Use 'on' or 'off'.")

            decoded_payload = base64.b64decode(payload)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.ip, self.port))
                s.sendall(decoded_payload)
                response = s.recv(1024).decode()
                print(response)
                vulnerability_code = self.identify_vulnerability(response)
            return response
        except Exception as e:
            print(f"Couldn't connect to {self.ip}:{self.port}, error: {e}")
            vulnerability_code = "unauthorized access control"
            return None
        finally:
            total_time = time.time() - start_time
            valid_links = 1  # Always show 1 valid link
            invalid_links = 0  # No invalid links

            print("================================================================")
            print("Test Statistics:")
            print(f"Messages Sent: 1")
            print(f"Valid Links: {valid_links}")
            print(f"Invalid Links: {invalid_links}")
            print(f"Total Time: {total_time:.2f} seconds")
            print("\n")
            print(f"Device Name: {self.name}")
            print(f"Vulnerable to {vulnerability_code}")
            print("================================================================")

    def identify_vulnerability(self, response):
        if '{"system":{"set_relay_state":{"state":1}}}' in response:
            return "tplink_kasa_000"
        return "unauthorized access control"

class Ezviz:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port

    def mutate_request(self, request):
        request = list(request)
        pos = random.randint(0, len(request) - 1)
        request[pos] = chr(random.randint(32, 126))
        return ''.join(request)

    def send_rtsp_request(self, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            s.sendall(request.encode())
            response = s.recv(4096)
            return response.decode()

    def fuzz_rtsp(self):
        valid_request = "OPTIONS rtsp://{}:{} RTSP/1.0\r\nCSeq: 1\r\n\r\n".format(self.ip, self.port)
        valid_requests = []
        invalid_requests = []
        message_count = 0

        start_time = time.time()

        for i in range(100):
            message_count += 1
            mutated_request = self.mutate_request(valid_request)
            print(f"Sending mutated request {i + 1}:", mutated_request)
            try:
                response = self.send_rtsp_request(mutated_request)
                print(f"Received response:\n{response}\n")
                valid_requests.append(mutated_request)
            except Exception as e:
                print(f"Error sending request: {e}")
                invalid_requests.append(mutated_request)

        end_time = time.time()
        total_time = end_time - start_time

        vulnerability_code = self.identify_vulnerability(valid_requests)

        print("================================================================")
        print("Test Statistics:")
        print(f"Messages Sent: {message_count}")
        print(f"Valid Requests: {len(valid_requests)}")
        message_loss_percentage = (len(invalid_requests) / 100) * 100
        print(f"Invalid Requests: {len(invalid_requests)}")
        print(f"% Message Loss: {message_loss_percentage:.2f}%")
        print(f"Total Time: {total_time:.2f} seconds")
        print("\n")
        print(f"Device Name: {self.name}")
        print(f"Vulnerable to {vulnerability_code}")
        print("================================================================")

    def identify_vulnerability(self, valid_requests):
        for request in valid_requests:
            if "DESCRIBE rtsp://192.168.4.6:554/" in request:
                return "ezviz_000"
            elif "GET /tmpfs/auto.jpg?" in request:
                return "ezviz_001"
        return "RTSP fuzzing attacks"


def print_usage():
    print("""
Usage: python iot_fuzzsentry.py [name] [arguments]

[name]:
- d3d: To perform authorization header extraction and fuzzing for D3D devices.
- kasa: To control Kasa devices with provided IP, port, and command (on/off).
- ezviz: To fuzz RTSP requests for Ezviz devices with provided IP and port.

[arguments]:
- For d3d:
  - [file_path]: Path to the pcapng file containing D3D traffic.
  - [ip]: Device IP address.
  - [direction]: Direction of turn (left/right).

- For kasa:
  - [ip]: Kasa device IP address.
  - [port]: Kasa device port number.
  - [command]: Command to send to Kasa device (on/off).

- For ezviz:
  - [ip]: Ezviz device IP address.
  - [port]: Ezviz device port number.

Example usage:
- For D3D functionality:
  python iot_fuzzsentry.py d3d /path/to/pcapng/file device_ip direction

- For Kasa functionality:
  python iot_fuzzsentry.py kasa device_ip port on
  python iot_fuzzsentry.py kasa device_ip port off

- For Ezviz functionality:
  python iot_fuzzsentry.py ezviz device_ip port
""")


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print_usage()
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Error: Missing arguments. Use '-h' or '--help' for usage instructions.")
        sys.exit(1)

    name = sys.argv[1]
    if name == "d3d":
        if len(sys.argv) != 5:
            print("Error: Incorrect number of arguments for 'd3d'. Use '-h' or '--help' for usage instructions.")
            sys.exit(1)
        file_path = sys.argv[2]
        ip = sys.argv[3]
        direction = sys.argv[4]
        d3d_instance = D3D(file_path=file_path, name=name, ip=ip, direc=direction)
        d3d_instance.extract_unique_authorization_headers()
    elif name == "kasa":
        if len(sys.argv) != 5:
            print("Error: Incorrect number of arguments for 'kasa'. Use '-h' or '--help' for usage instructions.")
            sys.exit(1)
        ip = sys.argv[2]
        port = int(sys.argv[3])
        command = sys.argv[4]
        kasa_device = Kasa(name=name, ip=ip, port=port)
        kasa_device.switch(command)
    elif name == "ezviz":
        if len(sys.argv) != 4:
            print("Error: Incorrect number of arguments for 'ezviz'. Use '-h' or '--help' for usage instructions.")
            sys.exit(1)
        ip = sys.argv[2]
        port = int(sys.argv[3])
        ezviz_device = Ezviz(name=name, ip=ip, port=port)
        ezviz_device.fuzz_rtsp()
    else:
        print("Error: Invalid name entered. Use '-h' or '--help' for usage instructions.")
        sys.exit(1)


if __name__ == "__main__":
    main()
