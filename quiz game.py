#Multiple choice with score tracker

score=0
print("="*40+"Welcome to Quiz game "+"="*40 )

#quection 01

print("\n01.What does CPU stand for?")
print("\nA. Central Processing Unit")
print("B. Central Print Unit")
print("C. Control Processing Unit ")
print("D. Central Power Unit ")

answer= input("Enter your answer:").upper()
if answer=="A":
    print("correct!")
    score+=1
else:
    print("incorrect!")

# quection 02

print("\n02.What is the brain of the computer?")
print("\nA. Hard disk")
print("B. CPU")
print("C. RAM")
print("D. Mouse")

answer = input("Enter your answer:").upper()
if answer == "B":
    print("correct!")
    score += 1
else:
    print("incorrect!")
# quection 03

print("\n03.Which of the following is not an operating system?")
print("\nA. Windows")
print("B. Linux")
print("C. Google Chrome ")
print("D. macOS")

answer = input("Enter your answer:").upper()
if answer == "C":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("\nYour Full Score:",score)

"""OUTPUTS: 

========================================Welcome to Quiz game ========================================

01.What does CPU stand for?

A. Central Processing Unit
B. Central Print Unit
C. Control Processing Unit 
D. Central Power Unit 
Enter your answer:a
correct!

02.What is the brain of the computer?

A. Hard disk
B. CPU
C. RAM
D. Mouse
Enter your answer:b
correct!

03.Which of the following is not an operating system?

A. Windows
B. Linux
C. Google Chrome 
D. macOS
Enter your answer:c
correct!
Your Full Score: 3

Process finished with exit code 0
"""