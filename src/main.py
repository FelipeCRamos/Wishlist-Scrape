#!/usr/bin/env python3

# Wishlist Scrapper
# A program to look out for the current prices onto your wishlist

# Author:
# FelipeCRamos

# Useful libraries
import datetime as dt   # For generating today's info (log generation)
import sys              # Argv manipulating
import re               # Regex things
import threading        # Threads everywhere

# Custom project libraries
import args
import product as pd
import logs

data = dict()
sorted_data = dict()
products = []

class CreateThread(threading.Thread):
    '''
    Thread system, each thread will be responsible for one Product
    '''
    def run(self):
        global data
        global products

        curr = products.pop(0)
        curr_name = curr.link.split('/')[-1]

        print('Fetching... \t{}\n'.format(curr_name[0:40]))

        #  Fetch data & spit onto the dictionary
        if( curr.get_title() in data ):
            data[curr.get_title()] += curr.get_price()
        else:
            data[curr.get_title()] = curr.get_price()


def main(filepath, filename):
    # Tries to open the file for links extraction
    try:
        links_file = open(filepath, 'r')
    except Exception as e:
        print(e)    # Display error msg
        exit()

    # Separate links into a link list
    links = [ link for link in links_file.read().split('\n') if link != '' and link[0] != '#' ]

    # Check if the file isn't empty
    if( len(links) == 0 ):
        print("ERROR: No links found on the file!")
        exit()

    # Create Product list
    global products
    products = [ pd.Product(link) for link in links ]

    for i in range(len(products)):
        CreateThread().start()

    #  while( len(products) != 0 ):
        #  print("")
        #  curr = products.pop(0)
        #  print("Fetching...")
        #  data[curr.get_title()] = curr.get_price()

    # Wait until all threads are done
    while( threading.active_count() != 1 ):
        continue

    # Sort data by price
    global sorted_data
    total_sum = 0
    for item, price in sorted(data.items(), key=lambda x: x[1], reverse=True):
        total_sum += price
        sorted_data[item] = price
        print("R$ {:8.2f}\t{}".format(price, item[0:70]))

    total_sum = round(total_sum, 2)
    sorted_data['TOTAL'] = total_sum

    print('-'*86)
    print("R$ {:8.2f}\t{}".format(total_sum, 'TOTAL'))

if __name__ == "__main__":
    parsed_info = args.parseArgs(sys.argv)

    if parsed_info['parse_fail'] is False:
        main(parsed_info['filepath'], parsed_info['filename'])

        day = dt.datetime.today()

        output_name = \
            parsed_info['output_dir'] + parsed_info['filename'].split('.')[0] +\
            "_{:02d}-{:02d}-{}".format(day.day, day.month, day.year)

        logs.write2json(
            output_name,
            sorted_data
        )
    else:
        exit()
