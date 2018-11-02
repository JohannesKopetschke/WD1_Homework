import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

import urllib
import random

from BeautifulSoup import BeautifulSoup

url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urllib.urlopen(url).read()
soup = BeautifulSoup(response)

quotes = soup.findAll('p',limit=5, attrs={'class': 'quoteContent'})
for quote in quotes:
    print quote.text

