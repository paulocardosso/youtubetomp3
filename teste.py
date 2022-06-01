import PySimpleGUI as sg
from pytube import YouTube

def run_pytube(link,pasta):
    yt = YouTube(link)
    video = yt.streams.get_by_itag(140)
    filename = "{}.mp3".format(yt.title)
    if '|' in filename:
        filename = filename.replace('|','-')
    elif '/' in filename:
        filename = filename.replace('/', '-')
    if pasta:
        pasta = r'{}/'.format(pasta)
        file = video.download(filename=filename, output_path=pasta)
    else:
        file = video.download(filename=filename)
    print('Conversão Concluída!\nLocal: {}'.format(file))


layout = [
            [sg.Text('Link do Youtube:')],
            [sg.Input(key='link',size=(50), do_not_clear=False)],
            [sg.Text('Local de Destino:')],
            [sg.Input(key='pasta',size=(50), do_not_clear=False), sg.FolderBrowse()],
            [sg.Button('Converter'),sg.Button('Limpar')],
            [sg.Output(size=(50,10))]
        ]

window = sg.Window('Youtube para Mp3', layout, icon=r'C:\Users\Paulo\Documents\Projetos\DIO\interfaces\convert.ico')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Converter':
        if 'youtube' in values['link'] and 'http' in values['link'] and 'watch' in values['link']:
            run_pytube(values['link'],values['pasta'])
        else:
            print('Link/URL Invalído! Por favor, tente novamente!')