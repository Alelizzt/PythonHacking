#!/usr/bin/python

import requests

myheaders = {'User-Agent' : 'Iphone 32'}
r = requests.get('http://arh.bg.ac.rs', headers = myheaders)

print(r.text)

