#!/usr/bin/env python
# A lot of this code is from Christian Wyglendowski found at http://www.esvapi.org/api#verse
# Adapted for Drafts & Pythonista on iOS by @pfcbenjamin
# Corresponding Drafts action [available here](http://drafts4-actions.agiletortoise.com/a/1NA)


import urllib
import sys
#import console
#import clipboard
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

# passage = clipboard.get() # the Drafts action

passage = "John 3:16\nPs 8\nRomans 3:23\nRomans 6:23"

# this is a working version to count the number of lines

lines = str.splitlines(passage)

for i, v in enumerate(lines):
	totallines = i

# end of section

passages = lines
for passage in passages:
   print '**' + passage + '**', bible.doPassageQuery(passage)

"""
index = 0

while index <= totallines:
	bibletext = bible.doPassageQuery(passage)
	fulltext = '## ' + passage + '\n' + bibletext
	print fulltext
	index += 1
"""


# bibletext = bible.doPassageQuery(passage) # This was used before I got the loop in lines 54-56 above.

# fulltext = '##' + passage + '\n' + bibletext

# url = 'drafts4://x-callback-url/create?text=' + urllib.quote(fulltext) #

# check to see that drafts is installed. probably not necessary, but...
#if webbrowser.can_open('drafts4://') == True:
#	webbrowser.open(url)

'''this is Eric Pramono's code for LCP actions. Save for possible future usage with LCP in addition to Drafts

encodedscheme = urllib.quote(urlscheme)

if (mode == 1):
  url = 'dayone://post?entry=' + urllib.quote(result)
elif (mode == 2):
  url = 'onewriter://x-callback-url/append?path=Documents&name=Sermon%20Notes.md&type=local&text=%0A' + urllib.quote('_' + result + '_\n')
elif (mode == 3):
  url = 'launch://x-callback-url/messaging?body=' + urllib.quote(ov + '\n\n' + urlscheme) + '&x-success=' + encodedscheme
else:
  url = 'launch://x-callback-url/messaging?body=' + urllib.quote(book + ' ' + cv + '\n\nLink: ' + urlscheme) + '&x-success=' + encodedscheme

webbrowser.open(url)'''
