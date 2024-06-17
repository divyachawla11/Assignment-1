#Program that prints the first n numbers in a fibonacci sequence
num=int(input("Enter number: "))
if num==0 | num==1:
    print("0")
else:
    a=0
    b=1
    print(a)
    print(b)
    for i in range(3,num+1,1):
        c=a+b
        print(c)
        a=b
        b=c
