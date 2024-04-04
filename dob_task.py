'''
This program reads DOB.text and print the names and birthdates separately
'''

file  = open("DOB.txt","r") # open as read only
lines = file.readlines()
print("Name:")
for line in lines:
    words = line.split(" ")  # turn each line into a list
    print(" ".join(words[:2])) # print the first two elements, i.e. first and last name

print("\n")   # separate the name and datebirth with an empty line
print("Birthdate:")
for line in lines:
    line = line.strip() # remove the \n after each line
    words = line.split(" ")
    print(" ".join(words[2:5])) # print the last three elements, i.e. dates

file.close() # close file