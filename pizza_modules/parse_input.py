
from numpy import zeros


def read(filename):

	file = open("./in/"+filename+".in","r")
	conf = file.readline().replace("\n","").split(" ")
	rows, cols, min, max = int(conf[0]), int(conf[1]), int(conf[2]), int(conf[3])

	#print rows, cols, min, max

	pizza = zeros((rows, cols))
	for index in range(rows):
		line = file.readline()
		line = line.replace("\n","")
		line = line.replace("T", "1")
		line = line.replace("M", "0")
		pizza[index][:] = [char for char in line]

	#print pizza

	file.close()

	return pizza, rows, cols, min, max