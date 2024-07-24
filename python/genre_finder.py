import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='your_client_id',
                                                           client_secret='your_client_secret'))

def get_genre(artist_name):
    result = spotify.search(q=artist_name, type='artist', limit=1)
    if result['artists']['items']:
        genres = result['artists']['items'][0]['genres']
        return ', '.join(genres)
    return 'Unknown'

artists = []
dates = []
genres = []

# read artists csv
print('Reading...')
with open('csv/ArtistsXXXX.csv', mode='r') as file:
    reader = csv.reader(file)

    for row in reader:
        artists.append(row[0])
        dates.append(row[1])

# find genres
print('Finding genres...')
for artist in artists:
    genre = get_genre(artist)
    genres.append(genre)

# write Lollapalooza csv
print('Writing...')
with open('csv/LollapaloozaXXXX.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    for i in range(len(artists)):
        writer.writerow([artists[i], dates[i], genres[i]])