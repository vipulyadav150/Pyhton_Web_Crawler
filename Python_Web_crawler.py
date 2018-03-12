import requests
from bs4 import BeautifulSoup


def spider_build():

        url = 'http://www.india.com/travel/articles/10-of-the-best-travel-agencies-in-india-that-will-make-trip-planning-a-cake-walk-for-you/'
        print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")

        for link in soup.findAll('a',{'rel':'nofollow'}):
            title = link.string
       
            href = link.get('href')
            print('Title : ' + title)
            print(href)

spider_build()
