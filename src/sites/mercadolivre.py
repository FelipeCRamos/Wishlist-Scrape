import re
import requests

class ML():
    def fetch(self, link):
        '''
        Will return a Dictionary with:
        - title -> String
        - price -> Float
        - discount -> Boolean
        '''

        patterns = {
            'title': re.compile(r'''<h1 class="item-title__primary\s">\n\t\t(.+)\n\t</h1>'''),
            'regular_price': re.compile(r'''class="price-tag-symbol"\scontent="(.+)"'''),
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
            raise Exception('No price found on link: %s' % link)

        # Convert price to a float
        infos['price'] = float(infos['price'])

        # Everything went OK by this point
        self.fetched = True
        return infos
