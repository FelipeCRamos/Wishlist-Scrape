import re
import requests
from bs4 import BeautifulSoup as bSoup
import cloudscraper
from .fetcher import *
import pdb
#  from .api import ProductModel

class ML(Fetcher):
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - isWithDiscount -> Boolean
        '''

        # Open the link
        try:
            scraper = cloudscraper.create_scraper()
            response = scraper.get(link)
            page = response.text
        except Exception:
            print("Link Error: %s" % link)
            return ProductModel(
                title = link.split('/')[-1],
                price = 0.0,
                hasError = True,
            )

        product = ProductModel()
        soup = bSoup(page, 'html.parser')

        # Title fetch
        try:
            product.title = soup.h1.string.replace('\n', '').replace('\t', '')
        except Exception as _:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        try:
            product.price = soup.fieldset.span.span['content']
            product.hasDiscount = False

        except Exception as _:
            raise Exception('No price found on link: %s' % link)

        try:
            if(soup.find('p', 'item-status-notification__title')):
                product.isIndisponible = True
        except:
            product.isIndisponible = False

        # Convert price to a float
        product.price = float(product.price)

        # Everything went OK by this point
        self.fetched = True
        return product
