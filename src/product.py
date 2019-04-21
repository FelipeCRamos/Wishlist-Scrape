#!/usr/bin/env python3

import re                   # Regex module
from sites.api import *     # Sites API's

class Product:
    '''
    Class to hold product details
    '''
    def __init__(self, link):
        self.link = link        # Product link
        self.fetched = False    # Fetch state

    def __repr__(self):
        return "{}".format(self.link.split('/')[-1])

    def fetch(self):
        '''
        Will be responsible for the comunication with the correct API
        '''
        if self.link != '' and self.fetched == False:
            # Check which API to use
            self.api = choose_api(self.link)

            # Store product info on the self.info
            self.info = self.api.fetch(self.api, self.link)
            self.fetched = True

        else:
            if self.link == '':
                raise Exception('Link is empty')

    def get_title(self):
        '''
        Will return the title of the product
        '''
        if self.fetched == False:
            self.fetch()
            return self.info['title']

        else:
            return self.info['title']

    def get_price(self):
        '''
        Will return the price of the product
        '''
        if self.fetched == False:
            self.fetch()
            return self.info['price']
        else:
            return self.info['price']

    def get_discount(self):
        '''
        Get the boolean
        '''
        if self.fetched == False:
            self.fetch()
            return self.info['discount']
        else:
            return self.info['discount']
