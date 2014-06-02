#!/usr/bin/python

import re
import sys
from elements_dict import *

def print_red(message):
    return "\x1b[31;01m" + message + "\x1b[0m"

for word in sys.argv[1:]:
    print "Results for '" + word + "':"
    for key in e.keys():
        if re.search(key.lower(), word.lower()):
            result = re.search(key.lower(), word.lower())
            int_start = len(word[:result.start()]) + len(key)
            print word[:result.start()] + print_red(key) + \
                  word[int_start:] + "  (" + e[key][1] + ")"

