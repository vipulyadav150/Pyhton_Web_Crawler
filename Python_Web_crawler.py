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
            brochure_download_link(href)


def brochure_download_link(main_url):
    source_code = requests.get(main_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    #print(soup)
    for link_down in soup.findAll('div',{'class':'customer-services'}):
      #  for head in link_down.findAll('h2'):
          #  print(head)
            #for un_list in head.findAll('ul'):
             for un_list in link_down.findAll('ul'):
              #  print(un_list.findAll('li')[0].findAll('a')[0])
                l = un_list.findAll('li')[0].findAll('a')[0]
                # for list in un_list.findAll('li'):
                #  for link_fresh in list.findAll('a'):
                href_new = str(main_url) + l.get('href')
                print("Download Brochure from : " + href_new)



        #title_new = link_down.string
        #print(title_new)








spider_build()
