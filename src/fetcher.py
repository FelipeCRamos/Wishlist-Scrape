if __name__ == "__main__":
    print("ERROR: You cannot run this script.")
    exit()

from sites.kabum import Kabum                   # Kabum fetcher
from sites.mercadolivre import MercadoLivre     # MercadoLivre fetcher

class Fetcher:
    '''
    Higher abstraction for site-specific API.
    '''
    def __init__(self, f_website):
        ''' Default constructor '''
        self.site = f_website   # website name
        self.getSiteClass()     # get the correct fetcher for a given website
        self.fetched = False    # useful for optimizing things

    def getSiteClass(self):
        '''
        Set's the API to be used on fetching process
        '''
        # set Kabum class as the fetcher
        if( self.site.lower() == "kabum" ):
            self.ref = Kabum()

        # set MercadoLivre class as the fetcher
        elif( self.site.lower() == "mercadolivre" ):
            self.ref = MercadoLivre()

        # No specified fetcher
        else:
            self.ref = None

    def getInfo(self, link):
        '''
        Returns an dictionary with useful scraped info
        '''
        infos = dict()
        if( self.ref == None ):
            print("ERROR: No valid fetcher provided.")
            return infos

        if self.fetched is False:
            self.ref.fetch(link) # Tries to fetch information
            self.fetched = True

        infos['name'] = self.ref.getName()
        infos['value'] = self.ref.getPrice()
        infos['available'] = True

        return infos

