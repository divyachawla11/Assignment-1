#Program that checks if a given string starts with a given prefix and ends with a given suffix
test_str=input("Enter the string: ")
prefix=input("Enter the prefix to check: ")
suffix=input("Enter the suffix to check: ")
if test_str.startswith(prefix)==True:
    print("The string starts with the given prefix!")
else:
    print("The string does not start with the given prefix!")
if test_str.endswith(suffix)==True:
    print("The string ends with the given suffix!")
else:
    print("The string does not end with the given suffix!")