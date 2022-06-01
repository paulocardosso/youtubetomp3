import youtube_dl
from pytube import YouTube



def run_youtubedl():
    video_url = input("please enter youtube video url:\n")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

def run_pytube():

    yt = YouTube('https://www.youtube.com/watch?v=W4yiW11DtoU')

    #video = yt.streams.filter(abr='128kbps')
    video = yt.streams.get_by_itag(140)
    filename = "{}.mp3".format(yt.title)
    print(video.download(filename=filename))

    #video.

    #video.download(output_path='',filename='')



if __name__=='__main__':
    run_pytube()