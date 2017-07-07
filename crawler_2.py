import urllib.request as urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("https://icc-ccs.org/piracy-reporting-centre/live-piracy-report")
soup = BeautifulSoup(page, "lxml") 
for incident in soup('td'):
    try:
        incident['class']
    except KeyError:
        continue
    if incident['class'] == u'jos_fabrik_icc_ccs_piracymap2012___narrations fabrik_element':
        where, linebreak, what = incident.contents[:3]
        print(where.strip())
        print(what.strip())