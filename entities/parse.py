#!/usr/bin/python

from polyglot.text import Text

with open('input.txt', 'r') as fd:
  txt = Text(fd.read())
  count = {}
  for ent in txt.entities:
    k = str(ent)
    if k in count:
      count[k] += 1
    else:
      count[k] = 1
  for k in count.keys():
    print "%d => %s" % (count[k], k)



