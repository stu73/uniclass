import csv
import sys
import xml.etree.cElementTree as ET
import xml.dom.minidom

uniclass2_array = []

cmdargs = str(sys.argv)

with open(str(sys.argv[1]), 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
  count = 0
  for row in spamreader:
	uniclass2_array.append([]) 
	uniclass2_array[count] = row
	count += 1

count = 0

# For each line in array

# count size of code
# if code  



for row in uniclass2_array:
	# if it's an 11 - it's the last in the list, do a normal tag
	if len(uniclass2_array[count][0]) == 11:
		print "\t<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"
		# if the next in line is an 8, up one in tree - close the tag		
		if len(uniclass2_array[count+1][0]) == 8:
			print "</DataEntry>"
		if len(uniclass2_array[count+1][0]) == 5:
			print "</DataEntry>"
	# if it's an 8 - it may have children - check if next one is 11 - if so, dont close tag	
	elif len(uniclass2_array[count][0]) == 8:
		if len(uniclass2_array[count+1][0]) == 11:
			print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
		elif len(uniclass2_array[count+1][0]) == 8:
			print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"
	# if it's a 5 - it may have children - check if next one is 8 - if so, dont close tag	
	elif len(uniclass2_array[count][0]) == 5:
		if len(uniclass2_array[count+1][0]) == 8:
			print "\t<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
		elif len(uniclass2_array[count+1][0]) == 5:
			print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"
	count +=1


