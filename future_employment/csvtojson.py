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

	data = []
	for lines in reader:
		splitted = lines[0].split("     ")
		#year14 = lines[-12]
		year24 = lines[-11]
		data.append([[splitted[0]] + [year24[1:]]]) #+ [year24[1:]])

json_data = json.dumps(data)
print json_data

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


