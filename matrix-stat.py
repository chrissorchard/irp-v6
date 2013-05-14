#!/usr/bin/env python

import sqlite3
import sys
import os

dbpaths = []

if(len(sys.argv) < 3):
    print("Not enough arguments!\n")
    exit(0)

dbfile = sys.argv[2] + ".db"
rootdir = sys.argv[1]

for root, dirs, files in os.walk(rootdir):
    if(dbfile in files):
        dbpaths.append(os.path.join(root, dbfile))

dbpaths.sort()

print dbpaths

for db in dbpaths:
    con = sqlite3.connect(db)
    c = con.cursor()

    
    c.execute("select count(domain) from WWW_{0} where ipv6 != \"n/a\"".format(sys.argv[2]))
    count = c.fetchone()[0]

    c.execute("select count(domain) from WWW_{0}".format(sys.argv[2]))
    total = c.fetchone()[0]

    print (float(count) / float(total))
