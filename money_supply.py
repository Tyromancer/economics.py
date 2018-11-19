C = float(input("Please enter the value of currency in circulation ==> "))
D = float(input("Please enter the value of checkable deposits ==> "))
RRR = float(input("Please enter the required reserve rate ==> "))
ER = float(input("Please enter the value of excess reserves ==> "))

nominator = float((C / D) + 1)
denominator = float((C / D) + RRR + (ER / D))
multiplier = float(nominator / denominator)

MB = float(C + D * RRR + ER)
result = MB * multiplier

print('The money supply is {}.'.format(result))
print('The money multiplier is {}.'.format(multiplier))
