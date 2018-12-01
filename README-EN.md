# karma-captive-portal
karma attack And captive portal </br>

## Prerequisites
"Ubiquiti SR-71 , TP-link WN722N 或 Alfa AWUS036NH" Wireless card </br>

## Install
`apt-get install mana-toolkit lighttpd nginx` </br>
`git clone https://github.com/nios34/karma-captive-portal && cd karma-captive-portal/bin` </br>

## Usage
`./karma [Option] "Built-in interface" "Wireless card interface" ` </br>
Option: </br>
> -web Start captive portal </br>

## Note
 * Do not support running with relative or absolute paths! </br>
 * The arm device needs to compile hostapd and put it under the "hostapd directory" </br>
 * Must be root running Wireless card support hostapd-mana </br>
 * Must be run in the desktop environment If it is xfac4 or kde, please replace the gorme-terminal of the karma script with your terminal! </br>
 * Put your captive portal in /var/www/ </br>

## Acknowledgement
[mana-toolkit](https://github.com/sensepost/mana) </br>
[hostapd-mana](https://github.com/sensepost/hostapd-mana) </br>
[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) </br>
[@EastwindZL](https://github.com/EastwindZL) (tester) </br>

## 中文版
[点我跳转](https://github.com/nios34/karma-captive-portal/blob/master/README.md)
