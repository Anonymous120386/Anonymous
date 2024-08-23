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

### Related CVEs:
 

