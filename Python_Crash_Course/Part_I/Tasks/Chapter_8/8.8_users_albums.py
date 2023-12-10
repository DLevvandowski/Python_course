# Ex. 8.8 Users albums
# Start your work with the program created in Exercise 8.7. Add a while loop allowing users to enter the artist and
# album title. After collecting this information, call the make_album() function with the user's input and display the
# dictionary created by the program. Make sure you define a value to exit the while loop.

def make_album(artist, title, numer_of_songs=None):
    """Displays album information."""
    album = {'artist': artist, 'title': title}
    if numer_of_songs:
        album['number_of_songs'] = numer_of_songs
    return album


album = make_album('three days grace', 'life starts now', 12)
print(album)
album = make_album('metallica', 'metallica', 12)
print(album)
album = make_album('system of a down', 'toxicity')
print(album)

while True:
    print(f"\nEnter name of artist and name of album. (type 'q' to quit at any time)")

    artists_name = input("Artist's name: ")
    if artists_name == 'q':
        break

    albums_name = input("Album's name: ")
    if albums_name == 'q':
        break

    choice = input("Do you want to enter number of songs? (y/n)")
    if choice == 'y':
        songs_on_album = input("Number of songs: ")
        if songs_on_album == 'q':
            break
    else:
        songs_on_album = None

    album = make_album(artists_name, albums_name, songs_on_album)
    print(album)
