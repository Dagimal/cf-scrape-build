import cloudscraper
import sys
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

<<<<<<< HEAD
OUTPUT_FILENAME = 'cf_link.txt'
=======
INPUT_FILENAME = ''
MARKDOWN_TEMPLATE = 'markdown-template/blog.md'
OUTPUT_FILENAME = 'cf_fonts.txt'
>>>>>>> cbb3178a3f26150c7a6160720fe1a26da0517f11

scraper = cloudscraper.create_scraper()

# Add Page URL File
#page_link = open('page-url.txt', 'r').readlines()

URL_PATTERN = ''

<<<<<<< HEAD
def scrapeTitle():
=======
def titleScraper():
>>>>>>> cbb3178a3f26150c7a6160720fe1a26da0517f11
	for line in tqdm(range(1405)):
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

<<<<<<< HEAD
def scrapeImage():
    pass

def scrapeContent():
    pass

=======
>>>>>>> cbb3178a3f26150c7a6160720fe1a26da0517f11
# FunctionCall
link_url()
