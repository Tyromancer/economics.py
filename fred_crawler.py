# Usage:
# Find and download fred series data
# then find the specific data on yyyy-mm-dd

import requests  # used for downloading text files from FRED
import os        # used for removing temporary text files


# Usage : download series data in the form of text file and extract data on given date
# param:
#         series: the series number
#         year  : target year. Format: 4 digit YYYY
#         month : target month. Format: 2 digit MM
#         day   : target day.  Format:  2 digit DD
def fred_crawler(series, year, month, day):
	r = requests.get('https://fred.stlouisfed.org/data/' + series + '.txt')
	fname = series + 'txt'

	with open(fname, 'wb') as f:
		f.write(r.content)

	with open(fname, 'r', encoding='utf-8') as f:
		lines = f.readlines()

		data_file = dict()
		for line in lines:
			if not line[0].isdigit():
				continue
			else:
				temp = line.rstrip().split()
				data_file[temp[0]] = temp[1]

	if len(month) == 1:
		month = '0' + mm

	if len(day) == 1:
		day = '0' + day

	date = year + '-' + month + '-' + day
	# print('The result is: {}'.format(data_file[date]))
	print("{} {}: {}".format(series.upper(), date, data_file[date]))
	os.remove(fname)


if __name__ == "__main__":
	query = input('Please enter the series ID ==> ').upper()
	yyyy = input('Year == > ')
	mm = input('Month ==> ')
	dd = input('Day ==> ')

	fred_crawler(query, yyyy, mm, dd)
