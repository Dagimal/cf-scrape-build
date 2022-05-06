import cloudscraper
import sys
import re
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
url = scraper.get('https://www.creativefabrica.com/product/3d-festive-lantern-svg-cut-file-set/')
soup = BeautifulSoup(url.text, 'html.parser')

urls = []

def link_url():
	for link in soup.find_all('a'):
		link_loop = link.get('href')
		regexp = re.compile(r'/product/')
		if regexp.search(link_loop):
			print(link_loop)


link_url()
