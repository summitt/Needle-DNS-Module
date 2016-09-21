# Needle-DNS-Module

This module can be added to [Needle](https://github.com/mwrlabs/needle) to automatically set the DNS of the iOS device. 

You can use this with the [NoPE proxy](https://github.com/summitt/Burp-Non-HTTP-Extension) to automatically send all traffic to BurpSuite.


```
[needle] use comms/dns/dns
[needle][dns] set dns 192.168.1.128
[needle][dns] > run
[*] Checking connection with device...
[+] Already connected to: 127.0.0.1
[V] Creating temp folder: /var/root/needle/
[*] Configuring device...
[?] Trying to continue anyway...
[+] Target app: XXXXXXXXXXXXXXXX
[*] Retrieving app's metadata...
[V] Refreshing list of installed apps...
[*] Converting plist to xml
[*] Backing up preferences
[*] Updating Preferences
[*] Pushing Preferences back to device
[*] Complete
```
