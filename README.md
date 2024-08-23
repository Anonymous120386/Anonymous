# Anonymous
This repository contains all the research output about vulnerabilities in IP Camera (D3D, Ezviz IP Camera).

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
 

