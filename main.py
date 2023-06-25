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
            audio_file = eyed3.load(f)
            if audio_file is not None:
                audio_file_name = os.path.basename(audio_file.path)
                # use regex to extract artist and title from file name
                regex_pattern = r"^(?P<artist>[^-]+)\s*-\s*(?P<title>[^-]+)\.[^.]+$"
                matches = re.search(regex_pattern, audio_file_name)
                print("===========================================")
                if matches:
                    new_artist = matches.group("artist").strip()
                    new_title = matches.group("title").strip()
                    # old mp3 tags
                    try:
                        old_album_artist = audio_file.tag.album_artist
                    except:
                        old_album_artist = ""

                    try:
                        old_title = audio_file.tag.title
                    except:
                        old_title = ""

                    try:
                        old_artist = audio_file.tag.artist
                    except:
                        old_artist = ""
                    # new mp3 tags
                    audio_file.tag.album_artist = new_artist
                    audio_file.tag.title = new_title
                    audio_file.tag.artist = new_artist
                    try:
                        audio_file.tag.save()
                    except:
                        print("*************************************")
                        print("* An error occurred saving MP3 tags *")
                        print("*************************************")
                    else:
                        print(f"File Name: {audio_file_name}")
                        print("------------------------------------------")
                        print(f"Old Album Artist: {old_album_artist}")
                        print(f"Old Title: {old_title}")
                        print(f"Old Contributing Artists: {old_artist}")
                        print("------------------------------------------")
                        print(f"New Album Artist: {audio_file.tag.album_artist}")
                        print(f"New Title: {audio_file.tag.title}")
                        print(f"New Contributing Artists: {audio_file.tag.artist}")
                else:
                    print("*************************************")
                    print("*         No matches found          *")
                    print("*************************************")
