import os
from dotenv import load_dotenv
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# load environmental variables
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')
scope = 'user-top-read'

# authenticate user with Spotify
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# fetch the current user's top artists
top_artists = spotify.current_user_top_artists(limit=50)

# collect genres from the top artists
genres = []
for artist in top_artists['items']:
    genres.extend(artist['genres'])

# count the top genres
genre_counts = Counter(genres)
top_genres = genre_counts.most_common(50)

# print the top genres
print("Top Genres:")
for idx, (genre, count) in enumerate(top_genres):
    print(f"{idx + 1}. {genre} (count: {count})")

# choose date

# create schedule