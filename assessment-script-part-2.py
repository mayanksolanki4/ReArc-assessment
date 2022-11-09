import requests
from bs4 import BeautifulSoup

def main():
	url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
	r = requests.get(url, allow_redirects=True)
	html = r.content.decode('utf-8')
	soup = BeautifulSoup(html, 'html.parser')

	with open('path/to/download/file.json', 'w') as file:
			file.write(str(soup))
		
if __name__ == "__main__":
    main()