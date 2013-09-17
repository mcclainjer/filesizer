#!/usr/bin/python

import os
import sys
import datetime
import math

#Simple utility to get the size of a file in bytes and output in KB to stdout.

now = datetime.datetime.now()#timestamp
filepath = sys.argv[1]#get file path from argument
filesize = os.path.getsize(filepath)#get the size of the file in bytes
c_filesize = filesize/1024#convert to kb
try:
    sys.stdout.write('{0} File {1} is bytes={2} kb={3}'.format(now, filepath, filesize, c_filesize))
except:
    sys.stdout.write('filesizer.py has encountered an exception')#throw arbitrary exception
