#!/usr/bin/env python
# A lot of this code is from Christian Wyglendowski found at http://www.esvapi.org/api#verse
# Adapted for Drafts & Pythonista on iOS by @pfcbenjamin
# Corresponding Drafts action [available here](http://drafts4-actions.agiletortoise.com/a/1NA)

import urllib
import sys
import console
import clipboard
import webbrowser
import urllib
import urllib2

class ESVSession:
    def __init__(self, key):
        options = ['include-short-copyright=0',
                   'output-format=plain-text',
                   'include-passage-horizontal-lines=0',
                   'include-heading-horizontal-lines=0',
                   'include-headings=0',
                   'include-subheadings=0',
                   'include-selahs=0',
                   'line-length=0',
                   'include-passage-references=0',
                   'include-footnotes=0']
        self.options = '&'.join(options)
        self.baseUrl = 'http://www.esvapi.org/v2/rest/passageQuery?key=IP'

    def doPassageQuery(self, passage):
        passage = passage.split()
        passage = '+'.join(passage)
        url = self.baseUrl + '&passage=%s&%s' % (passage, self.options)
        page = urllib.urlopen(url)
        return page.read()

key = 'IP' # You can access the ESV text using the key "IP" (without the quotes). This key limits you to 5,000 queries per day from a single IP address. You are bound by the below conditions of use, including the non-commercial aspects.

bible = ESVSession(key)

reference = clipboard.get() # the Drafts action sets the draft to the clipboard. I did this because it's easy and I'm not good at Python. If you have a better way, let me know!
reference = reference.encode() # make the Unicode text a String - otherwise 'splitlines' throws a fit.
reference = reference.title() # make those lowercase characters upper case

# this is a working version to count the number of lines

lines = str.splitlines(reference)

for i, v in enumerate(reference):
	totallines = i

# end of section

fulltext = []

passages = lines
for reference in passages:
   bibletext = '**' + reference + '**' + bible.doPassageQuery(reference)
   fulltext.append(bibletext)

fulltext = '\n\n'.join(fulltext) # Converts list to string

url = 'drafts4://x-callback-url/create?text=' + urllib.quote(fulltext)

# check to see that drafts is installed. probably not necessary, but...
if webbrowser.can_open('drafts4://') == True:
	webbrowser.open(url)
