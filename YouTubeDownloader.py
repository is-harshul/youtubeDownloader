
from pytube import YouTube

SAVE_PATH = 'E:/'

link = 'https://www.youtube.com/watch?v=hXfigUyeHaY'

try:
    yt =  pytube.YouTube(link)
except:
    print("Connection Error.")

mp4files = yt.filter('mp4')

yt.set_filename('Video_downloaded')

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

try: 
    #downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 

print('Task Completed!') 
