from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import random

class Program(GridLayout): #Program usa o GridLayout como base
    
    def __init__(self, **kwargs): #Kwargs é uma lista passada como parâmetros
        super(Program, self).__init__(**kwargs)
        global won #Definindo as variáveis como global
        global lost
        won, lost = 0, 0
        def newGame(arg): #Reseta e atualiza o Score para um novo jogo
            global won
            global lost
            won, lost = 0, 0
            wonPoints.text = str(won)
            lostPoints.text = str(lost)
            ending = (arg.parent).parent.parent #Eding é o PopUp criado em cada GameOver
            ending.parent.dismiss() 
        def choose(cup): #É executada a cada escolha entre Copo da Direita e Esquerda
            global won
            global lost
            coin = random.randint(1,2)#Um número aleatório é escolhido
            if lost > 9: #Caso os erros alcancem 10, GameOver
                ending = BoxLayout(orientation='vertical') #Layout criado para o PopUp
                GameOver = Label(text=str('deu ruim, score: '+ str(won)),
                      font_size='85sp',
                     color = [2, 255,2, 1])
                again = Button(text='Continuar?', on_press=newGame) #Invoca a função NewGame quando executada
                notAgain = Button(text='Sair?', on_press=exit)

                ending.add_widget(GameOver) #Adiciona os widgets ao PopUp Ending
                ending.add_widget(again)
                ending.add_widget(notAgain)
                end = Popup(title='End',
                            content=ending,
                            size=(400, 400)).open()
            #Atualiza o placar
            if coin == 1:  
                cups.text = 'Estava na esquerda!'
                if cup.text == 'Copo da Esquerda':
                    won += 1 
                    wonPoints.text = str(won)
                else:
                    lost += 1
                    lostPoints.text = str(lost)
            elif coin == 2:
                cups.text = 'Estava na direita!'
                if cup.text == 'Copo da Direita':
                    won += 1
                    wonPoints.text = str(won)
                else:
                    lost += 1
                    lostPoints.text = str(lost)
            #print(cup.text, won, lost)
        self.cols = 1
        cups = Label(text='''
Existe uma moeda escondida, um
copo na direita e outro na esquerda, em qual
deles reside a moeda?
''', font_size='30sp')
        score = BoxLayout()
        wonLabel = Label(text='Acertos:', font_size='40sp')
        lostLabel = Label(text='Erros:', font_size='40sp')
        wonPoints = Label(text=str(won), font_size='45sp')
        lostPoints = Label(text=str(lost), font_size='45sp')
        cupL = Button(text='Copo da Esquerda',
                      on_press=choose,
                      font_size='35sp')
        cupR = Button(text='Copo da Direita',
                      on_press=choose,
                      font_size='35sp')
        box = GridLayout()
        box.cols = 2
        
        self.add_widget(cups)
        self.add_widget(box)
        box.add_widget(cupL)
        box.add_widget(cupR)

        self.add_widget(score)
        score.add_widget(wonLabel)
        score.add_widget(wonPoints)
        score.add_widget(lostLabel)
        score.add_widget(lostPoints)
    
        

class App(App): #Classe base do programa
    def build(self): #Inicializa a janela e chama a classe Program
        return Program()

App().run()
