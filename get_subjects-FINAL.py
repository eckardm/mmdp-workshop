'''
first, import the tools that we'll need'''

# this module provides a portable way of using operating system dependent functionality
# it already comes with python
import os
from os.path import join

# lxml is the most feature-rich and easy-to-use library for processing xml and html in the python language
# you'll have to download it separately
# this blog post might help out: http://archival-integration.blogspot.com/2015/10/tools-for-programming-archivist-ead.html
from lxml import etree


'''
preliminaries'''

# this variable should point to the folder that contains the files we'll be manipulating
# note, we're using a relative path here, which means that python will expect this folder to be in the same folder as this script
# if it's not, you'll need to write out the absolute path
path = 'EADs'

# loop through each filename in the eads folder
for filename in os.listdir(path):
    # create an etree or element tree object out of it so that lxml can work with it
    tree = etree.parse(join(path, filename))
    # perform an xpath search for subject sub-elements of controlaccess elements
    # note, this returns a list of all subjects in the ead
    subjects = tree.xpath('//controlaccess/subject')
    
    # because it returns a list of all subjects in the ead, we'll need to loop through each subject in that list
    for subject in subjects:
        
