import json
import csv

with open("dataemployment.csv","rU") as fp:
	reader = csv.reader(fp, delimiter=',')
	next(reader, None)

	data = {	
		"name": "education",
		"children": []	}
	for lines in reader:
                
		splitted = lines[0].split("     ")
##		s = splitted[1].split("* ")
		education = lines[-6]
##		change = lines[-9]
##		
##		
##
##		#if not education in data["children"]:
##		#	data["children"].append(education)

json_data = json.dumps(data, indent=4)
print json_data
