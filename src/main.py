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
import argparse         # cool arg parser

# Custom project libraries
import args
import product as pd
import logs

data = dict()
repeatData = dict()
sorted_data = dict()
products = []

THREAD_ENABLE = True
VERBOSE_ENABLE = False
CURRENT_VERSION = "0.2.4"

def addFetchedData(title, price):
    global data

    if title is not None and price is not None:
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

    if VERBOSE_ENABLE:
        print("Fetching... \t{}\n".format(curr_name[0:40]))

    try:
        addFetchedData(curr.get_title(), curr.get_price())
    except Exception as e:
        print(e)

class CreateThread(threading.Thread):
    '''
    Thread system, each thread will be responsible for one Product
    '''
    def run(self):
        # Make the fetch on the next product
        fetchNext()

def main(filepath, folderpath):
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

    for _ in products:
        if THREAD_ENABLE:
            CreateThread().start()
        else:
            fetchNext()

    # Wait until all threads are done
    while threading.active_count() != 1:
        continue

    # Sort data by price
    global sorted_data
    total_sum = 0
    for item, price in sorted(data.items(), key=lambda x: x[1], reverse=True):
        total_sum += price

        no_occur = repeatData[item] if item in repeatData else 1

        itemName = "({}x) - {}".format(no_occur, item)
        sorted_data[itemName] = price

        print("R$ {:8.2f}\t({}x) {}".format(price, no_occur, item[0:70]))

    total_sum = round(total_sum, 2)
    sorted_data['TOTAL'] = total_sum

    print('-'*86)
    print("R$ {:8.2f}\t{}".format(total_sum, 'TOTAL'))
    print('-' * 90)

    output_filepath = folderpath + ("/" if folderpath[-1] != '/' else "") + \
        filepath.split('.')[0].split("/")[-1]
    print("Output filepath: {}".format(output_filepath))
    logs.write2json(output_filepath, sorted_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch prices of a given wishlist")

    parser.add_argument('-l', '--list', required=True, help="List of products (one link per line)", metavar=('list.txt'))
    parser.add_argument('-o', '--output', required=False, help="Output fetched prices", metavar=('output_file.json'), default='.')
    parser.add_argument('-T', '--no-threading',  required=False, help="Disable parallel fetches", action='store_true')

    args = parser.parse_args()

    if args.no_threading:
        print("[WARNING] No threads!")
        THREAD_ENABLE = False

    try:
        main(args.list, args.output)

    except Exception as inst:
        print('ERROR:', inst)

    exit()
