# Ex. 7.10 Dream vacation
# Prepare a program asking users about their dream vacation. The program should display a question like: "If you could
# visit any one place in the world, where would you go?". Put a block of code in the program responsible for displaying
# the results of the survey.

responses = {}

survey_active = True

while survey_active:
    name = input("\nWhat's your name? ")
    response = input("If you could visit any one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Does anyone else want to participate in the survey? (yes / no) ")
    if repeat == 'no':
        survey_active = False

print("\n--- Survey results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
