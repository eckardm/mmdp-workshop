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

  * Explain this particular thing is for cleaning up subjects. Some backstory.

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

<pre><code>>>> for filename in os.listdir(path):</code></pre>

  * Tell Python that this file is an xml file

<pre><code>>>>     tree = etree.parse(join(path, filename))</code></pre>

  * Explain the join part (telling Python how to do what is easy for a human), also how you don't have to typoe out the whole thing

<pre><code>>>>     subjects = tree.xpath('//controlaccess/subject')</code></pre>

  * Explain XPath (high-level, we'll get more in depth later), telling Python where to look matching anything, now it knows where all these are (in a list)
  * Explain EAD structure (why we're using controlaccess)
  * Explain that we need another loop to go through each subject it's found

<pre><code>>>>     for subject in subjects:</code></pre>
<pre><code>>>>         print subject.text.encode('utf-8')</code></pre>

  * Take a breath, marvel at our genius

### Writing a program

  * Explain about writing a program
  * Explain about why text editors are better than Notepad (or equivalent)
  * Open a text editors
  * Open get_subjects.py (we'll have this ready to go)
  * Note that you end it with "py"
  * Run the script by first quiting python, then changing directories (if necessary), typing the filename ("python" in front depending on OS) and pressing Enter

<pre><code>>>> quit()</code></pre>
<pre><code>python get_subjects.py</code></pre>

  * Explain about making comments (why and how)
  * Make some comments
  * Now, think about our overall goals--what else will we need to complete this whole process?
  * Turns out we'll also need filename and location (XPath)
  * Explain XPath--will be easier to understand once you see it--maybe show it in Oxygen
  * Add the following lines to get_subjects.py

<pre><code>        print filename</code></pre>
<pre><code>        print tree.getpath(subject)</code></pre>

  * Explain that this is just the way you say this in LXML
  * Run the code
  * Might be useful to make a variable out of the XPath (and, while we're at it, subject text)...
  * Edit get_subjects.py. Change...

<pre><code>        print tree.getpath(subject)</code></pre>
<pre><code>        print subject.text.encode('utf-8')</code></pre>

to...

<pre><code>        subject_path = tree.getpath(subject)</code></pre>
<pre><code>        subject_text = subject.text.encode('utf-8')</code></pre>

and add...

<pre><code>        print subject_xpath</code></pre>
<pre><code>        print subject_text</code></pre>

  * Talk about the error that just occured. Explain that Python is not mad, just confused.
  * Correct the mistake to...

<pre><code>        print subject_xpath</code></pre>

  * Make note about how variables can be called whatever you want, but they should be "semantic"--also explain semantic.
  * Now we have everything we need, except for the CSV. For the sake of time we're just going to write this out with high-level explanation...

<pre><code>        with open('subjects.csv', 'ab') as csv_file:</pre></code>
<pre><code>            writer = csv.writer(csv_file)</pre></code>
<pre><code>            writer.writerow([filename, subject_path, subject_text])</pre></code>

  * Run it
  * Look at that cool new CSV!
  * Explain that if we wanted to, we could comment out the print commands, but they're cool to look at so we'll leave them and helpful for troubleshooting.
  * Ask for questions

Use OpenRefine to Clean CSV
---------------------------

(20 minutes)

  * Create Project
  * Select our new CSV file
  * Configure Parsing Options (check for headers, check that's its delimited by the right character, explain other options)
  * Give it a name
  * Create project!
  * Create a working column
  * Tour: Text Facet on filename
  * Tour: 50 rows
  * Tour: Next, Next, etc.
  * Tour: Filter on particular filename, say that you could do this to more than one
  * Tour: Filter on subject, show '--', show regex of opposite [^\-\-]
  * Tour: Filter for pipe (|) followed by letter
  * Trim leading and trailing whitespace
  * Tour: Show change all to uppercase
  * Tour: Undo/Redo undo
  * Facet on subject
  * Fix a couple there
  * Then...
  * Cluster and edit (it's in Edit Cells, don't forget)
  * Show the different keying functions
  * Select a couple boxes
  * Write in New Cell Value
  * Merge and recluster
  * Repeat a couple times...
  * Filter on subjects that don't have punctuation at the end (period and parenthesis)
  * Undo/Redo and Extract
  * Could copy and paste this to replay on new data...
  * GREL to transform a department name
  * Split on '--'
  * Undo that
  * Once you're happy, export a CSV named subjects_clean.csv

Use Python and LXML to Update Original XML
------------------------------------------

  * Depending on time, either explain or do put_subjects.py
  * Commit changes to GitHub and show differences between old and new versions of subjects.

Use the exported CSV, open question of if we just have it ready or write it out, but will have opportunity to talk about indexes, and that they start with zero, reading and writing in CSV and LXML, setting row to variable using same variables, still need a loop, talk about either new EAD or overwrite EAD, have accidentally deleted things (and why backups are important), look at a before and after shot of the CSV (on GitHub).

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
