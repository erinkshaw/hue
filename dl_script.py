from lxml import html
from bs4 import BeautifulSoup
import urllib.request
import re, requests, zipfile, io, os, sys

def hue_scraper():
  try:
    # grabbing and parsing our html
    base = 'http://uadata.org'
    page = requests.get('http://uadata.org/hue/')
    soup = BeautifulSoup(page.text, 'html.parser')

    # get all dem links
    a = soup.find_all('a')

    # loop through all anchor tags in the html
    for link in a:

      # relative url
      url = base + link.get('href')

      # grab specific filename from url
      file_name = url.split('/')[-1]

      # regex to identify links that hold data about manhattan or brooklyn
      man = re.search('manhattan', url, re.IGNORECASE)
      brook = re.search('brooklyn', url, re.IGNORECASE)

      if man or brook:
        print(f'saving {file_name} to data directory...')
        urllib.request.urlretrieve(url, f'data/{file_name}')

        if url[-3:] == 'zip':
            # ..then we need to find the file and then unzip it
            print(f'unzipping {file_name}...')
            z = zipfile.ZipFile(f'data/{file_name}', mode='r')
            z.extractall(path='data/')

            # ..now it would be nice to delete the zip files
            print(f'deleting {file_name}...')
            os.remove(f'data/{file_name}')

  except requests.exceptions.RequestException as e:
      # catastrophic error. bail.
      print (e)
      sys.exit(1)

hue_scraper()
