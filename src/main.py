#!/usr/bin/env python3

# Wishlist Scrapper
# A program to look out for the current prices onto your wishlist

# Author:
# FelipeCRamos

# Useful libraries
import datetime as dt   # For generating today's info (log generation)
import sys              # Argv manipulating
import os
import re               # Regex things
import threading        # Threads everywhere

# Custom project libraries
import args
import product as pd
import logs
import parser

data = dict()
repeatData = dict()
sorted_data = dict()
products = []

THREAD_ENABLE = True

def addFetchedData(title, price):
    global data

    if title in data:
        data[title] += price

        if title in repeatData:
            repeatData[title] += 1
        else:
            repeatData[title] = 2
    else:
        data[title] = price

def fetchNext():
    global products

    curr = products.pop(0)
    curr_name = curr.link.split('/')[-1]

    print("Fetching... \t{}\n".format(curr_name[0:40]))

    addFetchedData(curr.get_title(), curr.get_price())

class CreateThread(threading.Thread):
    '''
    Thread system, each thread will be responsible for one Product
    '''
    def run(self):
        # Make the fetch on the next product
        fetchNext()

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
        if THREAD_ENABLE:
            CreateThread().start()
        else:
            fetchNext()

    # Wait until all threads are done
    while( threading.active_count() != 1 ):
        continue

    # Sort data by price
    global sorted_data
    total_sum = 0
    for item, price in sorted(data.items(), key=lambda x: x[1], reverse=True):
        total_sum += price
        sorted_data[item] = price

        no_occur = repeatData[item] if item in repeatData else 1

        print("R$ {:8.2f}\t({}x) {}".format(price, no_occur, item[0:70]))

    total_sum = round(total_sum, 2)
    sorted_data['TOTAL'] = total_sum

    print('-'*86)
    print("R$ {:8.2f}\t{}".format(total_sum, 'TOTAL'))

if __name__ == "__main__":
    #  parsed_info = args.parseArgs(sys.argv)

    arguments = [
        'l', # -l <links-file.txt>
        'o', # -o <output_folder/.>
    ]

    necessaryArguments = [ 'l' ]

    try:
        parsedArgs = parser.Parser(sys.argv, arguments, necessaryArguments).parseArgs()
        print(os.getcwd())
        if 'o' in parsedArgs:
            main(parsedArgs['l'], parsedArgs['o'])
        else:
            main(parsedArgs['l'], ".")

    except Exception as inst:
        print('ERROR:', inst)

    exit()

    if parsed_info['parse_fail'] is False:
        main(parsed_info['filepath'], parsed_info['filename'])

        day = dt.datetime.today()

        output_name = \
            parsed_info['output_dir'] + parsed_info['filename'].split('.')[0] +\ "_{:02d}-{:02d}-{}".format(day.day, day.month, day.year)

        logs.write2json(
            output_name,
            sorted_data
        )
    else:
        exit()
