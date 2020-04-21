string = input()
string = string[::-1]
value = ''
string1,j = 0,0
for i in string:
    if i.islower():
        string1 = ord(i)-96
    elif i.isupper():
        string1 = ord(i)-64
    else:
        print("Please Enter valid Character: ")
    string1 += j
    j +=  1
    value += str(string1)
print(value)
    
