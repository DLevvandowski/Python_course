# Ex. 8.3 T-shirt
# Create a function called make_shirt(), accepting the size of the shirt and the text to be printed on it. The function
# should display a sentence containing information about the T-shirt you ordered: its size and the text to be printed on
# it.
#
# During the first call of the function to prepare the shirt, use positional arguments. On the other hand, during the
# second call, use keyword arguments.

def make_shirt(size, sentence):
    """Displays information about the T-shirt you ordered: its size and the text to be printed on it."""
    print(f"\nSize of the t-shirt you have chosen is {size}.")
    print(f"You have selected the following text to be printed on a T-shirt: {sentence}.")

make_shirt("XL", 'My T-shirt')
make_shirt(size='XL', sentence='My T-shirt')
