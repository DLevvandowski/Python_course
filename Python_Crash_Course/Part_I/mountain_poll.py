# During each iteration of the while loop, the necessary amount of input can be taken. We will now create a program in
# which, during each iteration of the while loop, the user will provide the name and answer to the question.

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb one day? ")

    responses[name] = response

    repeat = input("Does anyone else want to participate in the survey? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Survey results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
