# Ex. 8.4 Big T-shirts
# Modify the make_shirt() function so that large t-shirts with the text "I love Python" printed on them are prepared by
# default. Create large and medium size T-shirts (both with the default text) and a T-shirt of any size and with
# different text printed on it.

def make_shirt(size="L", sentence="I love Python"):
    """Displays information about the T-shirt you ordered: its size and the text to be printed on it."""
    print(f"\nSize of the t-shirt you have chosen is {size}.")
    print(f"You have selected the following text to be printed on a T-shirt: {sentence}.")

make_shirt()
make_shirt("M")
make_shirt("XL", "My new brand")
