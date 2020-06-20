from .fetcher import *
import re
import requests
#  from .api import ProductModel

class Amazon(Fetcher):
    def fetch(self, link):
        '''
        Will return a ProductModel
        '''

        patterns = {
            'title': re.compile(r'''class="tit-prod">\n*<strong>(.+)</strong>'''),
            'regular_price': re.compile(r'''<p\sid="valVista"\sclass="val-prod\svalVista">R\$\s(\d*\.?\d*\.?\d*\,\d*)\s*</p>'''),
            'empty_store_price': re.compile(r'''\*<span>R\$\s(\d*\.?\d*\.?\d*\,\d*)\s*</span>''')
        }

        # Open the link
        try:
            response = requests.get(link)
            page = response.text
            if response.status_code != 200:
                Exception("Ops... Something went wrong! Error: {}"\
                          .format(response.status_code))
        except Exception as _:
            print("Link Error: %s" % link)
            return ProductModel(
                title = link.split('/')[-1],
                price = 0.0,
                hasErorr = True
            )

        product = ProductModel()
        # Title fetch
        title_re = patterns['title'].search(page)

        try:
            product.title = title_re.group(1)
        except Exception as _:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        regular_price_re = patterns['regular_price'].search(page)
        try:
            product.price = regular_price_re.group(1)
            product.hasDiscount = False
        except Exception as _:
            empty_store_price_re = patterns['empty_store_price'].search(page)
            try:
                product.price = empty_store_price_re.group(1)
                product.hasDiscount = False
                product.isIndisponible = True
            except Exception as _:
                err = open('error_page.html', 'wb')
                err.write(page)

                raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        product.price = float(product.price.replace('.','').replace(',', '.'))

        # Everything went OK by this point
        self.fetched = True
        return product
