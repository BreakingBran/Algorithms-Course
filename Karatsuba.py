
counter = 0

def kmult(x,y):

	global counter
	counter += 1
	#print("counter is at: ",counter)
	#print("variables: {x : %d}, {y : %d} " % (x,y))

	n = int(len(str(x)))

	if (0 <= x < 10) or (0 <= y < 10):
		return (x*y)

	else:

		strx = str(x)
		stry = str(y)

		#print(len(strx)/2)
		#print(int(len(strx)/2))

		lenstrxhalf = int(len(strx)/2)
		lenstryhalf = int(len(stry)/2)

		#print(strx[0:lenstrxhalf])

		'''
		There is a way to optomize it where you only make three recursive calls
		by simplyfing the kmult(a,d) + kmult(b,c) into [ kmult ( (a,b) + (c,d)) - kmult(a,c) - kmult(b,d)
		as kmult(a,c) and kmult(b,d) had already been computed
		
		'''

		a = int(strx[0:lenstrxhalf])
		b = int(strx[lenstrxhalf:])
		c = int(stry[0:lenstryhalf])
		d = int(stry[lenstryhalf:])

		return ( 10**n*(kmult(a,c)) + 10**(n/2)*(kmult(a,d) + kmult(b,c)) + kmult(b,d))

def main():

	value = None

	while (value != "exit"):

		int1 = int(input("What is your x: "))
		int2 = int(input("What is your y: "))

		print(kmult(int1,int2))

		value = input("Do you want to continue or exit: (continue/exit): ")

main()


