#!/usr/bin/env python3
#coding: utf-8

# Price Fetcher
# A simple log generator for getting current prices on specified products.
# Author: FelipeCRamos
# Version: 0.2.1

from product import Product

import datetime as dt
import sys
import json
import re

pattern_pc_name = re.compile(r'/(.+)\.\w+')

def main():
    input_f = open(sys.argv[1])
    input_name = pattern_pc_name.search(sys.argv[1]).group(1)
    input_site = sys.argv[2]
    products = [ line for line in input_f.read().split('\n') if line != '' ]

    total_price = 0

    data = dict()
    for product in products:
        curr = Product(product, input_site)
        prod_price = float(curr.getPrice())
        prod_name = curr.getName()
        print("R$ {:>10.2f}\t{}".format(prod_price, prod_name))

        total_price += prod_price
        data[prod_name] = prod_price

    print("-" * 80)
    print("R$ {:>10.2f}\tTOTAL".format(total_price))
    print("R$ {:>10.2f}\tTOTAL W/ CARD TAX (15% +/-)".format(total_price * 1.15))
    data["TOTAL"] = total_price
    data["TOTAL W/ TAXES (15%)"] = total_price * 1.15

    # write on the output file

    day = dt.datetime.today()
    output_filename = "{}_{:02d}-{:02d}-{}_{:02d}-{:02d}".format(
            input_name, day.day, day.month, day.year, day.hour, day.minute)


    try:
        output_file_json = open('logs/' + output_filename + '.json', 'w')
        json.dump(data, output_file_json, indent="\t", ensure_ascii=False)
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
