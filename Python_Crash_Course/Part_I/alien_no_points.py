# Using bracketed keys to retrieve desired values from a dictionary can lead to a potential problem: if the specified
# key does not exist, the result will be an error. When working with a dictionary, you can use the get() method to
# define a default value that will be returned if the requested key does not exist.
# The get() method requires a key as the first argument. The second, optional argument is the value returned if the
# specified key does not exist in the dictionary.

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No assigned points.')
print(point_value)
