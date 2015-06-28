#!/usr/bin/python
# -*- coding: utf-8 -*-

from glob import glob
from sys import argv

files = glob(argv[1] + '/*.t7')

def my_cmp(a, b):
  def loss_number(x):
    return x[-9:][:6]
  return cmp(loss_number(a), loss_number(b))
  
files = sorted(files, cmp=my_cmp)
files.reverse()

for fil in files:
  print fil

print "*** and the lowest checkpoint file is:\n%s" % (files[-1])

