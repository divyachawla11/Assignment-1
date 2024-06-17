#Program that copies contents of one text file to another
file1=open('C:/Users/Sanjeev Chawla/Desktop/Python ML internship/Assignments/Assignment 1/q25 text file 1.txt','r')
file1_text=file1.readlines()
file2=open('C:/Users/Sanjeev Chawla/Desktop/Python ML internship/Assignments/Assignment 1/q25 text file 2.txt','w')
print(file1_text,file=file2)

