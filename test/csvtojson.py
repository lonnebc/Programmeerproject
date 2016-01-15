import json
import csv

with open("dataemployment.csv","rU") as fp:
	reader = csv.reader(fp, delimiter=',')
	next(reader, None)

	data = {	
		"name": "Some college, no degree",
		"children": []	}
	for lines in reader:
                
		splitted = lines[0].split("     ")
##		s = splitted[1].split("* ")
		education = lines[-6]
		change = lines[-9]
##		##		
# ##
# 		if not education in data["children"]:
# 			data["children"].append(education)

		if education == "Some college, no degree":
			data["children"].append("{!name!: " + "!" + splitted[0] + "!" + ", " + "!size!: " + change + "}")

json_data = json.dumps(data, indent=4)
print json_data
