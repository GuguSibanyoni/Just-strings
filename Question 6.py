"""
Given a positive integer, N, print all the integers from 1 to N.
-For multiples of 3 print "Fizz" instead of the number 
-For multiples of 5 print "Buzz" 
-For numbers which are multiples of 3 and 5, print "FizzBuzz".

"""

N = 45

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
