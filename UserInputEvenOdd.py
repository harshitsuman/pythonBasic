from array import *
arr = array('i',[])
n = int(input("Enter the arrays length: "))
for i in range(n):
    x=int(input("Enter the numbers in the array: "))
    arr.append(x)
print(arr)

def count(arr):
    even = 0
    odd = 0
    for i in arr:
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    return even,odd

even, odd = count(arr)
print(even)
print(odd)

print("Even: {} and Odd: {}".format(even,odd))