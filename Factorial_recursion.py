n = int(input("Enter a number: "))
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
result = fact(n)
print("factorial : ",result)