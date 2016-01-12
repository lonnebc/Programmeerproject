# scraper1 voor alles

# import json
# import csv

# with open("dataemployment.csv","rU") as fp:
# 	reader = csv.reader(fp, delimiter=',')
# 	next(reader, None)

# 	data = []
# 	for lines in reader:
# 		splitted = lines[0].split("     ")
# 		s = splitted[1].split("* ")
# 		data.append([splitted[0]] + [s[1:]] + lines[-13:-1])

# json_data = json.dumps(data, indent=4)
# print json_data

#scraper 2 voor slopegraph data 2014 en 2024
import json
import csv

with open("dataemployment.csv","rU") as fp:
	reader = csv.reader(fp, delimiter=',')
	next(reader, None)

	data = {	
		"name": "education",
		"children": [
			
			data2 = {
				"name": []
			}
		]
	}
	#degree = []	

	for lines in reader:
		splitted = lines[0].split("     ")
		s = splitted[1].split("* ")
		education = lines[-6]
		change = lines[-9]
		
		#data.append([education] + [[splitted[0]] + [change]]) # + [s[1:]])

		if not education in data["children"]:
			data["children"].append(education)

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
		
json_data = json.dumps(data, indent=4)
print json_data




#try
# 	data = []
# 	for lines in reader:

# 		splitted = lines[0].split("     ")
# 		# year14 = lines[-12]
# 		jobs = lines[-11]
# 		#education = lines[-6]
# 		job = {}
# 		job["name"] = "jobs"
# 		job["children"] = jobs
# 		data.append([[splitted[0]] + [jobs[1:]]]) 

# json_data = json.dumps(data, indent=4)
# print json_data
#endtry


#sjoerd
	# sectors = []
	# for row in reader:
	#         sectors.append(row)
	# 	sectors = sectors[1:]
	# 	data_dict = {}
	# 	educationlist = sectors[-6]
	# 	print educationlist
	# 	#counter = 0
	# 	for degree in educationlist:
	# 		degreedict = {}
	# 		for entry in sector:
	# 			sector = entry[-3]
	# 			change = entry[-9]
	# 			degreedict[sector] = change
	# 		data_dict[degree] = degreedict
		#counter += 1
#eindesjoerd








	# var = 0 
	# if 'bla' in ['bla', 'bla1']:
	# 	var = 1
	# print var




		# splitted = lines.split(",")
	 # # 	#titlecode
	 # # 	title = splitted[0]
	 # # 	title1 = title[1:]
		# # titles.append(title1)

		# #employmentcode 2014
		# employment = splitted[-13:-1]
		# employment1 = employment
		# employment14.append(employment1)

	#print titles

	#print type(lines[0])
	# data = []
	# reader = csv.reader(fp, delimiter=',')
	# print reader
	# for row in reader:
	# 	data.append(row)
	# print data
# data = []
	# splitted = line.split(",")
	# title = splitted[1]
	#splitted = line.split(',')
	#wage = splitted[-7]
    #years8 = splitted[-1:-8].strip()
# 	data.append([title]) 


