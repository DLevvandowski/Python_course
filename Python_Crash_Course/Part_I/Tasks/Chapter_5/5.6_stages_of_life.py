# Ex. 5.6 Stages of life
# Prepare an if-else construction that establishes the stage of a person's life person. Assign a value to the age
# variable, and then:
#  If the person is less than 2 years old, display a message indicating that he or she is an infant.
#  If the person is at least 2 years old but less than 4, display a message indicating that the person is a child who
#   is learning to walk.
#  If the person is at least 4 years old but less than 13, display a message indicating that the person is a child.
#  If the person is at least 13 years old but less than 20, display a message indicating that he is a teenager.
#  If the person is at least 20 but less than 65, display a message indicating that they are an adult.
#  If the person is at least 65 years old, display a message indicating that he/she is a senior citizen.

age = 28

if age < 2:
    print("The person is an infant.")
elif age < 4:
    print("The person is a child who is learning to walk.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
elif age >= 65:
    print("The person is a senior citizen.")
