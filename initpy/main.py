from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import json
import subprocess
import os
import pyautogui as pg
import time

class initpy(BoxLayout):
    def __init__(self):
        super(initpy, self).__init__()
        self.load()
        self.loadingFiles()
    def remove(self):
        def closePop(Button):
            self.update()
            self.loadingFiles()
            window.dismiss()
        def remove(widget):
            print(widget, widget.text)
            delpop.remove_widget(widget)
            del self.database[widget.text]
        delpop = BoxLayout(orientation='vertical')
        helpLabel = Label(text='Clique no Path para remover:')
        confirmButton = Button(text='Okay', on_release=closePop)
        delpop.add_widget(helpLabel)
        for path in self.database:
            delpop.add_widget(Button(text=path, on_release=remove))
        delpop.add_widget(confirmButton)
        window = Popup(title='Remover', content=delpop)
        window.open()
    def add(self):
        def addPath(var):
            pathName = path = newPath.text.lower()
            if 'c:' in pathName:
                pathName = pathName.split('/')[-1]
                pathName = str(pathName).split('\\')[-1]
                pathName = pathName.split('.')[0]
                print(pathName, path)
                self.database[pathName] = path
                self.update()
                self.loadingFiles()
        def closePop(Button):
            window.dismiss()
        addpop = BoxLayout(orientation='vertical')
        helpLabel = Label(text='Informe o caminho e formato do arquivo:')
        newPath = TextInput()
        confirmButton = Button(text='Confirmar', on_release=addPath)
        cancelButton = Button(text='Cancelar', on_release=closePop)
        addpop.add_widget(helpLabel)
        addpop.add_widget(newPath)
        addpop.add_widget(confirmButton)
        addpop.add_widget(cancelButton)
        window = Popup(title='Adicionar', content=addpop)
        window.open()
    def update(self):
        with open('data/database.json', 'w') as db:
            json.dump(self.database, db)
    def load(self):
        try:
            with open('data/database.json', 'r') as db:
                self.database = json.load(db)
        except FileNotFoundError:
            with open('data/database.json', 'w') as db:
                self.database = {}
                json.dump(self.database, db)
    def execute(self, button):
        print(button.text)
        #os.chdir((self.database[button.text]).split(button.text)[0])
        #print(os.getcwd())
        #print(command)
        #try:
        #    print(suprocess.call('start main.py', shell=True))
        #except:
        #    print(subprocess.call('start main.pyw', shell=True))
        pg.hotkey('winleft')
        time.sleep(1)
        pg.typewrite('cmd', interval=0.2)
        pg.press('enter')
        pg.typewrite(str((self.database[button.text]).split(button.text)[0]))

    def loadingFiles(self):
        self.ids.ProgramGrid.clear_widgets()
        for path in self.database:
            print(self.database[path])
            self.ids.ProgramGrid.add_widget(Button(text=path, on_release=self.execute, background_color=[1, 2, 3, 1], color=[0, 0, 0, 1]))
class App(App):
    def build(self):
        return initpy()

App().run()
