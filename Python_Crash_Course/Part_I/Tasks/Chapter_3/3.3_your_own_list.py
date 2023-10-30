# Ex. 3.3
# Think about your favorite means of transportation, for example, a motorcycle or a car,
# and then create a list storing multiple examples. Use this list to display a few sentences about its items,
# for example, "I would like to own a Honda motorcycle."

means_of_transport = ['car', 'motorcycle', 'yacht', 'plane', 'bike']
vehicle_brands = ['Honda', 'Mazda', 'Merida', 'F16', 'Amels']

message_one = f"I would like to have a {vehicle_brands[2]} {means_of_transport[4]}.\n"
message_two = f"I wish to have a {vehicle_brands[4]} {means_of_transport[2]}.\n"
message_three = f"I think that the best of cars are {vehicle_brands[1]} {means_of_transport[0]}.\n"
message_four = f"The {vehicle_brands[3]} {means_of_transport[3]} is the one of the fastest planes.\n"
message_five = f"If someone say {means_of_transport[1]} then I think a {vehicle_brands[0]} {means_of_transport[1]}."

print(message_one, message_two, message_three, message_four, message_five)
