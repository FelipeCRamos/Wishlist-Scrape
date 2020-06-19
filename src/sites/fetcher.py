#!/usr/bin/env python3

from .product_model import ProductModel

class Fetcher:
    ''' Fetcher base class '''
    def __init(self):
        self.fetched = False

    def fetch(self, link):
        return ProductModel()
