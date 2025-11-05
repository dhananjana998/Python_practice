# Prime Number Generator - corrected

n = int(input("Enter the number: "))
print(f"\nPrime numbers between 1 and {n} are:")

if n < 2:
    print("None")
else:
    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end="  ")
print()
