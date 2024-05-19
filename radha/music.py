import os
import assistant_details as ad
import file_search


music_path = "/home/avc/Desktop/radha-ai/songs/"

def play_music():
    if ad.is_ubuntu:
        os.system('rhythmbox-client --play')
        return "Playing Music"
    else:
        return "For windows not avilable yet"

def pause_music():
    if ad.is_ubuntu:
        os.system('rhythmbox-client --pause')
        return "pause Music"
    else:
        return "For windows not avilable yet"

def stop_music():
    if ad.is_ubuntu:
        os.system('rhythmbox-client --stop')
        return "Music stopped"
    else:
        return "For windows not avilable yet"

def next_song():
    if ad.is_ubuntu:
        os.system('rhythmbox-client --next')
        return "playing next song"
    else:
        return "For windows not avilable yet"

def previous_song():
    if ad.is_ubuntu:
        os.system('rhythmbox-client --previous')
        return "playing previous song"
    else:
        return "For windows not avilable yet"

def play_specific_song(song_name):
    song_name=song_name.replace('play','')
    
    if ad.is_ubuntu:
        file_search.set_root(music_path)
        songs = file_search.searchFile(song_name)
        try:
            song_uri = songs[0]
            command = 'rhythmbox-client --play-uri="'+ song_uri + '"'
            os.system(command)
            return "playing" + song_name
        except:
            return "song not found in your computer"
        return "playing "+ song_name
     
    else:
        return "For windows not avilable yet"

# play_specific_song("do-you-know")
