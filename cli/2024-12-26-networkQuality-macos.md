# `networkQuality` tool in macos

In macos there is a  cli app `networkQuality` that can be used to test network quality. It outputs a summary including
download and upload speeds, latency, and responsiveness (measure in round trips per minute).

## Usage:

- `networkQuality` or `networkQuality -v` for a more verbose output

## Example output:

```
==== Verbose Results ====
---
Capacity:
---
   Uplink capacity: 31.259 Mbps
      Accuracy: High
      Uplink bytes transferred: 31.734 MB
      Uplink Flow count: 9
   Downlink capacity: 514.437 Mbps
      Accuracy: High
      Downlink bytes transferred: 500.612 MB
      Downlink Flow count: 9
---
Latency:
---
   Idle Latency:
      1057 RPM (56.750 milliseconds)
         Transport: 1185 RPM (50.625 milliseconds)
         Security: 860 RPM (69.750 milliseconds)
         HTTP: 1203 RPM (49.875 milliseconds)
      Accuracy: High
   Responsiveness: Medium
      680 RPM (88.154 milliseconds)
         Transport: 733 RPM (81.755 milliseconds)
         Security: 569 RPM (105.357 milliseconds)
         HTTP: 698 RPM (85.878 milliseconds)
         HTTP loaded: 316 RPM (189.871 milliseconds)
      Accuracy: High
---
Protocols Used:
---
    HTTP/2: 100%
---
Transport-layer info:
---
    ECN Disabled: 100%, L4S Disabled: 100%
---
Other Info:
---
   Test Endpoint: brsao4-edge-bx-012.aaplimg.com
   Interface: en0
   Start: 2024-12-26 11:32:26.700
   End: 2024-12-26 11:32:36.159
   OS Version: Version 15.1.1 (Build 24B2091)

==== SUMMARY ====
Uplink capacity: 31.259 Mbps
Downlink capacity: 514.437 Mbps
Responsiveness: Medium (88.154 milliseconds | 680 RPM)
Idle Latency: 56.750 milliseconds | 1057 RPM
```
