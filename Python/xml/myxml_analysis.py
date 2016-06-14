# -*- coding:utf8

from xml.dom.minidom import parseString

xml_file = open("1.xml", mode="r")
xml = xml_file.read()

dom = parseString(xml)

nodes = dom.childNodes

for node in nodes:
    print node.nodeName
print dom
