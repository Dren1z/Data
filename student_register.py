"""
This program allows a user to register students for an exam venue

"""

num = int(input("Please enter the number of students that you want to register: "))


student_ids = []# Initialize a list to store student IDs
i = 1 # Initialize counter
while i <= num:
    id = input("ID number (-1 if previous ID is wrong): ")

    # Check if the user wants to correct the previous ID
    if id == "-1" and student_ids:
        student_ids.pop()  # Remove the last ID
        print("Previous ID removed. Please enter a new ID.")
        i -= 1
        # Revert to previous counter
        continue

    # Add the ID to the list
    student_ids.append(id)
    i += 1


# Write the IDs to the file
with open('student_register.txt', 'w') as file:
    for id in student_ids:
        file.write(id + ": .................................\n")