import sys
from fred_crawler import fred_crawler
from money_supply import money_supply


argc = len(sys.argv)  # get number of argument given
if argc == 1 or ('-h' in sys.argv):  # if no arguments other than the filename is provided, display the help message
	print('''Usage: [func][-opt...]
func:
	fred_crawler: [series][YYYY][MM][DD]
		
	money_supply: [C][D][RRR][ER]
	'''
	)
	sys.exit(0)  # exit program

if sys.argv[1].lower().strip() == 'fred_crawler':  # use fred_crawler
	if argc != 6:  # check argument sanity
		print('Invalid number of arguments! Entered {}, required 6.'.format(argc))
		sys.exit(1)

	try:
		fred_crawler(sys.argv[2].upper(), sys.argv[3], sys.argv[4], sys.argv[5])
	except ...:
		print('Invalid arguments!')
		sys.exit(1)

elif sys.argv[1].lower().strip() == 'money_supply':
	if argc != 6:
		print('Invalid number of arguments! Entered {}, required 6.'.format(argc))
		sys.exit(1)

	try:
		money_supply(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
	except ...:
		print('Invalid arguments!')
		sys.exit(1)
