import vlc
import time

# Function to play a song
music_file = 'Gulabi-Sadi_320(PaglaSongs).mp3'
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

# Create media player
player = instance.media_player_new()

# Load the MP3 file
media = instance.media_new(music_file)
player.set_media(media)

# Start playing
player.play()

# Wait for playback to finish
while player.is_playing():
    pass

