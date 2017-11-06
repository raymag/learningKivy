'''from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='NickName'))
        self.nickname = TextInput(multiline=False)
        self.add.widget(self.nickname)
        self.add_widget(Label(text='Key'))
        self.key = TextInput(password=True, multiline=False)
        self.add_widget(self.key)
class App(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    App().run()
'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Nickname'))
        self.nickname = TextInput(multiline=False)
        self.add_widget(self.nickname)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class App(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    App().run()
