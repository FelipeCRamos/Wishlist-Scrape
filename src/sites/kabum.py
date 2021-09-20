import re
import requests
from bs4 import BeautifulSoup
#  from .api import ProductModel
from .fetcher import *
import pdb

class Kabum(Fetcher):
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        # Open the link
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response = requests.get(link, headers=headers)
            if(response.status_code == 200):
                page = response.text
            else:
                # TODO: Make error 502 to try again later
                raise Exception(f"Error {response.status_code} on link {link}")
        except Exception as e:
            print(f"Link Error: {e}")

            # will return a "null" infos object
            return ProductModel(
                title = link.split('/')[-1],
                price = 0.0,
                hasError = True
            )

        product = ProductModel()
        soup = BeautifulSoup(page, 'html.parser')

        #  print(soup.find('h1'))
        #  print(soup.find(id='blocoValores').find('h4'))

        #  raise Exception("Stop")

        # Getting title
        try:
            product.title = soup.find('h1').text.strip()
        except:
            product.title = '-'
            raise Exception("No title found on link: $s" % link)

        # Getting price
        try:
            # Normal price
            product.price = float(soup.find(id='blocoValores').find('h4').text[3:].replace('.', '').replace(',', '.'))
            product.hasDiscount = soup.find(id='cardAlertaOferta') != None
        except:
            raise Exception("No price found on link: %s" % link)

        # Everything went OK by this point
        self.fetched = True
        return product
