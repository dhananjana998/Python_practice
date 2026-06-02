#input student names and marks
n=int(input("Enter number of student:"))
student=[]
for i in range(n):
      name=input("Enter student name:")
      marks=int(input("Enter student marks:"))
    
      student.append([name,marks])

#calculate average
total=0

for s in student:
      total+=s[1]

average=total/n

#find highest marks

highest=student[0][1]
top_student=student[0][0]

for s in student:
      if s[1]>highest:
        highest=s[1]
        top_student=s[0]

#rank list
for i in range(len(student)):
      for j in range(len(student)-i-1):
         if student[j][1]<student[j+1][1]:
           temp=student[j]
           student[j]=student[j+1]
           student[j+1]=temp

#Output
print("\n Average marks=",average)
print("\n highest marks=",highest,"by",top_student)
print("\n Rank List")
rank=1
for s in student:
      print(rank,"-",s[0],"-",s[1])
      rank+=1
      
      
           
