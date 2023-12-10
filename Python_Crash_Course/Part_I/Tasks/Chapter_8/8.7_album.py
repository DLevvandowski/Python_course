# Ex. 8.7 Album
# Create a function called make_album() responsible for building a dictionary representing a music album. The function
# should retrieve the band or artist name and album title. The function's return value should be a dictionary containing
# these two bits of information. Using the prepared function, create three dictionaries representing different albums.
# Display each return value to show that the dictionaries correctly store album information.
# Using the special value None, add an optional parameter to the make_album() function to store the number of songs on
# the album. If the function call contains a value for the number of songs, add it to the album information dictionary.
# Define at least one new function call that also includes the number of songs on the album.

def make_album(artist, title, numer_of_songs=None):
    """Displays album information."""
    album = {'artist': artist, 'title': title}
    if numer_of_songs:
        album['number_of_songs'] = numer_of_songs
    return album


album_1 = make_album('three days grace', 'life starts now', 12)
album_2 = make_album('metallica', 'metallica', 12)
album_3 = make_album('system of a down', 'toxicity')

print(album_1)
print(album_2)
print(album_3)
