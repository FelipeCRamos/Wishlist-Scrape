import re
import requests
from bs4 import BeautifulSoup
import pdb
import cloudscraper
from .fetcher import *
#  from .api import ProductModel

class Terabyte(Fetcher):
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
            if response.status_code < 200 and response.status_code > 299:
                raise Exception("Ops... Something went wrong! Error: {}"\
                          .format(response.status_code))
        except Exception:
            print("Link Error: %s" % link)
            return ProductModel(
                title = link.split('/')[-1],
                price = 0.0,
            )

        product = ProductModel()
        soup = BeautifulSoup(page, 'html.parser')

        # Getting title
        try:
            product.title = soup.find('h1', 'tit-prod').text
        except:
            product.title = f"null ({link})"
            raise Exception("No title found on the link: %s" % link)

        # Getting price
        try:
            product.price = float(soup.find('p', 'valVista').text.strip()[3:].replace('.', '').replace(',', '.'))
            product.hasDiscount = False
        except:
            if soup.find('div', 'indisponivel') != None or soup.find('button', 'btn-exclusivo') != None:
                # Unavailable product
                product.isIndisponible = True
                try:
                    product.price = float(soup.find('p', 'p3').span.text.strip()[3:].replace('.','').replace(',', '.'))
                except:
                    product.price = 0
            else:
                raise Exception("No price found on link: %s" % link)

        # Everything went OK by this point
        self.fetched = True
        return product
