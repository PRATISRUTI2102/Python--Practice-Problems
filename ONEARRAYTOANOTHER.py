arr1 = [3,5,6,7,8]

arr2 = [None] * len(arr1)

for i in range(0, len(arr1)):
    arr2[i] = arr1[i]

print(" Elements of original array")
for i in range(0, len(arr1)):
     print(arr1[i]),
print();

print("Elements in new array:-")
for i in range(0, len(arr2)):
     print(arr2[i]),