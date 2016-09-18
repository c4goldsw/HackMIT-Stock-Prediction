import csv
import json
import sys

def main(csv_file, json_file):

	csvfile = open(csv_file, 'r')
	jsonfile = open(json_file, 'w+')

	fieldnames = ('Time', 'First', 'Last')
	reader = csv.DictReader( csvfile, fieldnames)

	jsonfile.write('[\n')
	for row in reader:
	    json.dump(row, jsonfile)
	    jsonfile.write('\n')
	jsonfile.write('\n]')

	csvfile.close()
	jsonfile.close()

if __name__ == '__main__':
	csv_file = sys.argv[1]
	json_file = '%s.json' % csv_file.split('.')[0]
	main(csv_file, json_file)