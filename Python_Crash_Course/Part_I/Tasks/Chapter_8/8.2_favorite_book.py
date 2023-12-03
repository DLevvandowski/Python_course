# Ex. 8.2 Favorite book
# Create a function called favorite_book() that accepts a single title parameter. This function should display a message
# like: "One of my favorite books is Alice in Wonderland". Call this function and make sure to pass the book title as an
# argument.

def favorite_book(book):
    """Displays name of favorite book that is used as an argument."""
    print(f"One of my favourite books is {book.capitalize()}.")

favorite_book('alice in wonderland')
