import re
import requests
from bs4 import BeautifulSoup
import pdb
import cloudscraper

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
            scraper = cloudscraper.create_scraper()
            response = scraper.get(link)
            print(f"[STATUS] Getting link: {link}")
            page = response.text
            print(f"response code: {response.status_code}")
            #  if response.status_code != 200:
                #  raise Exception("Ops... Something went wrong! Error: {}"\
                          #  .format(response.status_code))
        except Exception as e:
            print("Link Error: %s" % link)
            print(f"Error: {e}")
            infos = {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}
            return infos

        infos = dict()

        soup = BeautifulSoup(page, 'html.parser')

        # Getting title
        try:
            infos['title'] = soup.find('h1', 'tit-prod').text
        except:
            infos['title'] = f"null ({link})"
            raise Exception("No title found on the link: %s" % link)

        # Getting price
        try:
            infos['price'] = float(soup.find('p', 'valVista').text.strip()[3:].replace('.', '').replace(',', '.'))
            infos['discount'] = False
        except:
            if soup.find('div', 'indisponivel') != None or soup.find('button', 'btn-exclusivo') != None:
                # Unavailable product
                try:
                    infos['price'] = float(soup.find('p', 'p3').span.text.strip()[3:].replace('.','').replace(',', '.'))
                    infos['special'] = True
                except:
                    infos['price'] = 0
                    infos['special'] = False
            else:
                raise Exception("No price found on link: %s" % link)

        # Everything went OK by this point
        self.fetched = True
        return infos
