#!/usr/bin/python

# Import relevant modules
import sys
import csv

# Load the data
reader = csv.reader(sys.stdin)

# Skip the header
reader.next()

# For every line in the data...
for line in reader:

    # ...that has 19 fields...
    #print len(line) 
    if len(line) == 18:
        video= line[0]
        category=line[5]
        country=line[17]
        print '{0}\t{1}\t{2}'.format(category,video,country)
