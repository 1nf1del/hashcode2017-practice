import csv

def write(found, file):

	results = []
	for item in found:
		results.append([item['origin'][0]+item['r1'][0], item['origin'][1]+item['r1'][1], item['origin'][0]+item['r2'][0], item['origin'][1]+item['r2'][1]])

	results=[[len(results)]] + results

	export_file = 'out/' + file + '.out'

	with open(export_file, 'w') as fp :
		a = csv.writer(fp, delimiter=' ')
		a.writerows(results)