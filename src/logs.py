#!/usr/bin/env python3

import json

def write2json(filename, content):
    try:
        outputFilename = filename + '.json' if filename[-5:] != '.json' else filename
        #  print("[write2json]: Output filename will be: {}".format(outputFilename))
        output = open(outputFilename, 'w')
        json.dump(content, output, indent='\t', ensure_ascii=False)
    except Exception as e:
        print(e)
        exit()
