import csv
import sys
import datetime

# functions and definitions used in main prog

def xml_data_outro(current_section_code,now_day,now_month,now_year):

	xml_data_outro_string = "</DataEntries></Data><Script><CreateClassificationReference><IfcRelAssociatesClassification Name=\"Uniclass2 - "+current_section_code+"\"><IfcClassificationReference Name=\"$title\" ItemReference=\"$number\" Location=\"www.cpic.org.uk\"><IfcClassification Source=\"www.cpic.org.uk\" Name=\"Uniclass2\" Edition=\""+current_section_code+"\"><IfcCalendarDate DayComponent=\""+now_day+"\" MonthComponent=\""+now_month+"\" YearComponent=\""+now_year+"\"/> <!-- EditionDate --></IfcClassification></IfcClassificationReference></IfcRelAssociatesClassification></CreateClassificationReference></Script>"
	return xml_data_outro_string

def xml_name_header( current_section_code ):
	xml_name_string = "<Name>"+current_section_code+"</Name>"
	return str(xml_name_string)

xml_description = "<Description>Classifies construction works and spaces according to user activity or intended purpose based on Uniclass2 specifications.'Apply' creates a Classification Reference for selected IFC entity, using Uniclass2-required attributes derived from the item that you choose in the following list.</Description>"

xml_applicable_to = "<ApplicableTo><ClassName>IfcProject</ClassName><ClassName>IfcSpatialStructureElement</ClassName><ClassName>IfcGroup</ClassName><ClassName>IfcActor</ClassName><ClassName>IfcControl</ClassName><ClassName>IfcSpaceType</ClassName></ApplicableTo>"

xml_data_intro = "<Data><DataDescriptors><DataDescriptor Variable=\"number\" Title=\"Code\" /><DataDescriptor Variable=\"title\" Title=\"Description\" /></DataDescriptors><DataEntries>"

# Read in file from command line to uniclass2_array

cmdargs = str(sys.argv)
uniclass2_array = []

with open(str(sys.argv[1]), 'rb') as csvfile:
  spam = csv.reader(csvfile, delimiter=',', quotechar='\"')
  count = 0
  for row in spam:
	uniclass2_array.append([]) 
	uniclass2_array[count] = row
	count += 1

# get current time - use for inserting into xml in main file

now_day = datetime.date.today().strftime("%d")
now_month = datetime.date.today().strftime("%m")
now_year = datetime.date.today().strftime("%y")

# set counter - used as flag when going through each line of the file
count = 0

# set two letter code for each section - used to check against when inserting xml headers per section

current_section = uniclass2_array[0][0]
current_section_code = current_section[0:2]

# print xml_header
print "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
print "<Rules Name=\"Uniclass2\">"
print "<Rule>"
print xml_name_header(current_section_code)
print xml_description
print xml_applicable_to
print xml_data_intro

# for each row in the uniclass csv file, check its relation to the rest of the file
# and where it is in heirarchy

for row in uniclass2_array:

	current_section = uniclass2_array[count][0]
	new_section_code = current_section[0:2]


	# check if we're onto a new section of codes - if so, insert xml ending code and start new header

	if current_section_code != new_section_code:
		print xml_data_outro(current_section_code,now_day,now_month,now_year)
		print "</Rule>"
		print "<Rule>"	
		current_section_code = new_section_code
		print xml_name_header(current_section_code)
		print xml_description
		print xml_applicable_to
		print xml_data_intro
 
	
	# for each code line, check it against the relative codes above and below to work out what xml tags are needed
	
	# if uniclass code is 11 long and next one isn't 14 print line with included closing tag	
	# if next uniclass code is 8 long print closing tag

	if len(uniclass2_array[count][0]) == 11:
		
		# make sure you're not on the last line of code		
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 14):
				print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
			else:
				print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\"/>"
			# if next uniclass code is 8 long close tag
			if(len(uniclass2_array[count+1][0]) == 8):
				print "</DataEntry>"

	# if uniclass code is 14 long print with included closing tag - longest possible	
	# if next code is 11 long print closing tag
	# if next code is 8 long print 2 closing tags
	# if next code is 5 long print 3 closing tags
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
	

	# if code is 8 long print it
	# if next code is 8, close tag
	# if next code is 5, close tag

	elif len(uniclass2_array[count][0]) == 8:
		print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"
		if (count < len(uniclass2_array)-1):		
			if(len(uniclass2_array[count+1][0]) == 5):

				# check if this is a special case where we go on to next code section
				end_letter_check = uniclass2_array[count][0]
				end_check_letter = end_letter_check[0:2]
				next_letter_check = uniclass2_array[count+1][0]
				next_check_letter = next_letter_check[0:2]

				if next_check_letter != end_check_letter:
					print "</DataEntry>"
					print "</DataEntry>"
				else:					
					print "</DataEntry>"

			if(len(uniclass2_array[count+1][0]) == 8):
				print "</DataEntry>"


	
	# if uniclass code is 5 long print it
	# if previous code is 8, close tag
	# if previous code is 11, close tag twice
	# if next code code is 5 close tag 	
	elif len(uniclass2_array[count][0]) == 5:
		# check if it's not the first code		
		if count > 0:
			# check previous codes to see how many closing xml tags to use			
			if(len(uniclass2_array[count-1][0]) == 11):
				print "</DataEntry>"
				print "</DataEntry>"
			if(len(uniclass2_array[count-1][0]) == 8):
					
				# check if this is a special case where we go on to next code section
				end_letter_check = uniclass2_array[count][0]
				end_check_letter = end_letter_check[0:2]		
				first_letter_check = uniclass2_array[count-1][0]
				first_check_letter = first_letter_check[0:2]
	
				if first_check_letter == end_check_letter:
					print "</DataEntry>"

		print "<DataEntry number=\""+uniclass2_array[count][0]+"\" title=\""+uniclass2_array[count][1]+"\">"

		if (count < len(uniclass2_array)-1):		

			if(len(uniclass2_array[count+1][0]) == 5):
				print "</DataEntry>"

				# check if this is a special case where we go on to next code section

				end_letter_check = uniclass2_array[count][0]
				end_check_letter = end_letter_check[0:2]
				next_letter_check = uniclass2_array[count+1][0]
				next_check_letter = next_letter_check[0:2]
				first_letter_check = uniclass2_array[count-1][0]
				first_check_letter = first_letter_check[0:2]


				if next_check_letter != end_check_letter:
					if next_check_letter == first_check_letter:				
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

print xml_data_outro(current_section_code,now_day,now_month,now_year)
print "</Rule>"
print "</Rules>"

