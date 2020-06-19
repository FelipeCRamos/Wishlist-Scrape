import re
import requests
from bs4 import BeautifulSoup as bSoup
import cloudscraper

class ML():
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        # Open the link
        try:
            scraper = cloudscraper.create_scraper()
            response = scraper.get(link)
            page = response.text
        except Exception:
            print("Link Error: %s" % link)
            infos = {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}
            return infos

        infos = dict()
        soup = bSoup(page, 'html.parser')

        # Title fetch
        try:
            infos['title'] = soup.h1.string.replace('\n', '').replace('\t', '')
        except Exception as e:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        try:
            infos['price'] = soup.fieldset.span.span['content']
            infos['discount'] = False

        except Exception as e:
            raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        infos['price'] = float(infos['price'])

        # Everything went OK by this point
        self.fetched = True
        return infos
