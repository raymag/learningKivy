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
            super(Battle, self).__init__(orientation='vertical')
            def newGame(self):
                global database
                database = ['Jucelino', 0, 10, 2, 100, 10, 2, 0, 100]
                print(self.parent.parent.child)
                loadStats(self, database)
            def loadStats(self, database):
                  self.nickName = database[0]
                  self.score = database[1]
                  self.playerHp = database[2]
                  self.playerShield = database[3]
                  self.playerCoin = database[4]
                  self.enemyHp = database[5]
                  self.enemyShield = database[6]
                  self.playerBottle = database[7]
                  self.enemyCoin = database[8]
                  print(self.nickName)
            def loadData(self, database): #Carrega os Dados do Programa
                  try:
                        with open('data/database.json', 'r') as db:
                              database = json.load(db)
                  except:
                        with open('data/database.json', 'w') as db:
                              database = json.dump(database, db)
            def loadMainLayout(self): #Carrega o Layout Inicial
                  #Secoes Raizes ==================
                  topBox = BoxLayout()
                  bottomBox = BoxLayout(orientation='vertical')
                  topper = GridLayout(cols=2)

                  self.add_widget(topper)
                  self.add_widget(topBox)
                  self.add_widget(bottomBox)

                  #Secoes topBox ==================
                  leftGrid = GridLayout(cols=2)
                  rightGrid = GridLayout(cols=2)

                  topBox.add_widget(leftGrid)
                  topBox.add_widget(rightGrid)

                  #Secoes Topper =================
                  nameLabelText = Label(text='Nome:')
                  nameLabelValue = Label(text=self.nickName)
                  scoreLabelText = Label(text='Score:')
                  scoreLabelValue = Label(text=str(self.score))
                  playerSide = Label(text='== Jogador ==')
                  enemySide = Label(text='== Oponente ==')

                  topper.add_widget(nameLabelText)
                  topper.add_widget(nameLabelValue)
                  topper.add_widget(scoreLabelText)
                  topper.add_widget(scoreLabelValue)
                  topper.add_widget(playerSide)
                  topper.add_widget(enemySide)


                  #Secoes leftGrid =================
                  hpPlayerLabelText = Label(text='Vida:')
                  hpPlayerLabelValue = Label(text=str(self.playerHp))
                  coinPlayerLabelText = Label(text='Moedas:')
                  coinPlayerLabelValue = Label(text=str(self.playerCoin))
                  hpotPlayerLabelText = Label(text='HP Bottle:')
                  hpotPlayerLabelValue = Label(text=str(self.playerBottle))
                  shieldPlayerLabelText = Label(text='Escudo:')
                  shieldPlayerLabelValue = Label(text=str(self.playerShield))

                  leftGrid.add_widget(hpPlayerLabelText)
                  leftGrid.add_widget(hpPlayerLabelValue)
                  leftGrid.add_widget(coinPlayerLabelText)
                  leftGrid.add_widget(coinPlayerLabelValue)
                  leftGrid.add_widget(hpotPlayerLabelText)
                  leftGrid.add_widget(hpotPlayerLabelValue)
                  leftGrid.add_widget(shieldPlayerLabelText)
                  leftGrid.add_widget(shieldPlayerLabelValue)

                  #Secoes rightGrid ================
                  hpEnemyLabelText = Label(text='Vida:')
                  hpEnemyLabelValue = Label(text=str(self.enemyHp))
                  coinEnemyLabelText = Label(text='Moedas:')
                  coinEnemyLabelValue = Label(text=str(self.enemyCoin))
                  shieldEnemyLabelText = Label(text='Escudo:')
                  shieldEnemyLabelValue = Label(text=str(self.enemyShield))

                  rightGrid.add_widget(hpEnemyLabelText)
                  rightGrid.add_widget(hpEnemyLabelValue)
                  rightGrid.add_widget(coinEnemyLabelText)
                  rightGrid.add_widget(coinEnemyLabelValue)
                  rightGrid.add_widget(shieldEnemyLabelText)
                  rightGrid.add_widget(shieldEnemyLabelValue)

                  #Secoes Bottom ================
                  atackButton = Button(text='Atacar')
                  buyHpotButton = Button(text='Comprar HP Bottle')
                  buyShieldButton = Button(text='Comprar Escudo')
                  saveButton = Button(text='Salvar')
                  newGameButton =Button(text='Novo Jogo', on_release=newGame)

                  bottomBox.add_widget(atackButton)
                  bottomBox.add_widget(buyHpotButton)
                  bottomBox.add_widget(buyShieldButton)
                  bottomBox.add_widget(saveButton)
                  bottomBox.add_widget(newGameButton)
            database = ['Jucelino', 0, 10, 2, 100, 10, 2, 0, 100]
            loadData(self, database)
            loadStats(self, database)
            loadMainLayout(self)
            print(self.nickName)



class App(App):
      def build(self):
            return Battle()


App().run()
