#coding: utf-8
if __name__ == "__main__":
    print("ERROR: You cannot run this script.")
    exit()

from urllib.request import *
import re

class MercadoLivre:
    def __init__(self):
        self.name = "MercadoLivre"
        self.baselink = ""

    def __repr__(self):
        return "Fetcher Model: {} on {}".format(self.name, self.baselink)

    def fetch(self, link):
        pattern_value = re.compile(r'''class="price-tag-symbol"\scontent="(.+)"''')
        pattern_value_discount = re.compile(r'''"preco_desconto_avista-cm">R\$\s(\d+,\d+)</span>''') # dunno yet
        pattern_title = re.compile(r'''<h1 class="item-title__primary\s">\n\t\t(.+)\n\t</h1>''')

        error = False
        title_error = False

        desconto = False

        with urlopen(Request(link)) as response:
            page = response.read().decode('utf-8')

            # Search for the value of the product
            search_result = pattern_value.search(page)
            if search_result is not None:
                self.price = float(search_result.group(1))
            else:
                # it's on promo!
                search_result = pattern_value_discount.search(page)
                if search_result is not None:
                    self.price = search_result.group(1)
                    # in order to do not break further conversions
                    self.price = self.price.replace('.', '').replace(',','.')
                    desconto = True
                else:
                    # it's something else
                    self.price = None
                    error = True

            #  self.title = pattern_title.search(page).group(1)
            search_result = pattern_title.search(page)
            if search_result is not None:
                self.title = search_result.group(1)
            else:
                title_error = True
                self.title = "[Could not fetch]"

    def getPrice(self):
        if self.price is not None:
            return self.price
        else:
            return 0.0001

    def getName(self):
        if self.title is not None:
            return self.title
        else:
            return "No Title"
