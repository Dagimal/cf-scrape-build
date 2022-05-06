import cloudscraper
import sys
import re
from bs4 import BeautifulSoup

OUTPUT_FILENAME = 'cf.txt'

scraper = cloudscraper.create_scraper()
url = scraper.get('https://www.creativefabrica.com/product/3d-festive-lantern-svg-cut-file-set/')
soup = BeautifulSoup(url.text, 'html.parser')

urls = []

def link_url():
	for link in soup.find_all('a'):
		link_loop = link.get('href')
		regexp = re.compile(r'/product/')
		if regexp.search(link_loop):
			f = open(OUTPUT_FILENAME, 'a')
			print(link_loop, file=f)


link_url()
