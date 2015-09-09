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

### From the terminal

(20 minutes)

  * Open terminal/command prompt
  * Navigate to Python folder
  * Start Python
  
<pre><code>>>> print "Hello World"</code></pre>
  
  * Explain importing (metaphor of toolbelt, somebody has already done this for you...)
  * Explain os (second part will make our lives easier, just trust us for now)

<pre><code>>>> import os</code></pre>
<pre><code>>>> from os.path import join</code></pre>

  * Explain lxml (only what we need)

<pre><code>>>> from lxml import etree</code></pre>

  * Exlain csv

<pre><code>>>> import csv</code></pre>
  
  * Explain variables

<pre><code>>>> path = 'EADs'</code></pre>

  * Explain that directory is easy in this instance, but could be harder.
  * Explain problem of going through directories/nodes in XML
  * Explain solution (looping)
  
<pre><code>>>> for filename in path:</code></pre>

  * Tell Python that this file is an xml file
  
<pre><code>>>>     tree = etree.parse(join(path, filename))</code></pre>
 
  * Explain the join part (telling Python how to do what is easy for a human), also how you don't have to typoe out the whole thing
  
<pre><code>>>>     subjects = tree.xpath('//controlaccess/subject')</code></pre>
 
  * Explain XPath (high-level, we'll get more in depth later), telling Python where to look matching anything, now it knows where all these are (in a list)
  * Explain EAD structure (why we're using controlaccess)
  * Explain that we need another loop to go through each subject it's found

<pre><code>>>>     for subject in subjects:</code></pre>
<pre><code>>>>         print subject.text</code></pre>
  
  * Take a breath, marvel at our genius
  
### Writing a program
  
  * Get into writing a program... and making comments!

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