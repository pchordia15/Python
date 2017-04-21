# Use for, split(), and if to create a Statement that will print out words that start with 's':
st = 'print only the words that start with s in this sentence'
for letter in st.split():
  if letter[0] == 's':
    print(letter)
 
# Use range() to print all the even numbers from 0 to 10.   
for i in range(11):
  if i%2 == 0:
    print(i)
    
print(range(0,11,2))

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
l = [div for div in range(1,51) if div%3 == 0]
print(l)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for letter in st.split():
  if len(letter) %2 == 0:
    print(letter)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
  if i%3 == 0 and i%5 == 0:
    print('FizzBuzz')
  elif i%5 == 0:
    print('Buzz')
  elif i%3 == 0:
    print('Fizz')
  else:
    print(i)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
l = [letter[0] for letter in st.split()]
print(l)