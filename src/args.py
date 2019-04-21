# Args library
import re
import os.path

if __name__ == "__main__":
    print("This cannot be run as a script!")
    exit()

def parseArgs(args):
    '''
    Function to parse arguments correcly, will return a Dictionary with:
        - filepath -> String
        - filename -> String
        - output_dir -> String * OPTIONAL
        - parse_fail -> Boolean
    '''
    parsed = dict()

    if len(args) >= 2:
        # Should be the correct number of args
        parsed['filepath'] = args[1]

        # Extracting the filename out of filepath
        parsed['filename'] = parsed['filepath'].split('/')[-1]
        parsed['parse_fail'] = False

        if len(args) == 3:
            parsed['output_dir'] = args[2]

            # Add the /
            if( parsed['output_dir'][-1] != '/' ):
                parsed['output_dir'] += '/'

            # check if exists
            if os.path.isdir(parsed['output_dir']) is not True:
                raise Exception("Invalid directory specified for the output log.")
        else:
            parsed['output_dir'] = './'


    else:
        print("ERROR: PARSE: Incorrect number of Args!")
        print("Run:\t./wcalc.py [input_file] [output_dir]")
        parsed['parse_fail'] = True

    return parsed
