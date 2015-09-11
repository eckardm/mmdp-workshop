import os
from os.path import join
from lxml import etree
import csv

path = 'EADs'

for filename in path:
    tree = etree.parse(join(path, filename))
    subjects = tree.xpath('//controlaccess/subject')
    for subject in subjects:
        print subject.text