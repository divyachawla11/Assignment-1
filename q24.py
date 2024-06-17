#Program that acts as a simple calculator. The operators present: (+,-,*,/)
print("Press + for addition")
print("Press - for subtraction")
print("Press * for multiplication")
print("Press / for division")
choice=input("Enter your choice: ")
if choice=='+':
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    sum=num1+num2
    print("The result is:", sum)
elif choice=='-':
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    sub=num1-num2
    print("The result is:", sub)
elif choice=='*':
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    mul=num1*num2
    print("The result is:", mul)
elif choice=='/':
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    div=num1/num2
    print("The result is:", div)
else:
    print("Invalid choice!!!")