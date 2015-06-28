#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from glob import glob
from pprint import pprint
import codecs
import sys

match_name = " ".join([unicode(x, 'utf-8') for x in sys.argv[1:]])
prefix = "data"
files = glob(prefix + "/*.json")
print "Number files to parse: %d " % (len(files))

def process(d, w):
  global match_name
  is_text_block = type(d)==dict and ('text' in d) and ('name' in d)
  if is_text_block and (d['name'] == match_name):
    txt = d['text'].encode('utf-8')
    w.write(txt)
    return len(txt)
  elif type(d) == dict:
    return sum([process(d[x], w) for x in d.keys()])
  elif type(d) == list:
    return sum([process(x, w) for x in d])
  elif d is None or type(d) == unicode:
    return 0
  else:
    print "unknown type: %s" % (str(type(d)))
    import sys
    sys.exit(1)

with open('input.txt', 'w') as w:
  written = 0
  for (idx,fil) in enumerate(files):
    idx+=1
    with codecs.open(fil, 'r', 'utf-8') as fd:
      result = json.load(fd)
      written += process(result, w)
      percentage = idx*100.0 / len(files)
      print "Processed %d of %d files, %0.2f%% done." % (idx, len(files), percentage)

print "Wrote %d bytes, that's %0.2f MiB" % (written, (written / (1024.0*1024.)))

