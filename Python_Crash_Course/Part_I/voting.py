# We assume that we have a variable storing the age of a person, and we want to determine whether that person is old
# enough to participate in the vote. The following code snippet checks whether the person can participate in the voting.

age = 19

if age >= 18:
    print("You can vote!")
    print("Have you already registered to vote?")

print("\n------\n")

# Often we want to take one action if the conditional test is passed, and a completely another if it is not passed. The
# if-else syntax offered by Python gives us this possibility.

age = 17

if age >= 18:
    print("You can vote!")
    print("Have you already registered to vote?")
else:
    print("We're sorry, but you're too young to vote.")
    print("You can register after you turn 18!")
