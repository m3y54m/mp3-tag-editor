import eyed3

audiofile = eyed3.load("music.mp3")

print(audiofile.tag.title)
print(audiofile.tag.track_num)
print(audiofile.tag.artist)
print(audiofile.tag.album)
print(audiofile.tag.album_artist)

# audiofile.tag.title = "The Edge"
# audiofile.tag.track_num = 3
# audiofile.tag.artist = "Token Entry"
# audiofile.tag.album = "Free For All Comp LP"
# audiofile.tag.album_artist = "Various Artists"

# audiofile.tag.save()

