#scraper 
import json
import csv

with open("dataemployment.csv","rU") as fp:
	reader = csv.reader(fp, delimiter=',')
	next(reader, None)

	data = {	
		"name": "education",
		"children": []
	}

	for lines in reader:
		
		splitted = lines[0].split("     ")
		#s = splitted[1].split("* ")
		education = lines[-6]
		#change = lines[-9]

# 		if education == "Doctoral or professional degree":
# 			data["children"].append(splitted[0])

# json_data = json.dumps(data, indent=4)
# print json_data