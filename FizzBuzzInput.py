import sys 

#Check for command line arguments. If none request argument via user input

if len(sys.argv) > 1:
	n = (sys.argv[1])
else:
	n = None 

while True:
	try:
		n = int(n)
		break
	except TypeError:
		print "Incorrect Input. Please enter a whole number"
		n = (raw_input("What number would you like to play to? "))
	except ValueError:
		print "Incorrect Input. Please enter a whole number"
		n = (raw_input("What number would you like to play to? "))
	

y = 0

#FizzBuzz
print "Fizz buzz counting up to {}".format(n)

while y <= n:
	if y % 3 == 0 and y % 5 == 0:
		print"FizzBuzz"
	elif y % 3 == 0 and y % 5 != 0:
		print "Fizz"
	elif y % 3 != 0 and y % 5 == 0:
		print "Buzz"
	else:
		print "{}".format(y)

	y += 1
