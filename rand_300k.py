#!/usr/bin/python

from random import shuffle
from sys import stdout
from netaddr import *

ip=IPNetwork('64.0.0.0/3')
subnets=list(ip.subnet(22))
shuffle(subnets)
count = 0
while (count < 300000):
   stdout.write( 'announce route ' + str(subnets[count]) + ' next-hop self\n')
   stdout.flush()
   count = count + 1
