#swift_naviagtion_application_question.py

"""
In the programming language of your choice, write a program generating 
the first n Fibonacci numbers F(n), printing

	- "Buzz" when F(n) is divisible by 3.
	- "Fizz" when F(n) is divisible by 5.
	- "FizzBuzz" when F(n) is divisible by 15.
	- "BuzzFizz" when F(n) is prime.
	- the value F(n) otherwise.

We encourage you to compose your code for this question in a way that 
represents the quality of code you produce in the workplace - e.g. tests, 
documentation, linting, dependency management (though there's no need to go this far).

Please upload your code to GitHub or bitbucket and post a link to 
the repo or gist as your answer in the Lever form.
"""
import unittest
import math

# Set debug mode
debugMode = False

def isPrime(num):
	# Normal algorithm for checking prime

	cap = math.sqrt(num) #Only need to checkup to the square root of num

	for x in xrange(2, int(cap) + 1):
		# Return False if divisible 
		if num % x == 0: return False

	# Otherwise divisible
	return True


def F_helper(n, cur, fibList, debugString = None):
	if cur >= n: return debugString

	if debugMode and debugString == None: debugString = ""

	# Base case
	if cur == 0 or cur == 1: 
		if debugMode: debugString+= (str(1)+";")
		else: print(1)
		return F_helper(n, cur+1, fibList, debugString=debugString)

	# Else generate next number in sequence
	nextNum = fibList[-1] + fibList[-2]

	# Append to list 
	fibList.append(nextNum)

	# From directions, it seems we could potentially print more than one thing. (For example:
	# 15 is divisible by 3, 5, and 15 so Buzz, Fizz, and FizzBuzz would be printed on the same
	# line. And if no criteria are met the number is printed like 8)

	# Check at the end if we need to print the number instead
	printNumber = True

	# Add any words we need to the output
	output = ""

	#For debugging prepend output with nextNum

	# Divisible by 3
	if nextNum % 3 == 0:
		output+= "Buzz "
		printNumber = False

	# Divisible by 5
	if nextNum % 5 == 0:
		output+= "Fizz "
		printNumber = False

	# Divisible by 15
	if nextNum % 5 == 0:
		output+= "FizzBuzz "
		printNumber = False

	# prime
	if isPrime(nextNum):
		output+= "BuzzFizz "
		printNumber = False

	#Remove last space
	output = output[:-1] 

	if debugMode and printNumber: debugString+= (str(nextNum) + ";")
	elif debugMode: debugString+= (output + ";")

	# If no criteria met print number, else output for criteria
	else:
		if printNumber: print(nextNum)
		else: print(output)

	return F_helper(n, cur+1, fibList, debugString=debugString)

def F(n):
	# Pass in (length of sequence, the starting number, starting list with first 2 numbers)
	return F_helper(n, 0, [1,1])


		


def main():
	if debugMode:
		unittest.main()
	else:
		rt = F(9)

class MyTest(unittest.TestCase):
	# Generate no numbers
    def test0(self):
        self.assertEqual(F(0), None)

    # Base cases
    def test1(self):
    	self.assertEqual(F(1), "1;")

    def test2(self):
    	self.assertEqual(F(2), "1;1;")

    # Contains numbers for all criteria
    def test6(self):
    	self.assertEqual(F(6), "1;1;BuzzFizz;Buzz BuzzFizz;Fizz FizzBuzz BuzzFizz;8;")



if __name__ == '__main__':
	main()

