from kivy.app import App
from kivy.uix.widget import Widget
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager,Screen


class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass
    #def simple_calculator(number_one,sign,number_two):
    #    number_one = textinput

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

class buildGui(App):
    def build(self):
        return screen_manager

if __name__ == '__main__':
    buildGui.run()

#gnotes = buildGui()
#gnotes.run()
