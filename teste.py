import PySimpleGUI as sg
import youtube_dl
from pytube import YouTube


class Tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Link do Youtube:')],
            [sg.Input(key='link', size=(50), do_not_clear=False)],
            [sg.Text('Pasta de Destino:')],
            [sg.Input(key='pasta', size=(50), do_not_clear=False), sg.FolderBrowse()],
            [sg.Button('Converter'), sg.Button('Limpar')],
            [sg.Output(size=(50, 10))]
        ]
        #janela
        self.janela = sg.Window('Nome da Janela',layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            if self.button == sg.WINDOW_CLOSED:
                break
            if self.button == 'Converter':
                print('OK')


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
    #run_pytube()
    tela = Tela()
    tela.Iniciar()