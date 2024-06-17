#Program that converts temperature from celsius to fahrenheit and vice versa based on user input
print("Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius")
choice=int(input("Enter your choice: "))
if choice==1:
    temp=float(input("Enter the temperature in celsius: "))
    res_temp=float((1.8*temp)+32)
    print("The temperature in Farenheit is:",res_temp)
elif choice==2:
    temp=float(input("Enter the temperature in Farenheit: "))
    res_temp=float((temp-32)/1.8)
    print("The temperature in Celsius is:",res_temp)
else:
    print("Invalid choice!!!")