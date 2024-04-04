"""
This program removes all of the ! in a string and print the string in reverse
"""

string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
string = string.replace("!"," ")
print(string)

string = string.upper()
print(string)
print(string[::-1])