from lxml import html
from bs4 import BeautifulSoup
import re, requests, zipfile, io

def hue_scraper():
  base = 'http://uadata.org'
  page = requests.get('http://uadata.org/hue/')
  soup = BeautifulSoup(page.text, 'html.parser')
  a = soup.find_all('a')
  for link in a:
    url = base + link.get('href')
    man = re.search('manhattan', url, re.IGNORECASE)
    brook = re.search('brooklyn', url, re.IGNORECASE)
    if man or brook:
      if url[-3:] == 'pdf':
        print('hey pdf', url)
      # if pdf -->
      elif url[-3:] == 'zip':
        print('hey zip', url)
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
      # if zip -->

      # print(requests.get(base + url))
      # print(base + url)



hue_scraper()



# request website interpreter
# find all reference to 'brooklyn' or 'manhattan'
  # will i need to use regex for this?
# get links
# download links to HUE directory!
