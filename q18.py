#Program that checks if two strings are anagrams of each other or not
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")
list1=list(str1.lower())
list2=list(str2.lower())
list1.sort()
list2.sort()
if list1==list2:
    print("Yes! They are anagram strings")
else:
    print("No! They are not anagram strings")
