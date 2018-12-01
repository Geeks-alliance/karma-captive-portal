# -*- coding=UTF8 -*-
import time
import os
import random

def get():
    os.system("clear")
    a_l_l=0
    print("===============================BEGIN============================")
    with open('/var/log/dnsmasq.leases') as fd:
        for line in fd:
            a_l_l+=1
            try:
                print ('设备:%s MAC:%s IP:%s' % (((line.split())[-2]), (line.split())[-4], (line.split())[-3]))
            except:
                pass
            continue
        print("总数:%s" % a_l_l)
        print("================================END=============================")
        pass
    reget()
    pass

def reget():
    time.sleep(10)
    get()
    pass

if __name__ == "__main__":
    get()
    pass