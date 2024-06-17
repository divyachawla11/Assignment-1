#Program that takes input from user until the user enters an empty line and then prints all the lines
lines=[]
while True:
    line=input("Enter input: ")
    if line!='':
        lines.append(line)
    else:
        break
result='\n'.join(lines)
print(result)
