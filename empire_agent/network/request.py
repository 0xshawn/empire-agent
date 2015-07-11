# -*- coding: utf-8 -*-


import urllib2
import json
import socket
import traceback
import requests


class Request(object):

    def __init__(self):
        pass


def http_get(url):
    try:
        req = urllib2.urlopen(url)
        response = json.load(req)
        return response
    except Exception as inst:
        print '----FAIL----'
        print type(inst)
        print inst.args
        print inst
        traceback.print_exc()
    return None


def http_long_poling(self, url):
    pass


def http_patch(url, data, headers):
    try:
        response = requests.patch(
            url, data=json.dumps(data), headers=headers)
        return response
    except Exception as inst:
        print '----FAIL----'
        print type(inst)
        print inst.args
        print inst
        traceback.print_exc()
    return None
