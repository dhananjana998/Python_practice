def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 


numbers = [3, 8, 15, 23, 42, 56, 78, 91]
target = 42

result = binary_search(numbers, target)

if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")


"""output:
Number found at index 4
"""