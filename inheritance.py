class Fruit(object):

	def __init__(self):
		print("In Fruit class")

	def nutrition(self):
		print("Fruit class nutrition")

	def fruit_shape(self):
		print("Any shape")

class Apple(Fruit):

	def __init__(self):
		Fruit.__init__(self)
		print("In Apple class")

	def nutrition(self):
		print("Apple class nutrition")

	def color(self):
		print("Red")


f = Fruit()
f.nutrition()
f.fruit_shape()

print("*"*20)

a = Apple()
a.nutrition()
a.color()
a.fruit_shape()