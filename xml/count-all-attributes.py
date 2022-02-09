from inspect import getfile
import sys
import xml.etree.ElementTree as etree

# recursively gets all attributes in the xml tree
def get_attr_number(node):
    # your code goes here
    count = len(node.attrib)
    for child in node:
        if len(list(child)) > 0:
            count += get_attr_number(child)
        else:
            count += len(child.attrib)
    
    return count

if __name__ == '__main__':
    xml = str()
    with open('/Users/benjaminzimmer/Documents/GitHub/hacker-rank-practice/xml/count-all-attributes.xml', 'r') as f:
        xml = f.read()
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        print(get_attr_number(root))
    