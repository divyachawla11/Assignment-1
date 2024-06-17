#Program that counts the frequency of each character in a string
Freq={}
str1=input("Enter the string: ")
for i in str1:
    if i in Freq:
        Freq[i]=Freq[i]+1
    else:
        Freq[i]=1
print(Freq)