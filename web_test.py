########################################################
# Alain M. Lafon, 15.03.2009
# preek.aml@gmail.com
# 
# HTML scraping with Python and BeautifulSoup
# http://dispatched.ch
# http://blog.dispatched.ch/2009/03/15/webscraping-with-python-and-beautifulsoup/
########################################################


import urllib
import urllib2
import string
import sys
from BeautifulSoup import BeautifulSoup
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }
values = {'s' : sys.argv[0] }
data = urllib.urlencode(values)
request = urllib2.Request("http://www.dict.cc/", data, headers)
response = urllib2.urlopen(request)
the_page = response.read()
pool = BeautifulSoup(the_page)
results = pool.findAll('td', attrs={'class' : 'td7nl'})
source = ''
translations = []

for result in results:
    word = 'Hallo!'
    for tmp in result.findAll(text=True):
        word = word + " " + unicode(tmp).encode("utf-8")
    if source == '':
        source = word
    else:
        translations.append((source, word))

for translation in translations:
    print "%s => %s" % (translation[0], translation[1])
