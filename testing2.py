#!/usr/bin/env python

## """<?xml version="1.0" encoding="UTF-8"?><server><description>My virtual server test</description><destination>1.1.1.3:80</destination><ipProtocol>tcp</ipProtocol><kind>tm:ltm:virtual:virtualstate</kind><mask>255.255.255.255</mask><name>http-virtual</name><pool>http</pool><profiles><element><kind>ltm:virtual:profile</kind><name>http</name></element><element><kind>ltm:virtual:profile</kind><name>tcp</name></element></profiles><sourceAddressTranslation><type>automap</type></sourceAddressTranslation></server>"""

import xml.dom.minidom

xmlString = """<?xml version="1.0" encoding="UTF-8"?><server><description>My virtual server test</description><destination>1.1.1.3:80</destination><ipProtocol>tcp</ipProtocol><kind>tm:ltm:virtual:virtualstate</kind><mask>255.255.255.255</mask><name>http-virtual</name><pool>http</pool><profiles><element><kind>ltm:virtual:profile</kind><name>http</name></element><element><kind>ltm:virtual:profile</kind><name>tcp</name></element></profiles><sourceAddressTranslation><type>automap</type></sourceAddressTranslation></server>"""
a = "1"

dom = xml.dom.minidom.parseString(xmlString)
prettyxml = dom.toprettyxml()
print (prettyxml)


