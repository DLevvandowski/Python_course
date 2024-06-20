# Ex. 8.14 Cars
# Create a function that stores car information in a dictionary. This function should always receive the name of make
# and model of the vehicle, followed by any number of keyword arguments. Call the function with the required information
# and two additional name-value pairs, for example describing the color and accessories. The prepared function should be
# called in a manner similar to the one shown below:
#   car = make_car('subaru', ',outback', color='blue', tow_package='True')
# Display the contents of the dictionary returned by this function, and make sure that all the specified information is
# correctly stored in it.

def make_car(make_of, model, **car_info):
    car_info['make_of_car'] = make_of
    car_info['model'] = model
    return car_info


car = make_car('Nissan', 'GTR',
               hp=600,
               cost=250000)

print(car)
