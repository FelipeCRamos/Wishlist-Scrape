#!/usr/bin/env python3

# Parser Lib

import sys
import random
import re

class Parser:
    ''' Magic functions '''
    def __init__(self, arguments, acceptedArgs = [], necessaryArgs = []):
        self.rawArgs = Parser.splitter(self, arguments)
        self.lookupTable = acceptedArgs
        self.necessaryArgs = necessaryArgs

    ''' Parser methods '''
    def parseArgs(self):
        argumentTable = dict()
        for arg in self.lookupTable:
            # search for that arg on raw_args
            try:
                result = self.rawArgs.index('-' + arg) # TODO: Support '--' on future

                if len(self.rawArgs) >= result + 1:
                    argumentTable[arg] = self.rawArgs[result + 1]
                else:
                    print("[Debug] if() statement fail, arg:'{}', result: {}".format(arg, result))

            except ValueError:
                # This argument was not present!
                print("[Debug] ValueError on arg: '{}'".format(arg))
                if arg in self.necessaryArgs:
                    print("Necessary Arguments:", self.necessaryArgs)
                    raise Exception("PARSE: Necessary argument -{} not found!".format(arg))

        return argumentTable

    ''' Auxiliary methods '''
    def splitter(self, args):
        # todo: make a splitter that considers `"`
        if type(args) == type(list()):
            return args
        else:
            return args.split(' ')[1:] # without the program name

#  p = Parser('./killswitch -cill 39 -d 99', acceptedArgs = ['cill', 'd', 'f'], necessaryArgs = ['f'])
#  p.parseArgs()
