#!/usr/bin/env python3
#coding: utf-8

# Price Fetcher
# A simple log generator for getting current prices on specified products.
# Author: FelipeCRamos
# Version: 0.2.2

from product import Product

import datetime as dt
import sys
import json
import re
import threading

data = dict()
products = []

class FetchUrl(threading.Thread):
    '''
    Threads system, will fetch data from site and store-it on the data dict
    '''
    def run(self):

        global data         # Where the data will be inserted
        global products     # product list

        curr = Product(products.pop(0), sys.argv[2])

        prod_price = float(curr.getPrice())
        prod_name = curr.getName()

        #  print("@thread: {} fetchind data...".format(threading.active_count()))
        data[prod_name] = prod_price

pattern_pc_name = re.compile(r'/(.+)\.\w+') # re to get the path/<filename>.ext

def main():

    input_f = open(sys.argv[1])
    input_name = pattern_pc_name.search(sys.argv[1]).group(1)

    global products
    products = [ line for line in input_f.read().split('\n') if line != '' ]


    print("STATUS: Fetchind data... Please wait.")
    for i in range(len(products)):
        new_thread = FetchUrl(name = "Thread@{}".format(i+1))
        new_thread.start()

    # wait for all threads to finish
    while( threading.active_count() != 1 ):
        continue

    print("\nSTATUS: Fetching complete, now let's get the results!")
    print("-" * 80)

    global data
    sorted_data = dict()

    # exibit and calculate the sum of all prices
    price_sum = 0
    for item, price in sorted(data.items(), key=lambda x: x[1], reverse=True):
        price_sum += price
        print("R$ {:10.2f}\t{}".format(price, item))
        sorted_data[item] = price

    print("-" * 80)
    print("R$ {:>10.2f}\tTOTAL".format(price_sum))
    print("R$ {:>10.2f}\tTOTAL W/ CARD TAX (15% +/-)".format(price_sum * 1.15))

    data["TOTAL"] = price_sum
    data["TOTAL W/ TAXES (15%)"] = price_sum * 1.15

    # write on the output file

    day = dt.datetime.today()
    output_filename = "{}_{:02d}-{:02d}-{}_{:02d}-{:02d}".format(
            input_name, day.day, day.month, day.year, day.hour, day.minute)

    try:
        output_file_json = open('logs/' + output_filename + '.json', 'w')
        json.dump(sorted_data, output_file_json, indent="\t", ensure_ascii=False)
    except:
        print("Output file could not be written, make sure the ./logs folder exist.")
        exit()

if __name__ == "__main__":
    # execute only if run as script
    if len(sys.argv) == 3:
        main()
        day = dt.datetime.today()
        print("Generated on {:02d}/{:02d}/{} at {:02d}:{:02d}".format(
            day.day, day.month, day.year, day.hour, day.minute))
    else:
        print("ERROR: Incorrect number of arguments, please read the README.md")
        exit()
