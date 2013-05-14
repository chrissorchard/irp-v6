#!/usr/bin/env python

import sqlite3



if(len(sys.argv) < 2):
    print("Not enough arguments!\n")
    return

rootdir = sys.argv[1]

for root, dirs, files in os.walk(rootdir):
    print files
