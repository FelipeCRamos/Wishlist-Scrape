#!/usr/bin/env python3

import re

from sites.kabum import Kabum
from sites.mercadolivre import ML
from sites.terabyte import Terabyte
from sites.amazon import Amazon


def choose_api(link):
    '''
    Function that will choose the correct API for a given link
    '''
    # Possible domains and it's correspondent API's
    domains = {
        'kabum.com.br': Kabum,
        'terabyteshop.com.br': Terabyte,
        'mercadolivre.com.br': ML,
        'amazon.com.br': Amazon,
    }

    # Now, let's find the domain of the link
    for domain in domains:
        result = re.search(domain, link)

        if result != None:
            return domains[domain]

    # if the for loop has finished, no API was found
    raise Exception('No API found for the link: {}'.format(link))
