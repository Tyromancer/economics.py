p0 = float(input('The current price of the stock: '))
d = float(input('The dividend paid each year: '))
re = float(input('The required rate of return: '))
n = int(input('Number of years: '))

i = 1
while i <= n:
	temp = d / (1 + re) ** i
	p0 -= temp
	i += 1

p0 *= (1 + re) ** n
print('P{} is {}'.format(n, p0))
