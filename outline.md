Introduction
============

(5 minutes)

  1. Ourselves
  2. Structured data
  3. Why this is important
  4. Disclaimer
  5. How to approach these kinds of problems
    * Think like a computer
    * You will make mistakes
    * Backups! Did I mention backups?
  
Scope of Workshop 
=================

(10 minutes)

  1. Recap learning outcomes
  2. Introduce EAD (complicated, we're actually going to be accessing the easy part)
  3. Introduce Python
  4. Introduce libraries, like LXML and CSV (also difference between standard library and stuff you have to install separately)
  5. Introduce OpenRefine
  
[Pass out chocolate, do some stretching]

Workshop
========

Use Python and LXML to Create CSV
---------------------------------

  1. Open terminal/command prompt
  2. Navigate to Python folder
  3. Start Python
  
<code>print "Hello World"</code>
  
  5. Explain importing (metaphor of toolbelt, somebody has already done this for you...)
  6. Explain os
  7. import os
  8. from os.path import join (this will make our lives easier, just trust us for now)
  9. Explain lxml
  10. from lxml import etree (only what we need)
  11. Exlain csv
  12. import csv
  
  13. Explain variables
  14. path = 'EADs' (easy in this instance, but could be harder)
  
  15. Explain problem of going through directories/nodes in XML
  16. Explain solution (looping)
  17. for filename in 'EADs':

  18. Tell Python that this file is an xml file
  19. tree = etree.parse(join(path, filename))
  20. Explain the join part (telling Python how to do what is easy for a human), also how you don't have to typoe out the whole thing
  
  21. subjects = tree.xpath('//controlaccess/subject')
  22. Explain XPath (high-level, we'll get more in depth later), telling Python where to look matching anything, now it knows where all these are (in a list)
  23. Explain EAD structure

  24. Explain that we need another loop to go through each subject it's found
  24. for subject in subjects:
  
  25. print subject.text
  
  26. Take a breath, marvel at our genius
  
  27. Get into writing a program... and making comments!

(20 mintues)

Use OpenRefine to Clean CSV
---------------------------

(20 minutes)

Use Python and LXML to Update Original XML
------------------------------------------

(10 minutes)

Recap
=====

  1. One of many ways to do it
  2. One of many things to do
  3. Takeaways
     * Google
  4. You can do it!
  5. Evaluation (either us or MMDP)
  
Notes
=====

Ask people to come early if they have issues with downloading/installing Python, LXML, Open Refine

TO DO
=====
Instructions for Python, LXML, OpenRefine, something besides Notepad, recommendations.
Create some files to send around.