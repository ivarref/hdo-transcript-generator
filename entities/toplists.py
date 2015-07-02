#!/usr/bin/python

from glob import glob

for fil in glob("*.txt"):
  if fil == 'input.txt':
    continue
  with open(fil, 'r') as fd:
    lines = [x.strip() for x in fd.readlines()]
    lines = lines[-30:] # top 30
    for lin in lines:
      print "%s %s" % (fil.ljust(10), lin)

