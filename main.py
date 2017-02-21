
from pizza_modules import parse_input, pizza_combination, pizza_slice, slice_output

files = [
	{'name':"small", 'chunk': 0},
	{'name':"example", 'chunk': 0},
	{'name':"medium", 'chunk': 25},
	{'name':"big", 'chunk': 25},
]
for f in files:
	pizza, rows, cols, min, max = parse_input.read(f['name'])
	slices = pizza_combination.generate(min, max)
	pizza_slice.min, pizza_slice.max, pizza_slice.slices = min, max, slices

	if f['chunk'] == 0 :
		found = pizza_slice.slice(pizza, (0,0), rows, cols, 0)
	else :
		chunk=f['chunk']
		found = []
		for i in range(0, rows, chunk):
			for j in range(0, cols, chunk):
				#print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CHUNK", i, j
				print pizza[i:i+chunk,j:j+chunk], (i,j), chunk, chunk, 0
				found += pizza_slice.slice(pizza[i:i+chunk,j:j+chunk], (i,j), chunk, chunk, 0)
	
	score = 0
	for item in found:		
		score += item['score']

	print "!!!!!!!!!!! TOTAL SCORE IS ", score

	slice_output.write(found, f['name'])