#!/usr/bin/python
#Author: Raj Bindra
#Trueup script for out wonderful internal tool.
import sys
from lxml import etree
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint
devlist = open('device_list_test')
user = raw_input('username: ')
passwd = getpass('password: ')
for host in devlist:
    host = host.strip()
    print "Working on %s..." % host
    dev = Device(host,user=user,password=passwd, port=22)
    dev.open()
    file = open('out.txt', 'ab')
    output = dev.rpc.get_chassis_inventory(detail=True)
    file.write("\nrbindra@%s> show chassis hardware detail | display xml | no-more"% (host))
    file.write('\n')
    file.write(etree.tostring(output))
    file.write('\n              ')
    dev.close()
file.close()

