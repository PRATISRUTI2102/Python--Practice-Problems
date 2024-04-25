def simpleintrest(p,r,t):
    print('The principal amount is',p)
    print('The rate of intrest is',r)
    print('The time period is',t)
    
    si = (p*r*t)/100
    
    print("the simple intrest is ", si)
    
P = int(input(" Enter the principal amount: "))
R = int(input("Enter the rate of intrest: "))
T = int(input("Enter the time period: "))

simpleintrest(P,R,T)