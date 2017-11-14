from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class Forca(BoxLayout):
    def __init__(self):
        self.loadWord()
        super(Forca, self).__init__()
        self.loadScreen()
    def loadWord(self):
        self.words = ["banana", "roupa", "barco",
         "mesa", "computador", "astronalta"]
        self.word = random.choice(self.words)
    def loadScreen(self):
        self.key = list(self.word)
        self.keyword = ''
        for letter in self.key:
            self.keyword += "_"
        print(self.keyword, self.key)
        self.ids.screen.text = self.keyword
    def tryGuest(self):
        print(self.word)

class program(App):
    def build(self):
        return Forca()
program().run()
