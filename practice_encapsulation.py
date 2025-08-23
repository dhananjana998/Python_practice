

class NCOE:
    def student(self):
        print("127 First Year Batch\n")
        self.__first_Year_Student()
        self.__subjects()
        self.__Registration()

    def __first_Year_Student(self):
        print("first year girls :106\n")
        print("first year boys :21\n")

    def __subjects(self):
        print(" subject \n 251 \n 252 \n 253 \n 256 \n 257")

    def __Registration(self):
        R_No = []
        i = 1
        while i <= 5:
            R_Num = int(input("Enter Registration No: "))
            R_No.append(R_Num)
            i += 1
        print("All Registration Numbers:", R_No)

myObj = NCOE()
myObj.student()

""" OUTPUT:

127 First Year Batch

first year girls :106

first year boys :21

 subject 
 251 
 252 
 253 
 256 
 257
Enter Registration No: 1
Enter Registration No: 2
Enter Registration No: 3
Enter Registration No: 4
Enter Registration No: 5
All Registration Numbers: [1, 2, 3, 4, 5]


"""
