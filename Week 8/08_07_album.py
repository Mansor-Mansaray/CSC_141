def make_album(artist, album_name, number_of_songs = ''):
    album = {'Artist' : artist, 'Album Title' : album_name}
    if number_of_songs:
        album['Copys Sold'] = int(number_of_songs)
    return album

album = make_album('Juice Wrld', 'Legends Never Die')
print(album)

album = make_album('Fall Out Boy', 'MANIA')
print(album)

album = make_album('The Weekwnd', 'After Hours', 2032000)
print(album)