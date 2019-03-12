from array import *
arr = array('i',[])
n = int(input("Enter the arrays length: "))
for i in range(n):
    x = int(input("Enter the numbers iin array: "))
    arr.append(x)
print(arr)

val = int(input("Enter the value for searching: "))

k=0
for e in arr:
    if val == e:
        print(k)
        print(arr.index(val))
        break
    k = k + 1
else:
     print(val," is not in array")

