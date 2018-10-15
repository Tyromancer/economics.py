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

yr1 = int(input('Begin year ==> '))
yr2 = int(input('End year ==> '))

result = 0
i = yr1 + 1
prev = float(data_file[str(yr1) + '-01-01'])
while i < yr2:
	temp_yr = str(i) + '-01-01'
	temp = float(data_file[temp_yr])
	result += (temp - prev) / prev
	prev = temp
	i += 1

result /= (yr2 - yr1)
result *= 100
print('The average value is {:.2f}%'.format(result))
