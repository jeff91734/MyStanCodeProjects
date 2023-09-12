"""
File: prime_checker.py
Name: Jeff Tsai
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	The Prime checker will ask input from user.
	It will answer whether it is prime number or not, and generate another input request.
	The program can only be terminated if user provide constant EXIT as input.
	The program concept is to check if there is any number in between n and 1 can make mod equal to zero
	"""
	print('Welcome to the prime checker!')
	n = int(input('n: '))
	while n != EXIT:
		n1 = n - 1
		while True:
			if n == 2:
				# Special case since n1 already equals to 1
				print(str(n) + ' is a prime number.')
				break
			elif n % n1 == 0:
				# n1 exists to make mod equal zero
				print(str(n) + ' is not a prime number.')
				break
			else:
				n1 = minus_one(n1, n)
				if n1 == 1:
					# Checker stop while n1 equals to 1
					# No n1 qualified, n is a prime number.
					print(str(n) + ' is a prime number.')
					break
		n = int(input('n: '))
	else:
		print('Have a good one!')
		# Program termination


def minus_one(n1,n):
	"""
	:param n1: int, the checking number to make mod equal to zero.
	:param n: int, the input number
	:return: int, the next checking number
	"""
	n1 = n1 - 1
	return n1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
