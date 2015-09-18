# import what we need
import os
from os.path import join
from lxml import etree
import csv

# preliminaries
path = 'EADs'
clean_subjects_csv = 'subjects_clean.csv'

# open the csv file
with open(clean_subjects_csv, 'rb') as csv_file:
    
    # "read" the csv file
    reader = csv.reader(csv_file)
    # skip a line, since our csv file now has headers from openrefine
    next(reader, None)
    
    # go through each row in csv
    for row in reader:
    
        # we need to tell python what columns/index correspond to what data
        filename = row[0]
        subject_path = row[1]
        original_subject = row[2]
        clean_subject = row[3]
        
        # lets check to see if we need to actually do anything
        if original_subject != clean_subject:
        
            # let's make some stuff print to the terminal
            print 'Replacing ' + original_subject + ' with ' + clean_subject + ' at ' + subject_path + ' in ' + filename + '.'
        
            # this gets us to that particular ead
            ead_in = open(join(path, filename), 'r')
            
            # create the lxml tree
            tree = etree.parse(ead_in)
            
            # find the subject to replace (using the xpath)
            subject = tree.xpath(subject_path)
            
            # this is just a wierd lxml thing
            subject[0].text = clean_subject
            
            # now lets write the file again
            with open(join(path, filename), 'w') as ead_out:
                # this is just some extra encoding and declaration stuff
                ead_out.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))
                
print "That's it, we're done!"
