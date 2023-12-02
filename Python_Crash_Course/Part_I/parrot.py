# The input() function pauses the program and waits for the user to provide some information. The input data he enters
# is stored in a variable, which allows you to work with it conveniently.
# For example, in the program shown below, we ask the user to enter any text, which will then be displayed back to the
# user.

message = input("Please tell me something about you and I'll show you this on the screen: ")
print(message)

print("-----")

# The program can run as long as the user wants it to. To do this, we need to put the program logic inside a while loop.
# In the following program, we will define the so-called output value - the program will run until the user enters this
# value.

prompt = "\nPlease tell me something about you and I'll show you this on the screen."
prompt += "\nEnter 'end' to stop program. "

message = ""
while message != "end":
    message = input(prompt)

    if message != "end":
        print(message)
    else:
        print("Cya later!")

# For a program that runs as long as certain conditions are met, a single variable can be defined to indicate whether
# the entire program remains active. This kind of variable is referred to as a flag and is a kind of signal for the
# program. We can create programs that will run as long as the flag is assigned the value True, and will terminate its
# operation when any of the events causes the flag to be assigned the value False.

active = True
while active:
    message = input(prompt)

    if message == "end":
        print("Cya later!")
        active = False
    else:
        print(message)
