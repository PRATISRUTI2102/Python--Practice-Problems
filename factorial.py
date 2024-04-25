def factorial(n):
    return 1 if (n==0 or n==1) else n* factorial(n-1)

num = int(input("enter number: "))
print(" the factorial of",num,"is",factorial(num))