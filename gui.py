
def auto():
	"""
		FIRST SUB
	"""
	init = 0
	print(WAIT + 'TESTING ONE')
	init = init + 1
	print('\t' + WAIT + 'TESTING SUB A', end='')
	time.sleep(1)
	print('\r\t' + DONE)
	init = init + 1
	print('\t' + WAIT + 'TESTING SUB B', end='')
	time.sleep(1)
	print('\r\t' + DONE)
	init = init + 1
	print('\t' + WAIT + 'TESTING SUB C', end='')
	time.sleep(1)
	print('\r\t' + DONE)
	print('\033[' + str(init + 1) + 'A\r' + DONE + '\033[' + str(init) + 'B')
	"""
		SECOND SUB
	"""
	init = 0
	

auto()