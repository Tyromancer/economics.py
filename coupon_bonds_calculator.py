c = float(input('Yearly coupon payment ==> '))
f = float(input('Face value of the bond ==> '))
i = float(input('Yield to maturity ==> '))
n = int(input('Years to maturity date ==> '))

price = 0

x = 0
while x < n:
	price += c / (1 + i) ** (x + 1)
	x += 1

price += f / (1 + i) ** n
print('The price of the coupon bond is ', price)
