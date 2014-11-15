#!/usr/bin/env python
#sample code by Christian Wyglendowski found at http://www.esvapi.org/api#verse

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

key = 'IP'

bible = ESVSession(key)

'''This is remnant code from the Drafts 3 action before the clipboard was available.
book = sys.argv[1]
verse = sys.argv[2]
third = sys.argv[3]

passage = book + ' ' + verse + ' ' + third'''

passage = clipboard.get()

bibletext = bible.doPassageQuery(passage)

fulltext = '**' + passage + '**' + '\n' + bibletext

url = 'drafts4://x-callback-url/create?text=' + urllib.quote(fulltext)

# check to see that drafts is installed. probably not necessary, but...
if webbrowser.can_open('drafts4://') == True:
	webbrowser.open(url)

'''this is Eric Pramono's code for LCP actions.

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
