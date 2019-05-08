from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

class IncrediblyCrudeClock(Label):
    a = NumericProperty(60)  # seconds

    def open_reminder(self,fileName):
        reminder = ""
        fob = open(fileName,'r')
        for line in fob.readlines():
            reminder += line
        return reminder

    def save_reminders(self,reminder_one,fileName_one):
        fob = open(fileName_one,'w')
        fob.write(reminder_one)
        fob.close()

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        reminder_one = self.open_reminder('reminder_one.txt')
        self.text_input_one= TextInput(text=reminder_one,pos_hint={"center_x":0.6,"center_y": 0.9},size_hint=(0.7,0.1))
        self.button= Button(text="Save All", size_hint=(0.1,0.1), pos_hint={"center_x":0.5, "center_y":0.5},on_press=lambda x:self.save_reminders(self.text_input_one.text,'reminder_one.txt'))
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)
        self.add_widget(self.text_input_one)
        self.add_widget(self.button)

    def on_a(self, instance, value):
        self.text = str(round(value, 1))

class TimeApp(App):
    def build(self):
        crudeclock = IncrediblyCrudeClock()
        crudeclock.start()
        return crudeclock

if __name__ == "__main__":
    TimeApp().run()
