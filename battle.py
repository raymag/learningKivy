from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random
import json

class Battle(BoxLayout):
      def __init__(self, **kwargs):
            super(Battle, self).__init__(**kwargs)
            with open('data/database.json', 'r') as db:
                  database = json.load(db)
            print(database)
            self.add_widget(Label(text='hi'))

class App(App):
      def build(self):
            return Battle()


App().run()
