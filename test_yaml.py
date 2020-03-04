#!/usr/bin/env python

import yaml
import json
import xml.etree.ElementTree as ET
import dicttoxml
import xml.dom.minidom
import xmltodict

with open('test-playbook.yml', 'r') as file:
    data = yaml.safe_load(file)
user = data[0]['vars']
print (user)
file.close()

with open('test-playbook-var.yml','w') as file:
    yaml.dump(user, file, default_flow_style=False)
file.close()

with open('test-playbook.json', 'w') as file:
    json.dump(data, file, indent=4)
file.close()

with open('test-playbook.json', 'r') as file:
    json_data = json.load(file)
file.close()

xml_object = dicttoxml.dicttoxml(data)

with open('test-playbook.xml', 'w') as file:
    file.write(xml_object.decode())
file.close()

with open('test-playbook.xml', 'r') as file:
    myroot=xml.dom.minidom.parse(file)
file.close()

prettyxml=myroot.toprettyxml()
print (prettyxml)
todict=xmltodict.parse(prettyxml)
print (json.dumps(todict,indent=4))

print (todict)





