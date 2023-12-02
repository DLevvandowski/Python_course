# Whenever you use the input() function, you should try to prepare a clear and understandable message that explains to
# the user exactly what kind of information is expected. Here, any message indicating to the user what information he
# should provide will work. Look at the example shown below.

name = input("Enter your name: ")
print(f"Hello, {name.title()}!")

# Sometimes you need to prepare a message much longer than just one line of text. For example, in a message you explain
# to the user exactly why you are asking for specific information. In this case, you can put the message in a variable,
# which will then be passed to the input() function. In this way, you can prepare a really long message, followed by a
# clear and concise call to the input() function, as I have shown below.

print('-----')
prompt = "If you tell us who you are, we will personalize the displayed message."
prompt += "\nWhat's your name? "

name = input(prompt)
print(f"Hello, {name.title()}!")
