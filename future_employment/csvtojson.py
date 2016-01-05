import json

with open("Employment-Projections.csv","rb") as lines:
	lines = lines.readlines()[1:119]
    

data = []

for line in lines:
	#splitted_title = line.split('           ')
	#title = splitted_title[0]
    splitted = line.split(',')
    wage = splitted[-7]
    #years8 = splitted[-1:-8].strip()
    data.append([wage]) 
json_data = json.dumps(data)
print json_data