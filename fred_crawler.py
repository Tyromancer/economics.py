# Usage:
# Find and download fred series data
# then find the specific data on yyyy-mm-dd
import requests

series = input('Please enter the series ID ==> ').capitalize()
url = 'https://fred.stlouisfed.org/data/' + series + '.txt'

r = requests.get(url)
fname = series + '.txt'
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

yy = input('Year ==> ')
mm = input('Month ==> ')
if len(mm) == 1:
	mm = '0' + mm
dd = input('Day ==> ')
if len(dd) == 1:
	dd = '0' + dd
date = yy + '-' + mm + '-' + dd
print('The result is: {}'.format(data_file[date]))
