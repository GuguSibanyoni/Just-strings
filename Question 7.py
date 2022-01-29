# To find factorial using recursive function 

n = 5

def factorial_Recursion(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_Recursion(n-1)

print(factorial_Recursion(n))