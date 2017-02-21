"""

Generate all possible slice shapes from max to min

"""

from math import sqrt

def generate(min, max):
	if min < 1 or max < 1:
		raise ValueError('min : {min} & max :{max} must be > 0'.format(min, max))
	slices = []
	for count in range(min, max+1)[::-1]:
		slice = {}
		slice["count"] = count

		# Calc all divisors
		dividers = []
		for divider in range(1, int(sqrt(count))+1):
			if count % divider == 0 :
				dividers.append(divider)
				# don't include square root twice
				if divider**2 != count:
					dividers.append(count/divider)

		dividers.sort(reverse=True)

		shapes = []
		while len(dividers) > 0:
			n = m = dividers.pop()
			if len(dividers) != 0:
				m = dividers.pop(0)
			shapes.append({'n': n, 'm': m})
			if n != m :
				shapes.append({'n': m, 'm': n})
		
		slice["shapes"] = shapes

		slices.append(slice)

	return slices

