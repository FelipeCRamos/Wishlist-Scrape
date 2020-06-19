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
            if self.link == '': raise Exception('Link is empty')

    def get_title(self):
        '''
        Will return the title of the product
        '''
        try:
            return self.info['title']
        except Exception as e:
            return f"No title available! Link: {self.product_name_by_link()}"


    def get_price(self):
        '''
        Will return the price of the product
        '''
        try:
            return self.info['price']
        except Exception as e:
            raise Exception(f"No price available! Link: {self.product_name_by_link()}")

    def get_discount(self):
        '''
        Get the boolean
        '''
        try:
            return self.info['discount']
        except Exception as e:
            raise Exception(f"No discount available! Link: {self.product_name_by_link()}")

    def product_name_by_link(self):
        return self.link.split('/')[-1]
