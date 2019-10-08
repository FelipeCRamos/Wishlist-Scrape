import re
import requests
from bs4 import BeautifulSoup as bSoup
import pdb

class Kabum():
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        # Open the link
        try:
            response = requests.get(link)
            page = response.text
        except Exception as e:
            print("Link Error: %s" % link)
            return {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}

        infos = dict()
        with open('test.html', 'w') as file:
            file.write(page)
        soup = bSoup(page, 'html.parser')

        # title fetch
        try:
            infos['title'] = soup.article.h1.string
        except Exception as e:
            raise Exception('No title found on the link: %s' % link)

        # price fetch
        try:
            infos['price'] = float(soup.article.find(attrs={'itemprop': 'price'})['content'])
            infos['discount'] = False
        except Exception as e:
            raise Exception('No price found on link: %s' % link)

        self.fetched = True
        return infos
