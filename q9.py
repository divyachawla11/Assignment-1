#Program that checks whether a substring is present in the given string
main_str=input("Enter the main string: ")
substr=input("Enter the substring that you want to check: ")
result=substr in main_str
if result==True:
    print("The substring is a part of the main string!")
else:
    print("The substring is not a part of the main string!")