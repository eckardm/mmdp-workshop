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

# implements classes to read and write tabular (read table-like) data in csv format
# it already comes with python
import csv


'''
preliminaries'''

# this variable should point to the folder that contains the files we'll be manipulating
# note, we're using a relative path here, which means that python will expect this folder to be in the same folder as this script
# if it's not, you'll need to write out the absolute path
path = 'EADs'


'''
loop through the files and the subjects in the file'''

# loop through each filename in the eads folder
for filename in os.listdir(path):
    # create an etree or element tree object out of it so that lxml can work with it
    tree = etree.parse(join(path, filename))
    
    # perform a general xpath search for subject sub-elements of controlaccess elements
    # note, this returns a list of all subjects in the ead
    subjects = tree.xpath('//controlaccess/subject')
    
    # because it returns a list of all subjects in the ead, we'll need to loop through each subject in that list
    for subject in subjects:
    
    
            '''
            create a couple variables that we'll need, noting that we already have one for filename'''
            
            # particular xpath
            subject_xpath = tree.getpath(subject)
            # text
            subject_text = subject.text.encode('utf-8')
            
            
            '''
            write it to a csv'''
            
            # open up a csv file (the actual file is subjects.csv, but we'll be using a variable called csv_file in the code) in append mode (the a in ab)
            # note, the b in ab means binary, and for all practical purposes just means that our csv will be single-spaced instead of double-spaced
            with open('subjects.csv', 'ab') as csv_file:
                # create a writer (just something we have to do when using the csv module)
                writer = csv.writer(csv_file)
                # use the writer to write rows of the variables that we'll need
                # note, this function takes a list, and in python lists are enclosed in square brackets
                writer.writerow([filename, subject_xpath, subject_text])
            