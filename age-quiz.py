age = int(input("What is you age?  "))

if age >= 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy you retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13 :
    print("You qualify for the kiddie")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number")