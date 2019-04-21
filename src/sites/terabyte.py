import re
import requests

class Terabyte():
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        patterns = {
            'title': re.compile(r'''class="tit-prod">\n*<strong>(.+)</strong>'''),
            'regular_price': re.compile(r'''<p\sclass="val-prod">R\$\s(\d*\.?\d*\.?\d*\,\d*)\s*</p>'''),
            'empty_store_price': re.compile(r'''\*<span>R\$\s(\d*\.?\d*\.?\d*\,\d*)\s*</span>''')
        }

        # Open the link
        try:
            response = requests.get(link)
            page = response.text
        except Exception as e:
            print("Link Error: %s" % link)
            infos = {'title': link.split('/')[-1], 'price': 0.00, 'discount': False}
            return infos

        infos = dict()
        # Title fetch
        title_re = patterns['title'].search(page)

        try:
            infos['title'] = title_re.group(1)
        except Exception as e:
            raise Exception('No title found on the link: %s' % link)

        # Price fetch
        regular_price_re = patterns['regular_price'].search(page)
        try:
            infos['price'] = regular_price_re.group(1)
            infos['discount'] = False
        except Exception as e:
            empty_store_price_re = patterns['empty_store_price'].search(page)
            try:
                infos['price'] = empty_store_price_re.group(1)
                infos['discount'] = False
                infos['empty_store'] = True
            except Exception as ej:
                err = open('error_page.html', 'wb')
                err.write(page)

                raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        infos['price'] = float(infos['price'].replace('.','').replace(',', '.'))

        # Everything went OK by this point
        self.fetched = True
        return infos
