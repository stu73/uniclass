import csv
import sys

uniclass2_array = []

cmdargs = str(sys.argv)

with open(str(sys.argv[1]), 'rb') as csvfile:
  spam = csv.reader(csvfile, delimiter=',', quotechar='\"')
  count = 0
  for row in spam:
	uniclass2_array.append([]) 
	uniclass2_array[count] = row
	count += 1

# rest counter
count = 0

print len(uniclass2_array)

for row in uniclass2_array:

	if len(uniclass2_array[count][0]) == 11:
		print "3-------<d>"+uniclass2_array[count][0]+"</d>"
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 8):
				print "2----</d>"

	elif len(uniclass2_array[count][0]) == 8:
		print "2----<d>"+uniclass2_array[count][0]
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 8):
				print "2----</d>"
			if(len(uniclass2_array[count+1][0]) == 5):
				print "2----</d>"

	elif len(uniclass2_array[count][0]) == 5:
		if count > 0:
			if(len(uniclass2_array[count-1][0]) == 11):
				print "2----</d>"
				print "1-</d>"
			if(len(uniclass2_array[count-1][0]) == 8):
				print "2----</d>"			
		print "1-<d>"+uniclass2_array[count][0]

	count +=1

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 11):
	print "3-------</d>"
	print "2----</d>"
	print "1-</d>"

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 8):
	print "2----</d>"
	print "1-</d>"

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 5):
	print "1-</d>"

