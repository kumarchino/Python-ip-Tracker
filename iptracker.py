import os
import urllib2
import json

while True:
    ip=raw_input("What is your target IP: ")
    url = "https://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print(" IP: " + values['query'])
    print(" City: " + values['city']) 
    print(" ISP: " + values['isp'])
    print(" Country: " + values['country'])
    print(" Region: " + values['region'])
    print(" Time zone: " + values['timezone'])

    break
