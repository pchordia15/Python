#1
try:
	for i in ['a','b','c']:
		print(i**2)
except:
	print("TypeError Exception")

print("*"*20)

#2
x = 5
y = 0
try:
	z = x/y
except:
	print("DivideByZero Error")
finally:
	print("All Done")

print("*"*20)

#3
def ask():
	while True:
		try:
			num = int(raw_input("Input an Integer: "))
		except:
			print("An error occured! Please try again!")
		else:
			print("Thank you, number squared is: " + str(num ** 2))
			break
ask()

print("*"*20)

#4
def exceptionHandling():
	try:
		car = {'make':'bmw', 'model':'550i', 'year':2016}
		print(car['color'])
	except:
		print("Key not found")
	finally:
		print("In Finally Block")
exceptionHandling()