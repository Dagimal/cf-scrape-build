
def image_url():
	for link in soup.find_all('img'):
		link_loop = link.get('src')
		print(link_loop)