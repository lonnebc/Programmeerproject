import json
import csv

with open("datacsv.csv","rb") as fp:
	#lines = fp.readlines()[1:119]
	#lines = fp.readlines()
	#print type(lines[0])
	#print lines[0]
	reader = csv.reader(fp,',')
	print reader
# data = []
# for line in lines:
# 	print line[0]
# 	# new_line = line.replace("          ",",")
	# #print line.split()
	# splitted = line.split(",")
	# title = splitted[1]
	#splitted = line.split(',')
	#wage = splitted[-7]
    #years8 = splitted[-1:-8].strip()
# 	data.append([title]) 
# json_data = json.dumps(data)
# print json_data