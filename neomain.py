from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random

class end(App):
    def build(self):
        return Button(text=str('deu ruim, score: '+ str(won)),
                      font_size='95sp',
                     color = [0, 255, 0, 1], on_press=exit)
class Program(GridLayout):
    
    def __init__(self, **kwargs):
        super(Program, self).__init__(**kwargs)
        global won
        global lost
        won, lost = 0, 0
        def choose(cup):
            global won
            global lost
            coin = random.randint(1,2)
            if lost > 9:
                end().run()
                exit()
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
''')
        score = BoxLayout()
        wonLabel = Label(text='Acertos:')
        lostLabel = Label(text='Erros:')
        wonPoints = Label(text=str(won))
        lostPoints = Label(text=str(lost))
        cupL = Button(text='Copo da Esquerda', on_press=choose)
        cupR = Button(text='Copo da Direita', on_press=choose)
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
    
        

class App(App):
    def build(self):
        return Program()

App().run()
