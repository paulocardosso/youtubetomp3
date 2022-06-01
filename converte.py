import PySimpleGUI as sg
from pytube import YouTube

def converter(link,pasta,name):
    try:
        yt = YouTube(link)
    except:
        print('Link/URL Invalído! Por favor, tente novamente!')
    else:
        video = yt.streams.get_by_itag(140)
        filename = "{}.mp3".format(name)
        if pasta:
            pasta = r'{}/'.format(pasta)
            file = video.download(filename=filename, output_path=pasta)
        else:
            file = video.download(filename=filename)
        print('Conversão Concluída!\nLocal: {}'.format(file))

class Tela:
    def __init__(self):
        layout = [
                    [sg.Text('Nome do Arquivo:*')],
                    [sg.Input(key='name',size=(45), do_not_clear=False),sg.Text('Ex.: Brisa - IZA',font='Arial 8 italic')],
                    [sg.Text('Link do Youtube:*')],
                    [sg.Input(key='link',size=(45), do_not_clear=False)],
                    [sg.Text('Local de Destino:')],
                    [sg.Input(key='pasta',size=(45), do_not_clear=False), sg.FolderBrowse()],
                    [sg.Button('Converter'),sg.Button('Limpar')],
                    [sg.Text('*Campos obrigatórios',font='Arial 8 italic')],
                    [sg.Output(size=(50,10))],
                    [sg.Text(justification='r',text='Desenvolvido por Paulo Cardoso', font='Arial 8 bold')]
                ]
        self.window = sg.Window('Youtube para Mp3', layout, icon=r'C:\Users\Paulo\Documents\Projetos\DIO\interfaces\convert.ico')

    def Iniciar(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WINDOW_CLOSED:
                break
            if self.event == 'Converter':
                if self.values['link'] and self.values['name']:
                    converter(self.values['link'],self.values['pasta'],self.values['name'])
                else:
                    print('Por favor, preenche os campos obrigatórios para realizar a conversão!')

if __name__ == '__main__':
    tela = Tela()
    tela.Iniciar()