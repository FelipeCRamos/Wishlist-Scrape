import re
import requests
from . import api

class Kabum(api.Fetcher):
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        patterns = {
            'title': re.compile(r'''class="titulo_det">(.+)</'''),
            'regular_price': re.compile(r'''<meta\sitemprop="price"\scontent="(.+)">'''),
            'discount_price': re.compile(r'''preco_desconto_avista-cm">R\$\s(\d*\.?\d*\.?\d*\,\d*)<'''),
        }

        # Open the link
        try:
            response = requests.get(link)
            if(response.status_code != 200):
                raise Exception(f"Error {response.status_code} on link {link.split('/')[-1]}")
            page = response.text
        except Exception as e:
            print(f"Link Error: {e}")

            # will return a "null" infos object
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
            discount_price_re = patterns['discount_price'].search(page)
            try:
                infos['price'] = discount_price_re.group(1)
                infos['discount'] = True
            except Exception as ej:
                raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        if infos['discount'] == False:
            infos['price'] = float(infos['price'])
        else:
            infos['price'] = float(infos['price'].replace('.','').replace(',', '.'))

        # Everything went OK by this point
        self.fetched = True
        return infos
