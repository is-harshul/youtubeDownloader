from bs4 import BeautifulSoup as bs
import requests
from pytube import YouTube

base = "https://www.youtube.com/results?search_query="
qstring = "shivani+mangal"
req = requests.get(base+qstring)

page = req.text
soupData=bs(page,'html.parser')

vids = soupData.findAll('a',attrs={'class':'style-scope yt-img-shadow'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)

count=0
for item in videolist:
    count+=1    # increment counter
    yt = YouTube(item)   # initiate the class
    #formats = yt.get_videos()     # have a look at the different formats available
    video = yt.get('mp4', '360p')     # grab the video
    yt.set_filename('Video_'+str(count))       # set the output file name
    # video.download('./nancy/')  # download the video
    video.download('E:/')
