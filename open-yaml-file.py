#!/usr/bin/env python

import sys
from helper import *
from ruamel import yaml

import yaml
#import ruamel.yaml

import json

import xmltodict
#import untangle
import xml.dom.minidom as MD
import xml.etree.ElementTree as ET 

with open('user.yaml', 'r') as file:
    data = yaml.safe_load(file)
file.close()
data['first_name'] = "John"
print (data)

with open('user.yaml', 'w') as file:
    yaml.dump(data,file)
file.close()

with open('user.json','r') as file:
    data_string = json.load(file)
file.close()
data_json = json.loads(data_string)
data_json['first_name'] = "John"

print (data_json)

print("================================================")
for address in data_json['address']:
    address['city']="North Point"

with open('user.json','w') as file:
    json.dump(data_json, file, indent=4)
file.close()



with open ('xml-sample.xml','r') as file:
    data_xmltodict = xmltodict.parse(file.read())
#    data_et = ET.parse(file)
file.close()

print(data_xmltodict)


data_et = ET.parse('user.xml')
root = data_et.getroot()

print ('Tags in the XML:')
for element in root:
    print (element.tag)

print ('print first_name: ')
print (root.find('first_name').text)
addresses = root.findall('address')
for address in addresses:
    for i in address:
        print (i.tag + ":" + i.text)
print ("Print score: ")
print (root.find('score').text)

print ("Print structure: ")
for element in root.iter():
    print (element.tag + ":" + element.text)


dom = MD.parse('user.xml')
print ('Tags in the XML: ')
for node in dom.childNodes:
    printTags(node.childNodes)

