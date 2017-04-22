def prime(number):
  for n in range(2,number):
    if number%n == 0:
      print('Not Prime')
      break
  else:
    print('Prime')
      
prime(15)