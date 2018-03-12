import requests
from bs4 import BeautifulSoup


def spider_spoj(max_pages):
    page = 1
    start = 0
    while page <= max_pages:
         url = 'http://www.spoj.com/problems/classical/sort=6,start=' + str(start)
         print("Page link : "+ url)
         main_links_len = 0
         source_code_main = requests.get(url)
         print(source_code_main)
         plain_text = source_code_main.text
        # print(plain_text)
         main_soup = BeautifulSoup(plain_text,"html.parser")
       #  print(main_soup)
         for link in main_soup.findAll('table',{'class':'problems table table-condensed table-hover'}):
             for link_one in link.findAll('tbody'):
                 for row in link_one.findAll('td',{'align':'left'}):
                     main_part = row.findAll('a')
                     useable = main_part[0]
                     #for linkers in useable.findAll('href'):
                     prob_link = "http://www.spoj.com/problems/" + useable.get('href')
                     prob_title = useable.string
                     print("Problem : " + prob_title)
                     print(prob_link)







         page +=1
         start +=50
inp_pages = int(input("Enter the Number of Pages to crawl : \n"))
spider_spoj(inp_pages)

