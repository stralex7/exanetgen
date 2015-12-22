#!/usr/bin/python

from random import shuffle
from sys import stdout
from time import sleep
from netaddr import *

ip=IPNetwork('64.0.0.0/3')
subnets=list(ip.subnet(22))
shuffle(subnets)
count = 0
c=0
while (count < 300000):
        while (c<1000):
                stdout.write( 'announce route ' + str(subnets[count]) + ' next-hop self\n')
                count = count + 1
                c=c+1
        stdout.flush()
        sleep(5)
        c=0
        count = count + 1

#Loop endlessly to allow ExaBGP to continue running
while True:
    sleep(1)
