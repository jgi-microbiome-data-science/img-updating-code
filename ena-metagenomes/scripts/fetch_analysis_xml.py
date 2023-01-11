import urllib.request
import json
import os
import sys
from bs4 import BeautifulSoup

accession = sys.argv[1] #"ERZ483" "ERZ096912" # 
            
# get html
site = "https://www.ebi.ac.uk/ena/browser/api/xml/%s" % accession
urlopen = urllib.request.urlopen(site)
html = urlopen.read() 

# write data
outdir = "data/xml/analyses"
if True: #html.find(b"fasta.gz") != -1:
    with open("%s/%s" % (outdir, accession), "wb") as out:
        out.write(html)
