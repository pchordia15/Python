#Write a function that computes the volume of a sphere given its radius.

def volume(radius):
  return ((4.0/3)*3.14*(radius**3))
  
print(volume(1))

#Write a function that checks whether a number is in a given range (Inclusive of high and low)

#Using print statement
def ran_check(num,low,high):
  if num in range(low,high+1):
    print('In Range')
  else:
    print('Not in Range')
    
ran_check(5,1,5)

#Return bool
def ran_bool(num,low,high):
  return num in range(low,high+1)

print(ran_bool(6,1,5))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
def up_low(s):
  up = 0
  low = 0
  for st in s:
    if st.isupper():
      up += 1
    elif st.islower():
      low += 1
  print("Number of uppercase characters are: " + str(up))
  print("Number of lowercase characters are: " + str(low)) 
  
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(l):
  new_list = []
  for i in l:
    if i not in new_list:
      new_list.append(i)
  return new_list
      
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):
  x = 1
  for i in numbers:
    x = x*i
  return x
  
print(multiply([1, 2, 3, -4]))

#Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
  s = s.replace(' ','')
  return s == s[::-1]
  
print(palindrome('nurses run'))

# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
  alphaset = set(alphabet)
  return alphaset <= set(str1.lower())
  
print(ispangram("The quick brown fox jumps over the lazy dog"))