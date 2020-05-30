import requests #to download requests module :  pip3/pip install requests

from bs4 import BeautifulSoup # pip3 install beautifulSoup4

url = 'https://github.com/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a', href= True):
	#ok now i'm gonna retrieve all 'https://'links only
	if link['href'].startswith('https://'):
		print(link['href'])
	# as you can see it works just fine 
