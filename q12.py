#Program that calculates the sum of the digits of a given number
num=int(input("Enter the number: "))
sum=0
while num!=0:
    sum=sum+int(num%10)
    num=num/10
print("The sum of the digits is:",sum)