import cloudscraper
import sys
import re
from bs4 import BeautifulSoup

OUTPUT_FILENAME = 'cf_link.txt'

scraper = cloudscraper.create_scraper()

# Add Page URL File
#page_link = open('page-url.txt', 'r').readlines()

URL_PATTERN = ''

def link_url():
	for line in range(1405):
	#for line in page_link: # Use page_link variables
		#url = scraper.get(line) # Use page_link variables
		url = scraper.get(f'https://www.creativefabrica.com/subscriptions/fonts/script-handwritten/page/{line+1}')
		soup = BeautifulSoup(url.text, 'html.parser')

		for link in soup.find_all('a'):
			link_loop = link.get('href')
			regexp = re.compile(r'/product/')
			if regexp.search(link_loop):
				f = open(OUTPUT_FILENAME, 'a')
				print(link_loop, file=f)

# FunctionCall
link_url()
