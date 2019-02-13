import pylast
from keys import API_KEY, API_SECRET, USERNAME, PASSWORD

password_hash = pylast.md5(PASSWORD)
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=USERNAME, password_hash=password_hash)

albums = network.get_user("JustBirdBrain").get_top_albums()

print(albums)
