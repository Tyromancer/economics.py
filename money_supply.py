

def money_supply(c, d, rrr, er):
	nominator = float((c / d) + 1)
	denominator = float((c / d) + rrr + (er / d))
	multiplier = float(nominator / denominator)

	mb = float(c + d * rrr + er)
	result = mb * multiplier
	print('The money supply is {}.'.format(result))
	print('The money multiplier is {}.'.format(multiplier))


if __name__ == '__main__':
	C = float(input("Please enter the value of currency in circulation ==> "))
	D = float(input("Please enter the value of checkable deposits ==> "))
	RRR = float(input("Please enter the required reserve rate ==> "))
	ER = float(input("Please enter the value of excess reserves ==> "))

	money_supply(C, D, RRR, ER)
