user_album_active = True

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

while user_album_active == True:
    print('Enter "q" to quit')
    
    user_artist = input('Name of the artist: ')
    if user_artist == 'q':
        user_album_active = False
        break
    
    user_album_title = input('Name of the album: ')
    if user_album_title == 'q':
        user_album_active = False
        break
   
    user_sold = input('Albums Sold (Optional, press enter to skip) : ')
    if user_sold == 'q':
        user_album_active = False
        break
    
    if user_sold:   
        album = make_album(user_artist,user_album_title,user_sold)
        print(album)
        user_album_active = False
        break
    else:
        album = make_album(user_artist,user_album_title)
        print(album)
        user_album_active = False
        break


# my code allows you tadd your own 
# artist as well as any album they 
# have made and how many copies that 
# album sold.you can enter q to end
# the program.