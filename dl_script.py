from lxml import html
from bs4 import BeautifulSoup
import requests
import re

def hue_scraper():
  base = 'http://uadata.org'
  page = requests.get('http://uadata.org/hue/')
  soup = BeautifulSoup(page.text, 'html.parser')
  a = soup.find_all('a')
  for link in a:
    man = re.search('manhattan', link.get('href'), re.IGNORECASE)
    brook = re.search('brooklyn', link.get('href'), re.IGNORECASE)
    if man or brook:
      print(base + link.get('href'))


hue_scraper()



# request website interpreter
# find all reference to 'brooklyn' or 'manhattan'
  # will i need to use regex for this?
# get links
# download links to HUE directory!
