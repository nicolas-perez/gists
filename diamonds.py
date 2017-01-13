def diamond(char, size):
	for row in range(1, size*2+1, 2):
		if row <= int(size):
			print(" "*int((size-row)/2) + char*row + " "*int((size-row)/2))
		else:
			print(" "*int((row-size)/2) + char*(size*2-row) + " "*int((row-size)/2))

diamond('*', 19)
diamond('$', 19)
diamond('+', 19)