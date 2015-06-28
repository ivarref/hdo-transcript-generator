#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
import sys

if len(sys.argv) < 4:
  print "Usage ./load.py <elasticsearch url> <name> <output-filename>"
  print """Example ./load.py http://localhost:9200 "Jens Stoltenberg" stoltenberg.txt"""
  sys.exit(1)

host = sys.argv[1]
name = sys.argv[2]
fil = sys.argv[3]

url = host + "/hdo-transcripts/_search"

values = {
  "size": 1000000,
  "query": { 
    "filtered" : { 
      "query" : { "match_all" : {}},
      "filter" : {
        "term" : { "name" : name }
      }
    }
  }
}

query = json.dumps(values)
response = urllib2.urlopen(url, query)

result = json.loads( response.read() )

written = 0
with open(fil, 'w') as w:
  def process(d):
    global written
    for k in d.keys():
      e = d[k]
      if type(e)==dict:
        if 'text' in e:
          txt = e['text'].encode('utf-8')
          w.write(txt)
          written += len(txt)
        process(e)
      elif type(e)==list:
        for x in e:
          process(x)
  process(result)

print "Wrote %d bytes, that's %0.2f MiB" % (written, (written / (1024.0*1024.)))

