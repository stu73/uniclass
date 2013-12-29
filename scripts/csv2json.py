import csv
import sys

# set up the Uniclass2 array

uniclass2_array = []

cmdargs = str(sys.argv)

# load in Uniclass2 array from command line

with open(str(sys.argv[1]), 'rb') as csvfile:
  spam = csv.reader(csvfile, delimiter=',', quotechar='\"')
  count = 0
  for row in spam:
	uniclass2_array.append([]) 
	uniclass2_array[count] = row
	count += 1

# Print opening json bracket
print "["
count = 0
for row in uniclass2_array:

	if (count < len(uniclass2_array)-1):		
		print "[\""+uniclass2_array[count][0]+"\",\""+uniclass2_array[count][1]+"\",\""+uniclass2_array[count][2]+"\"],"
	else:
		print "[\""+uniclass2_array[count][0]+"\",\""+uniclass2_array[count][1]+"\",\""+uniclass2_array[count][2]+"\"]"

	count +=1

# print closing json bracket

print "]"

