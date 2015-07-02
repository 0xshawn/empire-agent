#!/usr/bin/env python

from subprocess
import requests
import urllib2
import json
import os

req = urllib2.Request('http://localhost:9000/api/tasks')
response = json.load(urllib2.urlopen(req))
print response
print 'finish request'
