import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
        
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    xml = str()
    with open('/Users/benjaminzimmer/Documents/GitHub/hacker-rank-practice/xml/count-all-attributes.xml', 'r') as f:
        xml = f.read()
        tree = etree.ElementTree(etree.fromstring(xml))
        root = tree.getroot()
        depth(tree.getroot(), -1)
        print(maxdepth)