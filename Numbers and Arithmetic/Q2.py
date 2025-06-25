#Generate Fibonacci Series up to N Terms

n = int(input("Enter the number of terms in the series: "))
a, b = 0, 1  # F(0), F(1)

for i in range(n):
    print(a)
    a, b = b, a + b  # Update F(n-1) and F(n)
        

