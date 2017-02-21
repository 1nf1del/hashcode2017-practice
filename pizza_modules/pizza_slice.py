
memory = {}


def find(pizza, position, rows, cols):
	global slices, min, max

	bestSlice = {
		'score': 0,
		'r1': (0,0),
		'r2': (0,0)
	}

	for slice in slices:
		for shape in slice['shapes']:
			# Next if shape outfit current pizza
			if shape['n'] > rows or shape['m'] > cols: 
				continue
			subpizza = pizza[0:shape['n'],0:shape['m']]
			tomatosCount = subpizza.sum()
			mushroomCount = slice['count'] - tomatosCount
			
			# Is is delicious ?
			if tomatosCount >= min and mushroomCount >= min :
				miam = {
					'score': slice['count'],
					'origin': position,
					'r1': (0,0),
					'r2': (shape['n']-1, shape['m']-1)
				}
				print ">>>>>> THIS SLICE IS DELICIOUS ", miam
				return miam

	print "NOTHING !!", position
	# No slice found
	return bestSlice


def slice(pizza, position, rows, cols, iteration):

	# Pizza is too small ?
	if(rows*cols < min*2):
		return []

	memKey = str(position[0])+','+str(position[1])+','+str(rows)+','+str(cols)

	if memKey in memory :
		print ":::::::::::: MEMORY HIT", position
		return memory[memKey]

	print "||||||||||||||| ITERATION ", iteration

	bestSlice = find(pizza, position, rows, cols)

	# What is the best cut to make ?
	bestSlices = []
	if bestSlice['score'] != 0 :
		bestSlices.append(bestSlice)

	favorRight = []
	favorDown = []


	# More to right ?
	if bestSlice['r2'][1]+1 < cols :
		subpizza = pizza[:, bestSlice['r2'][1]+1:]
		subposition = (position[0] + bestSlice['r1'][0], position[1] + bestSlice['r2'][1]+1)
		#print "RIGHT RIGHT", subpizza, subposition, len(subpizza), len(subpizza[0])
		favorRight += slice(subpizza, subposition, len(subpizza), len(subpizza[0]), iteration+1)
	
	if bestSlice['r2'][0]+1 < rows :
		subpizza = pizza[bestSlice['r2'][0]+1:,:bestSlice['r2'][1]+1]
		subposition = (position[0] + bestSlice['r2'][0]+1, position[1] + bestSlice['r1'][1])
		#print "RIGHT DOWN", subpizza, subposition, len(subpizza), len(subpizza[0])
		favorRight += slice(subpizza, subposition, len(subpizza), len(subpizza[0]), iteration+1)
	
	scoreRight = 0
	for item in favorRight:
		scoreRight += item['score']
	
	#print "BEST SLICE ", bestSlice
	# More to down ?
	if bestSlice['r2'][1]+1 < cols :
		subpizza = pizza[:bestSlice['r2'][0]+1, bestSlice['r2'][1]+1:]
		subposition = (position[0] + bestSlice['r1'][0], position[1] + bestSlice['r2'][1]+1)
		#print "DOWN RIGHT", subpizza, subposition, len(subpizza), len(subpizza[0])
		favorDown += slice(subpizza, subposition, len(subpizza), len(subpizza[0]), iteration+1)

	if bestSlice['r2'][0]+1 < rows :
		subpizza = pizza[bestSlice['r2'][0]+1:,:]
		subposition = (position[0] + bestSlice['r2'][0]+1, position[1] + bestSlice['r1'][1])
		#print "DOWN DOWN", subpizza, subposition, len(subpizza), len(subpizza[0])
		favorDown += slice(subpizza, subposition, len(subpizza), len(subpizza[0]), iteration+1)
	
	scoreDown = 0
	for item in favorDown:
		scoreDown += item['score']

	if scoreDown > scoreRight :
		bestSlices += favorDown
	else :
		bestSlices += favorRight

	memory[memKey] = bestSlices

	return bestSlices