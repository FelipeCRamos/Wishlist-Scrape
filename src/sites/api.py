#!/usr/bin/env python3

import re
from urllib.request import *

from sites.kabum import Kabum
from sites.mercadolivre import ML
from sites.terabyte import Terabyte

class Fetcher:
    '''
    Fetcher base class
    '''
    def __init__(self):
        self.fetched = False

    def fetch(self, link):
        pass

def choose_api(link):
    '''
    Function that will choose the correct API for a given link
    '''
    # Possible domains and it's correspondent API's
    domains = {
        'kabum.com.br': Kabum,
        'terabyteshop.com.br': Terabyte,
        'mercadolivre.com.br': ML,
    }

    # Now, let's find the domain of the link
    for domain in domains:
        result = re.search(domain, link)

        if result != None:
            return domains[domain]

    # if the for loop has finished, no API was found
    raise Exception('No API found for the link: {}'.format(link))
