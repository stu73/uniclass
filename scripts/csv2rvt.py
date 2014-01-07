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
print "Uniclass2.0\tUniclass2.0\t1\t-2000000"
count = 0
for row in uniclass2_array:

	if (count < len(uniclass2_array)):		
		
		len_var = len(uniclass2_array[count][0])		

		len_print = 0

		if(len_var == 2):
			len_print = 2
		elif(len_var == 5):
			len_print = 3
		elif(len_var == 8):
			len_print = 4
		elif(len_var == 11):
			len_print = 5
		elif(len_var == 14):
			len_print = 6
		if(uniclass2_array[count][1].find(',')==-1):
			print uniclass2_array[count][0]+"\t"+uniclass2_array[count][1]+"\t"+str(len_print)+"\t-2000000"
		else:
			print uniclass2_array[count][0]+"\t\""+uniclass2_array[count][1]+"\"\t"+str(len_print)+"\t-2000000"
	count +=1


