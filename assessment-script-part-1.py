import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://download.bls.gov/pub/time.series/pr/'
    r = requests.get(url, allow_redirects=True)
    html = r.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    atags = soup.find_all('a')
    for t in atags[1:]:
        str = t.get('href', None)
        str=str.split('/')
        url2 = url+str[4]
        r = requests.get(url2, allow_redirects=True)
        html = r.content.decode('utf-8')
        with open('path/to/download/files/'+str[4], 'w') as file:
            file.write(html)
        
if __name__ == "__main__":
    main()