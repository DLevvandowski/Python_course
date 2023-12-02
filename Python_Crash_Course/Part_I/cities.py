# To immediately exit the while loop without executing any remaining code in it and regardless of the result of the
# conditional test, you can use the break command. This command determines the control flow of the program operation.
# It can be used to indicate executed and unexecuted lines of code so that the program executes only the code you want
# to run, and does so when you want it to.

prompt = "\nName the cities you would like to visit."
prompt += "\n(When you have finished specifying the cities, write 'end'.). "

while True:
    city = input(prompt)

    if city == "end":
        print("Cya later!")
        break
    else:
        print(f"I'd visit {city.title()}!")
