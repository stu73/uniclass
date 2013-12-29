import csv
import sys

# basic vars

xml_header = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"

xml_main_header = "<Rule><Name>Co - Complexes</Name><Description>Classifies complexes (multi-entity construction projects) according to their function based on Uniclass2 specifications. 'Apply' creates a Classification Reference for selected IFC entity, using Uniclass2-required attributes derived from the item that you choose in the following list.</Description><ApplicableTo><ClassName>IfcProject</ClassName><ClassName>IfcSpatialStructureElement</ClassName><ClassName>IfcGroup</ClassName><ClassName>IfcActor</ClassName><ClassName>IfcControl</ClassName><ClassName>IfcSpaceType</ClassName></ApplicableTo><Data><DataDescriptors><DataDescriptor Variable=\"number\" Title=\"Code\" /><DataDescriptor Variable=\"title\" Title=\"Description\" /></DataDescriptors>"

xml_script_ending = "<Script><CreateClassificationReference><IfcRelAssociatesClassification Name=\"Uniclass2 - En - Entities\"><IfcClassificationReference Name=\"$title\" ItemReference=\"$number\" Location=\"www.cpic.org.uk\"><IfcClassification Source=\"www.cpic.org.uk\" Name=\"Uniclass2\" Edition=\"En - Entities\"><IfcCalendarDate DayComponent=\"15\" MonthComponent=\"01\" YearComponent=\"2013\"/> <!-- EditionDate --></IfcClassification></IfcClassificationReference></IfcRelAssociatesClassification></CreateClassificationReference></Script></Rule>"


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

# print len(uniclass2_array)

# get letter of first item - make that one to check against

letter_check = uniclass2_array[0][0]
first_letter = letter_check[0]

#print intro headers

print xml_header

print "<open>"

# print xml_main_header

for row in uniclass2_array:

	letter_check = uniclass2_array[count][0]
	check_letter = letter_check[0]

	if first_letter != check_letter:
		# put in new header and start again
		# print xml_script_ending
		# print xml_main_header
	
		first_letter = check_letter
 
	# if code is 11 long and next one isn't 14 print with included closing tag	
	# if next is 8 print closing tag

	if len(uniclass2_array[count][0]) == 11:
		
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 14):
				print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
			else:
				print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 8):
				print "</DataEntry>"

	# if code is 14 long print with included closing tag	
	# if next is 11 print closing tag
	# if next is 8 long print 2 closing tags
	# if next is 5 long print 3 closing tags
	if len(uniclass2_array[count][0]) == 14:
		
		print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"

		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 11):
				print "</DataEntry>"
			if(len(uniclass2_array[count+1][0]) == 8):
				print "</DataEntry>"
				print "</DataEntry>"
			if(len(uniclass2_array[count+1][0]) == 5):
				print "</DataEntry>"
				print "</DataEntry>"
				print "</DataEntry>"


	# if code is 8 long print
	# if next is 8, close tag
	# if next is 5, close tag
	elif len(uniclass2_array[count][0]) == 8:
		print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 5):
				print "</DataEntry>"
			if(len(uniclass2_array[count+1][0]) == 8):
				print "</DataEntry>"


	
	# if code is 5 long print
	# if previous is 8, close tag
	# if previous is 11, close tag twice
	# if next code is 5 close tag 	
	elif len(uniclass2_array[count][0]) == 5:
		if count > 0:
			if(len(uniclass2_array[count-1][0]) == 11):
				print "</DataEntry>"
				print "</DataEntry>"
			if(len(uniclass2_array[count-1][0]) == 8):
				print "</DataEntry>"	

		print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"

		if (count < len(uniclass2_array)-1):		

			if(len(uniclass2_array[count+1][0]) == 5):
				print "</DataEntry>"


	count +=1

#end tags

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 11):
	print "</DataEntry>"
	print "</DataEntry>"
	print "</DataEntry>"

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 8):
	print "</DataEntry>"
	print "</DataEntry>"

if(len(uniclass2_array[len(uniclass2_array)-1][0]) == 5):
	print "</DataEntry>"

print "</open>"

# print "</DataEntry>"
# print xml_script_ending

