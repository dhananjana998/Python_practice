#fibonacci sequence generator
n=int(input("Enter how many fibonacci numbers you want:"))
a,b=0,1
print("Fibonacci numbers:")

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b