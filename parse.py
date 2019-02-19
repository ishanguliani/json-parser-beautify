"""
filename: parse.py
author: ishanguliani
website: github.com/ishanguliani/json-parser-beautify
description:

view a cleaner version of your json file. Helpful for viewing a part of a huge dataset
before importing it into your DATABASE
"""

import json
import sys

def main():
    count = 0
    try:
            filename = str(sys.argv[1])
            with open(filename) as f:
                print(json.dumps(json.loads(f.readline().strip()), indent=2))
                count += 1
                response = str(input('The first line is printed, do you want to see the whole file ?')).lower()
                if response.__contains__('n'):
                    sys.exit(0)
                for line in f.readlines():
                    count += 1
                    print(json.dumps(json.loads(line.strip()), indent=2))
                print(count, 'json objects printed')

    except:
            print("your json file could not be loaded. Please make sure this script is in the same working directory as your json file.")

if __name__ == '__main__':
        main()