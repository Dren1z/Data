'''
Printing a pattern with *
variables:
    row - row of the pattern
'''

for row in range(10):
    if row <= 5:  # for row <= 5, print (row) asterisks
        print(row*'*')
    else:       # for row > 5, print (10-row) asterisks
        print((10-row)*"*")