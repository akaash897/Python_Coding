#Find Factorial of a Number using iterative method

n = int(input("Enter the number: "))
fact = 1
while(n>0):
    fact = n * fact
    n=n-1
print(fact)    