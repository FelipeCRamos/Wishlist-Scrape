#!/usr/bin/env python3

import json

def write2json(filename, content):
    try:
        output = open(filename + '.json', 'w')
        json.dump(content, output, indent='\t', ensure_ascii=False)
    except Exception as e:
        print(e)
        exit()
