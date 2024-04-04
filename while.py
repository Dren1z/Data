'''
The user will enter a number on prompt until he enters '-1'. Then the program will return the mean of the numbers entered.
variables:
    nmu - number entered
    sum - sum of the numbers entered
    i   - numbers of entry
'''


i = 0
sum = 0
while True:
    num = float(input("Please enter a number(-1 will end the program): "))
    if num == -1: # check whether entry is -1
        break
    sum += num
    i += 1

print(f"The average of the numbers entered is {sum/i}")