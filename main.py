import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __int__(self):
        super(MyRoot, self).__int__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))

class DevelopingApp(App):

    def build(self):
        return MyRoot()

DevelopingApp = DevelopingApp()
DevelopingApp.run()