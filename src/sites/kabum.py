#coding: utf-8
if __name__ == "__main__":
    print("ERROR: You cannot run this script.")
    exit()

from urllib.request import *    # url handling tools
import re                       # regex ftw

class Kabum:
    '''
    API for fetching data from Kabum
    '''
    def __init__(self):
        ''' Default Constructor '''
        self.name = "Kabum"

    def fetch(self, link):
        pat_value = re.compile(r'''<meta\sitemprop="price"\scontent="(.+)">''')
        pat_value_discount = re.compile(r'''preco_desconto_avista-cm">R\$\s(\d*\.?\d*\.?\d*\,\d*)<''')
        pat_title = re.compile(r'''class="titulo_det">(.+)</''')

        error = False
        title_error = False
        desconto = False

        with urlopen(Request(link)) as response:
            page = response.read().decode('ISO-8859-1') # kabum needs ISO-8859-1

            # Search for the value of the product
            search_result = pat_value.search(page)
            if search_result is not None:
                self.price = float(search_result.group(1))

            else:
                # it's on promo!
                search_result = pat_value_discount.search(page)
                if search_result is not None:
                    self.price = search_result.group(1)
                    # in order to do not break further conversions
                    self.price = self.price.replace('.', '').replace(',','.')
                    desconto = True
                else:
                    # it's something else
                    print("ERROR: Price not found!")
                    # Creates an html log file
                    with open('error_page.html', 'w') as error_output:
                        error_output.write(page)
                    self.price = None
                    error = True

            search_result = pat_title.search(page)

            if search_result is not None:
                self.title = search_result.group(1)

            else:
                title_error = True
                self.title = "[Could not fetch]"

    def getPrice(self):
        '''
        Return fetched value for product
        '''
        if self.price is not None:
            return self.price
        else:
            return 0.0001

    def getName(self):
        '''
        Return fetched value for getName
        '''
        if self.title is not None:
            return self.title[0:-1]
        else:
            return "No Title"
