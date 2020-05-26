#program  to find geometric sequence

import math

def term(a,r):
	for i in range(11):
		print(a*int((math.pow(r,i))))

def main():
	a = int(input("Enter a: "))
	r = int(input("Enter r: "))
	print("First 10 numbers form geometric series are:")
	term(a,r)

if __name__ == "__main__":
	main() 
