def numbercheck(a):
    if a>0:
        print("The number is positive")
    elif a<0:
        print("The number is negative")
    else:
        print("The number given by user is a zero")
a = float(input("Envter a number:- "))
numbercheck(a)