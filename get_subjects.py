import os
from os.path import join
from lxml import etree

path = 'EADs'

for filename in os.listdir(path):
    tree = etree.parse(join(path, filename))
    subjects = tree.xpath('//controlaccess/subject')
    for subject in subjects:
        print subject.text.encode('utf-8')
