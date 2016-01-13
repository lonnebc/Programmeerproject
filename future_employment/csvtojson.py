#scraper voor slopegraph data 2014 en 2024
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
		change = lines[-9]
			
		#data.append([education] + [[splitted[0]] + [change]]) # + [s[1:]])

		# if not education in data["children"]:
		# 	data["children"].append(education)

		if education == "Doctoral or professional degree":
			data["children"].append(splitted[0])

json_data = json.dumps(data, indent=4)
print json_data	 
	# for lines2 in reader
	# 	for education in degree:
	# 		if degree == lines2[-6]

	#print degree

	# jobs = {}
	# for degree in data["children"]:
	# 	for lines in reader:
	# 		
	# 	jobs["name"] = sector
	# 	jobs.append(sector)
				# job = {}
				# job["name"] = education
				# data["children"]["name"] = job
		
