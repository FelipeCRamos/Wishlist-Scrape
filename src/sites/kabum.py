import re
import requests
from bs4 import BeautifulSoup
#  from .api import ProductModel
from .fetcher import *

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
            response = requests.get(link)
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
            )

        product = ProductModel()
        soup = BeautifulSoup(page, 'html.parser')

        # Getting title
        try:
            product.title = soup.find('h1', 'titulo_det').text.strip()
        except:
            product.title = '-'
            raise Exception("No title found on link: $s" % link)

        # Getting price
        try:
            # Normal price
            product.price = float(soup.find('span', 'preco_desconto').strong.text.strip()[3:].replace('.', '').replace(',', '.'))
            product.hasDiscount = False
        except:
            try:
                # Discount price
                product.price = float(soup.find('div', 'preco_desconto-cm').text[3:].replace('.', '').replace(',', '.'))
                product.hasDiscount = True
            except:
                raise Exception("No price found on link: %s" % link)

        # Everything went OK by this point
        self.fetched = True
        return product
