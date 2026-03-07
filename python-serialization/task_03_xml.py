#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    return {child.tag: child.text for child in root}
