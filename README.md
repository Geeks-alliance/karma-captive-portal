# karma-captive-portal
karma attack And captive portal </br>

## 先决条件
一张 "Ubiquiti SR-71 , TP-link WN722N 或 Alfa AWUS036NH" 等网卡 </br>

## 安装方法
`apt-get install mana-toolkit lighttpd nginx` </br>
`git clone https://github.com/nios34/karma-captive-portal && cd karma-captive-portal/bin` </br>

## 运行方法
`./karma [选项] 内置接口 外接网卡 ` </br>
选项: </br>
> -web 启动captive portal (否则客户端可以联网) </br>

## 注意 
 * 不支持使用相对路径或绝对路径运行! </br>
 * arm设备需要自行编译出hostapd放到"hostapd目录"下 </br>
 * 必须Root运行 网卡支持hostapd-mana </br>
 * 必须在桌面环境下运行 如果是xfac4 kde请把karma脚本的gnome-terminal换成你的终端!
 * 把你的captive portal 放在 /var/www/

## 鸣谢
[mana-toolkit](https://github.com/sensepost/mana) </br>
[hostapd-mana](https://github.com/sensepost/hostapd-mana) </br>
[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) </br>
[@EastwindZL](https://github.com/EastwindZL) (测试者) </br>

## ENGLISH VERSION
[Click me!](https://github.com/nios34/karma-captive-portal/blob/master/README-EN.md)
