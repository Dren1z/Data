'''
This program reads a string and makes each alternate char into an upper case and each
other alternate char a lower case

It also generates an output that makes each alternative word lower and upper case
'''

string = input("Enter a string: ")
string = string.upper() # format all characters into upper case
result1, result2 = "", [] # initialize a string to store converted string 
                          # initialize a list to store coverted words

# alternate upper and lower characters
for i in range(len(string)):
    if i % 2 == 0: 
        result1 += (string[i]) # if in even position, lower case
    else:
        result1 += (string[i].lower())  #if in odd position, upper case

print(result1)


# alternate upper and lower words
lst = string.split(" ") # split the string into list of words
for i in range(len(lst)):
    if i % 2 != 0: 
        result2.append(lst[i]) # if in odd position, lower case
    else:
        result2.append(lst[i].lower())  #if in even position, upper case

result2 = ' '.join(result2) # convert list to string, joined by space
print(result2)
