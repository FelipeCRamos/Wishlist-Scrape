#!/usr/bin/env python3

class Fetcher:
    ''' Fetcher base class '''
    def __init(self):
        self.fetched = False

    def fetch(self, link):
        pass

    def get_title(self, soup):
        pass

    def get_price(self, soup):
        pass

