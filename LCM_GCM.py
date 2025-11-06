import math

num1=int(input("enter number one:"))
num2=int(input("enter number two:"))

gcd=math.gcd(num1,num2)
lcm=(num1*num2)//gcd

print(f"GCD of {num1} and {num2} is:{gcd}")
print(f"LCM of {num1} and {num2} is:{lcm}")

""" output:

enter number one:50
enter number two:100
GCD of 50 and 100 is:50
LCM of 50 and 100 is:100




"""