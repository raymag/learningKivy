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
            super(Battle, self).__init__(**kwargs, orientation='vertical')
            def loadData(self): #Carrega os Dados do Programa
                  global database
                  database = ['Jucelino']
                  try:
                        with open('data/database.json', 'r') as db:
                              database = json.load(db)
                  except FileNotFoundError:
                        with open('data/database.json', 'w') as db:
                              database = json.dump(database, db)
            def loadMainLayout(self): #Carrega o Layout Inicial
                  #Seções Raízes ==================
                  topBox = BoxLayout()
                  bottomBox = BoxLayout(orientation='vertical')
                  topper = BoxLayout()

                  self.add_widget(topper)
                  self.add_widget(topBox)
                  self.add_widget(bottomBox)

                  #Seções topBox ==================
                  leftGrid = GridLayout(cols=2)
                  rightGrid = GridLayout(cols=2)

                  topBox.add_widget(leftGrid)
                  topBox.add_widget(rightGrid)

                  #Seções Topper =================
                  nameLabelText = Label(text='Nome:')
                  nameLabelValue = Label(text=str(database[0]))
                  
                  topper.add_widget(nameLabelText)
                  topper.add_widget(nameLabelValue)
                  

                  #Seções leftGrid =================
                  hpPlayerLabelText = Label(text='Vida:')
                  hpPlayerLabelValue = Label(text='10')
                  coinPlayerLabelText = Label(text='Moedas:')
                  coinPlayerLabelValue = Label(text='000')
                  hpotPlayerLabelText = Label(text='HP Pot')
                  hpotPlayerLabelValue = Label(text='00')

                  leftGrid.add_widget(hpPlayerLabelText)
                  leftGrid.add_widget(hpPlayerLabelValue)
                  leftGrid.add_widget(coinPlayerLabelText)
                  leftGrid.add_widget(coinPlayerLabelValue)
                  leftGrid.add_widget(hpotPlayerLabelText)
                  leftGrid.add_widget(hpotPlayerLabelValue)

                  #Seções rightGrid ================
                  hpEnemyLabelText = Label(text='Vida:')
                  hpEnemyLabelValue = Label(text='10')
      
                  rightGrid.add_widget(hpEnemyLabelText)
                  rightGrid.add_widget(hpEnemyLabelValue)

                  #Seções Bottom ================
                  atackButton = Button(text='Atacar')

                  bottomBox.add_widget(atackButton)
            
            loadData(self)
            loadMainLayout(self)
            
      

class App(App):
      def build(self):
            return Battle()


App().run()
