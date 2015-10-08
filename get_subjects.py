# importing all the tools i'll need for this program
# os 
import os
from os.path import join
from lxml import etree
import csv

# path to eads

path = 'EADs'

# going through al lthe files in that directory

for filename in os.listdir(path):
	# parsing it
    tree = etree.parse(join(path, filename))
    # isolating subjects, this returns alist
    subjects = tree.xpath('//controlaccess/subject')
    # going through that list of subejcts
    for subject in subjects:

        subject_text = subject.text.encode('utf-8')
        subject_xpath = tree.getpath(subject)

        with open('subjects.csv', 'ab') as csv_file:
        	writer = csv.writer(csv_file)
        	writer.writerow([filename, subject_xpath, subject_text])
