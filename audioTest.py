from ffpyplayer.player import MediaPlayer
import time

video = 'data/1280x720_5mb.mp4'

player = MediaPlayer(video)
val = ''
count=0
while val != 'eof':
    frame, val = player.get_frame()   
    count+=1
    print(count)
