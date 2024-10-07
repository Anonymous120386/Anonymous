# Anonymous
This repository contains all the research output about vulnerabilities in Smart Plug (IoT Haat), IP Camera (D3D, Ezviz IP Camera).

# IoT Haat Smart Plug IH-IN-16A-S

## Affected Product

 IH-IN-16A-S - Application Software Version: 5.16.1

## Affected Vendor

 IoT Haat Smart Plug IH-IN-16A-S. 

## CVE Number

[CVE-2024-46040] (https://cve.mitre.org/cgi-bin/cvename.cgi?name=2024-46040)

## Summary

IoT Haat Smart Plug IH-IN-16A-S IH-IN-16A-S v5.16.1 suffers from Insufficient Session Expiration. The lack of validation of the authentication token at the IoT Haat during the Access Point Pairing mode leads the attacker to replay the Wi-Fi packets and forcefully turn off the access point after the authentication token has expired

## Tested Versions

IH-IN-16A-S - Application Software Version: 5.16.1

## Product URLs

[Website] (https://www.iothaat.com/)

## CVSSv3 Score

TBA

## CWE

TBA

## Details

To exploit the vulnerability, an attacker replays the Wi-Fi packets captured during the provisioning phase of the IoT Haat in the Access Point pairing mode.

# IoT Haat Smart Plug IH-IN-16A-S

## Affected Product

 IH-IN-16A-S - Application Software Version: 5.16.1

## Affected Vendor

 IoT Haat Smart Plug IH-IN-16A-S. 

## CVE Number

[CVE-2024-46041] (https://cve.mitre.org/cgi-bin/cvename.cgi?name=2024-46041)

## Summary

IoT Haat Smart Plug IH-IN-16A-S v5.16.1 is vulnerable to Authentication Bypass by Capture-replay.

## Tested Versions

IH-IN-16A-S - Application Software Version: 5.16.1

## Product URLs

[Website] (https://www.iothaat.com/)

## CVSSv3 Score

TBA

## CWE

TBA

## Details

To exploit this vulnerability, an attacker in the provisioning phase of IoT Haat, performs an authentication-token-based replay attack by replacing a legitimate authentication token with the attacker's token.


# Ezviz IP Camera : Sneak IP camera Live Video Stream

## Affected Product

Ezviz Internet PT Camera

## Affected Vendor

Hangzhou Hikvision Digital Technology Co. Limited. 

## CVE Number

[CVE-2024-42531] (https://www.cve.org/CVERecord?id=CVE-2024-42531)

## Summary

Ezviz Internet PT Camera (CS-CV246) (D15655150) allows an unauthenticated host to access its live video stream by crafting a set of RTSP packets with a specific set of URI that can be used to redirect the camera feed.

## Tested Versions

Ezviz Internet PT Camera (Model : CS-CV246) (B0-1C1WFR)
Serial Number: D15655150 Version : V5.3.0 build 191225

## Product URLs

[Website](http://ezviz.com)

## CVSSv3 Score

TBA

## CWE

TBA

## Details

The camera allows an unauthenticated host to access its live videos by crafting set of valid RTSP Uniform Resource Identifier (URI) from payload to perform attack.


 

# D3D IP Camera IoT Command Injection

## Affected Product

D3D Security IP Camera

## Affected Vendor

D3D Security Private Limited.

## CVE Number

[CVE-2024-41623] (https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41623)

## Summary

An issue in D3D Security D3D IP Camera (Model D8801) v.V9.1.17.1.4-20180428 allows a local attacker to execute arbitrary code via a crafted payload

## Tested Versions

D3D Security IP Camera (D8801) v.V9.1.17.1.4-20180428

## Product URLs

[Website](https://www.amazon.in/D3D-Wireless-Indoor-Security-Support/dp/B01N2VLFQ5/ref=cm_cr_arp_d_product_top?ie=UTF8)
[Shodan Search Engine] (https://www.shodan.io/search?query=d3d+camera)

## CVSSv3 Score

TBA

## CWE

TBA

## Details

The camera allows an unauthenticated host to access its live images by crafting set of HTTP packets with Method as GET and Request-URI tag containing a mutated value using Fuzzing.

### Related CVEs:
 

