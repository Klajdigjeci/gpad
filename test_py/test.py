from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""

<Screen1>:


    Label:
        font_size: 50
        center_x: root.width / 2
        top: root.top
        text: "Gnotes"

    Button:
        center_x: root.width * 1 / 4
        top: root.top - 100
        text: "New ideas"
        width: 250

    Button:
        center_x: root.width * 3 / 4
        top: root.top - 100
        text: "learning notes"
        width: 250

    Button:
        center_x: root.width * 1 / 4
        top: root.top - 250
        text: "Reminders"
        width: 250

    Button:
        center_x: root.width * 3 / 4
        top: root.top - 250
        text: "Goals"
        width: 250



    Button:
        text: 'Goto settings'
        on_press: root.manager.current = 'settings'
        center_x: root.width * 3 / 4
        top: root.top - 400
        width: 250

<Screen2>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'


""")

# Declare both screens
class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(Screen1(name='menu'))
sm.add_widget(Screen2(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
