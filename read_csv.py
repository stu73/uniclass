import csv
import sys
cmdargs = str(sys.argv)
with open(str(sys.argv[1]), 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader: print ', '.join(row)