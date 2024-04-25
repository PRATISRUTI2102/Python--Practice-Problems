import random

n = random.random()

print("generating random number from 0 to 1 :- ", n)

m = random.randint(12,67)
print("generating random number from 12 to 67 :- ",m) 

#creating a list:-
rand_list = []
for i in range(0,10):
    
    L = random.randint(10,78)
    rand_list.append(L)
    
print("List or random numbers from 10 to 78 :- ",rand_list)