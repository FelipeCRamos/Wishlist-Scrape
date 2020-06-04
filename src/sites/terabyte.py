import re
import requests
from bs4 import BeautifulSoup
import pdb

class Terabyte():
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
            print(f"[STATUS] Getting link: {link}")
            page = response.text
            if response.status_code != 200:
                Exception("Ops... Something went wrong! Error: {}"\
                          .format(response.status_code))
        except Exception as e:
            print("Link Error: %s" % link)
            infos = {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}
            return infos

        infos = dict()

        soup = BeautifulSoup(page, 'html.parser')

        # Getting title
        try:
            infos['title'] = soup.find('h1', 'tit-prod').text
        except:
            raise Exception("No title found on the link: %s" % link)

        # Getting price
        try:
            infos['price'] = float(soup.find('p', 'valVista').text.strip()[3:].replace('.', '').replace(',', '.'))
            infos['discount'] = False
        except:
            if soup.find('div', 'indisponivel') != None or soup.find('button', 'btn-exclusivo') != None:
                # Unavailable product
                infos['price'] = 0
            else:
                raise Exception("No price found on link: %s" % link)

        # Everything went OK by this point
        self.fetched = True
        return infos
