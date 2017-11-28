import time
import matplotlib.pyplot as plt


#this algorithm caches prime numbers as it calculates them
#will be compared to an algorithm that performs the same task without caching results
class getPrimes_mem:

	
	#initializes class by calculating first maxN primes
	def __init__(self, maxN):
		#can't overload the constructor (or other functions) in python
		if(maxN == None):
			maxN = 50 #default initial size of primes list

		self.primes = []
		self.primeHelper(maxN)

	#resizes primes list to the Nth prime
	def resizePrimes(self,maxN):
		self.primeHelper(maxN)

	#returns value of nth prime number (utilizing memoization)
	#records elapsed time
	def DPgetPrime(self,n):
		start = time.clock()
		if(n >= len(self.primes)):
			self.resizePrimes(n*2)

		end = time.clock()
		elapsed = end - start
		
		return (self.primes[n], elapsed)



	def primeHelper(self,n):
		#does not have to start at beginning
		#can begin calculating primes starting at end of existing primes list
		if(len(self.primes) == 0):
			self.primes.append(2)
			curr = 3
		else:
			curr = self.primes[len(self.primes) - 1] + 2

		while(len(self.primes) < n):
		
			checkPrime = True
		
			for x in self.primes:
				if(curr % x == 0 and checkPrime == True):
					checkPrime = False 
				

			if(checkPrime):
				self.primes.append(curr)

			#never need to check even numbers
			curr += 2

		return self.primes[len(self.primes) - 1]



#encapsulates the non-memoization form of primes function
#must put in different classes because __init__ function of other class runs a time-consuming computation
class getPrimes_reg:

	#constructor listed here in case it needs to be used for anything later
	def __init__(self):
		return

	#this is the normal implementation of finding primeNumbers
	#used to compare to an algorithm that caches prime numbers up to a certain value initially
	def getNthprime(self,n):
		start = time.clock()
		primeList = []
		primeList.append(2)

		curr = 3

		while(len(primeList) < n):
		
			checkPrime = True
		
			for x in primeList:
				if(curr % x == 0 and checkPrime == True):
					checkPrime = False 
				

			if(checkPrime):
				primeList.append(curr)

			#never need to check even numbers
			curr += 2

		end = time.clock()
		elapsed = end - start
		return (primeList[len(primeList) -1],elapsed)

if __name__ == '__main__':

	#how many primes are initially stored in primes list
	INITIAL_SIZE = 50

	raw_input("This program will test the time efficiency of two algorithms that calculated the first *n* prime numbers both normally and using memoization. Press anything to continue.")
	#this object is only created to record elapsed time of function without memoization
	prime_obj1 = getPrimes_reg() 

	#graphs the runtime of algorithm for different inputs to prove O(N^2) efficiency
	MAX_RAN = 0
	try:
		MAX_RAN = int(raw_input("How many primes would you like to calculate? [Enter an integer value]: "))
	except:
		MAX_RAN = 100

	normalX = []
	normalY = []


	memY = []

	for maxRange in range(2,MAX_RAN):
		elapsedTime = 0
		for i in range(1,maxRange):
			result = prime_obj1.getNthprime(i)
			elapsedTime += result[1]
		#append these results to see runtime of algorithm for different inputs
		#graph will display actual efficiency of algorithm
		normalY.append(elapsedTime)
		normalX.append(maxRange)

	#this object used for 
	prime_obj2 = getPrimes_mem(INITIAL_SIZE)

	for maxRange in range(2,MAX_RAN):
		elapsedTime = 0
		for i in range(1,maxRange):
			result = prime_obj2.DPgetPrime(i)
			elapsedTime += result[1]
		#append these results in same fashion as before but to separateLists
		#can be graphed against same x values
		memY.append(elapsedTime)


	#graphs results using pyplot
	plt.plot(normalX,normalY, color = "red", label = "Normal")
	plt.plot(normalX,memY, color = "blue", label = "Optimized")
	plt.xlabel("Number of primes Calculated")
	plt.ylabel("Runtime")
	plt.title("Efficiency of Different Primes Algorithms")
	plt.legend()
	plt.show()