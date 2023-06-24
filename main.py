import eyed3
import os
import re

music_dir = "musics"

# iterate over files in
# that directory
for filename in os.listdir(music_dir):
    f = os.path.join(music_dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # checking if it is mp3
        _, file_extension = os.path.splitext(f)
        if file_extension.lower() == ".mp3":
            audiofile = eyed3.load(f)
            audiofile_name = os.path.basename(audiofile.path)

            regex_pattern = r"^(?P<artist>[^-]+)\s*-\s*(?P<title>[^-]+)\.[^.]+$"
            matches = re.search(regex_pattern, audiofile_name)
            if matches:
                artist = matches.group("artist").strip()
                title = matches.group("title").strip()
                # change mp3 tags
                audiofile.tag.album_artist = artist
                audiofile.tag.title = title
                audiofile.tag.artist = artist

                print("===========================================")
                try:
                  audiofile.tag.save()
                except:
                  print("*************************************")
                  print("* An error occurred saving MP3 tags *")
                  print("*************************************")
                else:
                  print(f"File Name: {audiofile_name}")
                  print("------------------------------------------")
                  print(f"Old Album Artist: {audiofile.tag.album_artist}")
                  print(f"Old Title: {audiofile.tag.title}")
                  print(f"Old Artist: {audiofile.tag.artist}")
                  # print(f"Old Album: {audiofile.tag.album}")
                  print("------------------------------------------")
                  print(f"New Album Artist: {artist}")
                  print(f"New Title: {title}")
            else:
                print("*************************************")
                print("*         No matches found          *")
                print("*************************************")
