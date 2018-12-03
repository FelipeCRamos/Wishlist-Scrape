if __name__ == "__main__":
    print("ERROR: You cannot run this script.")
    exit()

from fetcher import Fetcher

class Product:
    def __init__(self, p_link, p_site):
        '''
        Default constructor, initializes the product link and price,
        setup the fetcher
        '''
        self.link = p_link          # product link
        self.api = Fetcher(p_site)  # product fetcher
        self.price = 0

    def getPrice(self, force_update=False):
        '''
        Function to get product price, calling the API for the value
        '''
        # if not already fetched, fetch it
        if( self.price == 0 or force_update == True ):
            self.price = self.api.getInfo(self.link)['value']
            return self.price

        # just return the already checked value
        else:
            return self.price

    def getName(self):
        '''
        Function to get product name, calling the API details
        '''
        self.name = self.api.getInfo(self.link)['name']
        return self.name
