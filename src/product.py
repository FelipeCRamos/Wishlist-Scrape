#!/usr/bin/env python3

import re                   # Regex module
from sites.api import choose_api # Sites API's
from sites.product_model import ProductModel

class Product:
    '''
    Class to hold product details
    '''
    def __init__(self, link):
        self.link = link        # Product link
        self.fetched = False    # Fetch state
        self.title = ""
        self.price = 0.0
        self.hasDiscount = False
        self.isIndisponible = False
        self.hasError = False

    def __repr__(self):
        return "{}".format(self.link.split('/')[-1])

    def fetch(self):
        if self.link != '' and self.fetched == False:
            # Check which API to use
            self.api = choose_api(self.link)

            # Store product info on the self.info
            info = self.api.fetch(self.api, self.link)
            self.title = info.title
            self.price = info.price
            if(self.price == 0): self.hasError = True
            self.hasDiscount = info.hasDiscount
            self.isIndisponible = info.isIndisponible
            self.fetched = True

        else:
            if self.link == '': raise Exception('Link is empty')

    def get_title(self):
        if(self.title != ''):
            return self.title
        else:
            return f"(no-title: {self.product_name_by_link()})"


    def get_price(self):
        return self.price

    def get_discount(self):
        return self.hasDiscount

    def get_indisponible(self):
        return self.isIndisponible

    def get_error(self):
        return self.hasError

    def product_name_by_link(self):
        return self.link.split('/')[-1]
