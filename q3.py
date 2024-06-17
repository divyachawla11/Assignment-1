#Program that calculates the factorial of a given number
import math
num=int(input("Enter th enumber you want the factorial for: "))
print("The factorial of",num,"is",math.factorial(num))
#Or there is another method by looping
fact=1
while num>0:
    fact=fact*num
    num=num-1
print("The factorial is:",fact)