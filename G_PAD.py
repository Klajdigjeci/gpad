from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from datetime import datetime, timedelta
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle



# Here is where I create the multiple canvas windows that switch when the buttons are pressed. I also design and create few objects in here.
w = Builder.load_string("""
#this is the main screen when the user starts the app
<Main_Screen>:
    #this is the with the image design
    canvas:
        Rectangle:
            source: 'images/ups.jpg'
            pos: self.pos
            size: self.size
    #the button that makes the transition to the new ideas screen
    Button:
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "new_ideas_screen"
        center_x: root.width * 0.2
        center_y: root.height * 0.45
        size_hint: .2,.1
        text: "New ideas"
        Image:
            source: 'images/logo.png'
            size: 30, 30
            center_x: root.width * 0.21
            center_y: root.height * 0.7

    Button:
        center_x: root.width * 0.2
        center_y: root.height * 0.25
        size_hint: .2,.1
        text: "Learning Notes"
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "learning_notes_screen"

    Button:
        center_x: root.width * 0.2
        center_y: root.height * 0.65
        size_hint: .2,.1
        text: "Reminders"
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "reminders_screen"

    Button:
        center_x: root.width * 0.7
        center_y: root.height * 0.45
        size_hint: .2,.1
        text: "Goals"
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "goals_screen"


    Button:
        center_x: root.width * 0.7
        center_y: root.height * 0.25
        size_hint: .2,.1
        text: "Other notes"

        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "other_notes_screen"


    Button:
        center_x: root.width * 0.7
        center_y: root.height * 0.65
        size_hint: .2,.1
        text: "Simple Calculator"
        on_press:
            root.manager.transition.direction = "left"
            root.manager.transition.duration = 1
            root.manager.current = "calculator_screen"


<New_Ideas_Screen>:

    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'


<Learning_Notes_Screen>:
    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'
<Reminders_Screen>:
    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'
    Label:
        center_x :root.width *0.73
        center_y: root.height * 0.75
        text: "Due in? (Days)"
        size_hint : 0.1,0.1

    Label:
        center_x :root.width *0.87
        center_y: root.height * 0.75
        text: "Due date:"
        size_hint : 0.1,0.1

<Goals_Screen>:
    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'

    Label:
        center_x :root.width *0.86
        center_y: root.height * 0.75
        text: "Achieved?"
        size_hint : 0.1,0.1

<Other_Notes_Screen>:

    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'


<Calculator_Screen>:
    number_one_input: number_one_input
    number_one: number_one_input.text
    number_two_input: number_two_input
    number_two: number_two_input.text
    sign: sign_input
    Button:
        center_x: root.width * 1 / 14
        pos: 500,500
        size_hint: .1,.1
        text: "Back"
        on_press: root.manager.current = 'main_screen'

    Button:
        text: "+"
        size_hint:.1,.1
        center_x:  root.width * 0.4
        id: sign_input
        center_y: root.height * 0.65
        on_press: root.adding(number_one_input.text,number_two_input.text)
    Button:
        id: subtraction
        text: "-"
        size_hint:.1,.1
        center_x:  root.width * 0.6
        center_y: root.height * 0.65
        on_press: root.subtracting(number_one_input.text,number_two_input.text)


    Button:
        id: multiplication
        text: "*"
        size_hint:.1,.1
        center_x:  root.width * 0.4
        center_y: root.height * 0.5
        on_press: root.multiplication(number_one_input.text,number_two_input.text)


    Button:
        id: division
        text: "/"
        size_hint:.1,.1
        center_x:  root.width * 0.6
        center_y: root.height * 0.5
        on_press: root.division(number_one_input.text,number_two_input.text)

    Button:
        id: power
        text: "^"
        size_hint:.1,.1
        center_x:  root.width * 0.4
        center_y: root.height * 0.35
        on_press: root.power(number_one_input.text,number_two_input.text)

    Button:
        id: powerInverse
        text: "x√y"
        size_hint:.1,.1
        center_x:  root.width * 0.6
        center_y: root.height * 0.35
        on_press: root.powerInverse(number_one_input.text,number_two_input.text)

    Label:
        id: number_one
        text: "Number 1:"
        center_x:  root.width * 0.2
        center_y: root.height * 0.6
        size_hint : 0.1,0.1

    TextInput:
        id: number_one_input
        center_x:  root.width * 0.2
        center_y: root.height * 0.5
        size_hint : 0.1,0.1

    Label:
        id: number_two
        text: "Number 2:"
        center_x:  root.width * 0.8
        center_y: root.height * 0.6
        size_hint : 0.1,0.1

    TextInput:
        id: number_two_input
        center_x:  root.width * 0.8
        center_y: root.height * 0.5
        size_hint : 0.1,0.1

    Label:
        id: result
        text: "Result:"
        size_hint:.1,.1
        center_x:  root.width * 0.5
        center_y: root.height * 0.2

    Label:
        id: math
        text: number_one_input.text
        size_hint:.1,.2
        center_x:  root.width * 0.4
        center_y: root.height * 0.75

    Label:
        id: math
        text: number_two_input.text
        size_hint:.1,.2
        center_x:  root.width * 0.6
        center_y: root.height * 0.75
""")


# Declaring the main screen
class Main_Screen(Screen):
     def __init__(self, **args):
        Screen.__init__(self, **args)

# Declaring the new ideas screen
class New_Ideas_Screen(Screen):

    def edit_one(self,element):
        element.size_hint=(0.7,0.15)
        element.pos_hint={"center_x":0.4,"center_y": 0.7}

    def edit_two(self,element):
        element.size_hint=(0.7,0.15)
        element.pos_hint={"center_x":0.4,"center_y": 0.5}

    def edit_three(self,element):
        element.size_hint=(0.7,0.15)
        element.pos_hint={"center_x":0.4,"center_y": 0.3}

    def edit_four(self,element):
        element.size_hint=(0.7,0.15)
        element.pos_hint={"center_x":0.4,"center_y": 0.1}

    def save_idea(self,idea,element,label,fileName):
        element.size_hint=(0.001,0.001)
        element.pos_hint={"center_x":1,"center_y": 1}
        fob = open(fileName,'w')
        fob.write(idea)
        fob.close()
        label.text = self.open_idea(fileName)

    #method that reads the ideas from the idea files
    def open_idea(self,ideaFile):
        idea = ""
        fob = open(ideaFile,'r')
        for line in fob.readlines():
            idea += line
        return idea

    #main method of the new ideas screen
    def __init__(self, **args):
        Screen.__init__(self, **args)

        #get the ideas from the files
        idea_one = self.open_idea('text_files/idea_one.txt')
        idea_two = self.open_idea('text_files/idea_two.txt')
        idea_three = self.open_idea('text_files/idea_three.txt')
        idea_four = self.open_idea('text_files/idea_four.txt')

#labels that show the ideas
        self.textLabel = Label(text="New Ideas", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.5, "center_y":0.95})
        self.label_one = Label(text=str(idea_one), text_size = (self.width*5.5,None), color=(1,0,0,1), font_size=(12),size_hint=(0.,0.7), pos_hint={"center_x":0.4, "center_y":0.7})
        self.label_two = Label(text=str(idea_two), text_size = (self.width*5.5,None), color=(0,1,0,1), font_size=(12),size_hint=(0.8,0.7), pos_hint={"center_x":0.4, "center_y":0.5})
        self.label_three = Label(text=str(idea_three), text_size = (self.width*5.5,None), color=(1,0,1,1), font_size=(12),size_hint=(0.8,0.7), pos_hint={"center_x":0.4, "center_y":0.3})
        self.label_four = Label(text=str(idea_four), text_size = (self.width*5.5,None), color=(1,1,0,1), font_size=(12),size_hint=(0.9,0.7), pos_hint={"center_x":0.4, "center_y":0.1})


#textboxs
        self.text_input_one= TextInput(text=idea_one,pos_hint={"center_x":0.4,"center_y": 0.7},size_hint=(0.7,0.15))
        self.text_input_two= TextInput(text=idea_two,pos_hint={"center_x":0.4,"center_y": 0.5},size_hint=(0.7,0.15))
        self.text_input_three= TextInput(text=idea_three,pos_hint={"center_x":0.4,"center_y": 0.3},size_hint=(0.7,0.15))
        self.text_input_four= TextInput(text=idea_four,pos_hint={"center_x":0.4,"center_y": 0.1},size_hint=(0.7,0.15))
#buttons
        self.save_one_button = Button(pos_hint={"center_x":0.92,"center_y": 0.7},size_hint=(0.1,0.1), text= "Save", on_press=lambda x: self.save_idea(self.text_input_one.text,self.text_input_one,self.label_one,'text_files/idea_one.txt'))
        self.edit_one_button = Button(pos_hint={"center_x":0.82,"center_y": 0.7},size_hint=(0.1,0.1), text= "Edit", on_press=lambda x: self.edit_one(self.text_input_one))
        self.save_two_button = Button(pos_hint={"center_x":0.92,"center_y": 0.5},size_hint=(0.1,0.1), text= "Save", on_press=lambda x: self.save_idea(self.text_input_two.text,self.text_input_two,self.label_two,'text_files/idea_two.txt'))
        self.edit_two_button = Button(pos_hint={"center_x":0.82,"center_y": 0.5},size_hint=(0.1,0.1), text= "Edit", on_press=lambda x: self.edit_two(self.text_input_two))
        self.save_three_button = Button(pos_hint={"center_x":0.92,"center_y": 0.3},size_hint=(0.1,0.1), text= "Save", on_press=lambda x: self.save_idea(self.text_input_three.text,self.text_input_three,self.label_three,'text_files/idea_three.txt'))
        self.edit_three_button = Button(pos_hint={"center_x":0.82,"center_y": 0.3},size_hint=(0.1,0.1), text= "Edit", on_press=lambda x: self.edit_three(self.text_input_three))
        self.save_four_button = Button(pos_hint={"center_x":0.92,"center_y": 0.1},size_hint=(0.1,0.1), text= "Save", on_press=lambda x: self.save_idea(self.text_input_four.text,self.text_input_four,self.label_four,'text_files/idea_four.txt'))
        self.edit_four_button = Button(pos_hint={"center_x":0.82,"center_y": 0.1},size_hint=(0.1,0.1), text= "Edit", on_press=lambda x: self.edit_four(self.text_input_four))
#adding the labels
        self.add_widget(self.textLabel)
        self.add_widget(self.label_one)
        self.add_widget(self.label_two)
        self.add_widget(self.label_three)
        self.add_widget(self.label_four)
#adding the textboxes and the buttons
        self.add_widget(self.text_input_one)
        self.add_widget(self.save_one_button)
        self.add_widget(self.edit_one_button)

        self.add_widget(self.text_input_two)
        self.add_widget(self.save_two_button)
        self.add_widget(self.edit_two_button)

        self.add_widget(self.text_input_three)
        self.add_widget(self.save_three_button)
        self.add_widget(self.edit_three_button)

        self.add_widget(self.text_input_four)
        self.add_widget(self.save_four_button)
        self.add_widget(self.edit_four_button)

#the learning notes class
class Learning_Notes_Screen(Screen):

    #method that save the learning notes to the file
    def save_learning_notes(self,title_one,title_two,title_three,notes_one,notes_two,notes_three,fileName_one,fileName_two,fileName_three):
        fob = open(fileName_one,'w')
        fob.write(title_one)
        fob.write(notes_one)
        fob.close()

        fob_two = open(fileName_two,'w')
        fob_two.write(title_two)
        fob_two.write(notes_two)
        fob_two.close()

        fob_three = open(fileName_three,'w')
        fob_three.write(title_three)
        fob_three.write(notes_three)
        fob_three.close()

    #method that reads the title of the notes from the file
    def open_title(self,fileName):
        first_line=""
        with open(fileName) as f:
            first_line = f.readline()
        return first_line

    #method that reads the notes from the file
    def open_learning_notes(self,fileName):
        learn_notes= ""
        with open(fileName) as f:
            f.readline()
            for line in f:
                learn_notes += line
        return learn_notes


    #main method of the learning notes class
    def __init__(self, **args):
        Screen.__init__(self, **args)

        #basic label for learning notes
        self.label = Label(text="Learning Notes", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.5, "center_y":0.95})
        self.add_widget(self.label)

        #gets the value to the title and the learning notes from the files
        title_one = self.open_title('text_files/learning_notes_one.txt')
        title_two = self.open_title('text_files/learning_notes_two.txt')
        title_three = self.open_title('text_files/learning_notes_three.txt')

        explanation_one = self.open_learning_notes('text_files/learning_notes_one.txt')
        explanation_two = self.open_learning_notes('text_files/learning_notes_two.txt')
        explanation_three = self.open_learning_notes('text_files/learning_notes_three.txt')



#---first textbox (capital letters)
        self.text_input_one= TextInput(text=title_one,pos_hint={"center_x":0.5,"center_y": 0.72},size_hint=(0.87,0.08),font_size=16.5)
        self.add_widget(self.text_input_one)
#-- First explanation textbox
        self.text_explanation_one= TextInput(text=explanation_one,pos_hint={"center_x":0.5,"center_y": 0.60},size_hint=(0.87,0.15))
        self.add_widget(self.text_explanation_one)
#---second textbox (capital letters)
        self.text_input_two= TextInput(text=title_two,pos_hint={"center_x":0.5,"center_y": 0.47},size_hint=(0.87,0.08))
        self.add_widget(self.text_input_two)
#-- second explanation textbox
        self.text_explanation_two= TextInput(text=explanation_two,pos_hint={"center_x":0.5,"center_y": 0.35},size_hint=(0.87,0.15))
        self.add_widget(self.text_explanation_two)
#---third textbox (capital letters)
        self.text_input_three= TextInput(text=title_three,pos_hint={"center_x":0.5,"center_y": 0.22},size_hint=(0.87,0.08))
        self.add_widget(self.text_input_three)
#-- third explanation textbox
        self.text_explanation_three= TextInput(text=explanation_three,pos_hint={"center_x":0.5,"center_y": 0.1},size_hint=(0.87,0.15))
        self.add_widget(self.text_explanation_three)
# button to save all the info
        self.button= Button(text="Save All", size_hint=(0.1,0.1), pos_hint={"center_x":0.885, "center_y":0.88},on_press=lambda x:self.save_learning_notes(self.text_input_one.text,self.text_input_two.text,self.text_input_three.text,self.text_explanation_one.text,self.text_explanation_two.text,self.text_explanation_three.text,'text_files/learning_notes_one.txt','text_files/learning_notes_two.txt','text_files/learning_notes_three.txt'))
        self.add_widget(self.button)

#this is the reminders screen class
class Reminders_Screen(Screen):

    #the method to save all the reminders in the files
    def save_reminders(self,reminder_one,reminder_two,reminder_three,reminder_four,fileName_one,fileName_two,fileName_three,fileName_four):
        fob = open(fileName_one,'w')
        fob.write(reminder_one)
        fob.close()

        fob_two = open(fileName_two,'w')
        fob_two.write(reminder_two)
        fob_two.close()

        fob_three = open(fileName_three,'w')
        fob_three.write(reminder_three)
        fob_three.close()

        fob_four = open(fileName_four,'w')
        fob_four.write(reminder_four)
        fob_four.close()

    #the method to save all the dates in the files
    def save_date(self,date,fileName):
        fob = open(fileName,'w')
        fob.write(date)
        fob.close()

    #the method to read all the dates from the files
    def open_date(self,fileName):
        date = ""
        fob = open(fileName,'r')
        for line in fob.readlines():
            date += line
        return date

    #the method to read all the reminders from the files
    def open_reminder(self,fileName):
        reminder = ""
        fob = open(fileName,'r')
        for line in fob.readlines():
            reminder += line
        return reminder

    #the method to add the date
    def add_date(self,input,label,fileName):
        try:
            number_days =float(input.text)
            date_string =str(datetime.today()+timedelta(days=number_days))
            label.text = date_string[0:10]
            self.save_date(date_string[0:10],fileName)
        except ValueError as err:
            label.text = "Invalid value!"


    #the main method
    def __init__(self, **args):
        Screen.__init__(self, **args)

        #giving all the reminder and the dates values
        reminder_one = self.open_reminder('text_files/reminder_one.txt')
        reminder_two = self.open_reminder('text_files/reminder_two.txt')
        reminder_three = self.open_reminder('text_files/reminder_three.txt')
        reminder_four = self.open_reminder('text_files/reminder_four.txt')

        date_one = self.open_date('text_files/date_one.txt')
        date_two = self.open_date('text_files/date_two.txt')
        date_three = self.open_date('text_files/date_three.txt')
        date_four = self.open_date('text_files/date_four.txt')

        #Set reminder label
        self.label = Label(text="Set Reminders", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.5, "center_y":0.95})

        #adding all elements for the first reminder
        self.text_input_one= TextInput(text=reminder_one,pos_hint={"center_x":0.37,"center_y": 0.7},size_hint=(0.6,0.1))
        self.date_input_one = TextInput(pos_hint={"center_x":0.75,"center_y": 0.7},size_hint=(0.1,0.1))
        self.date_label_one = Label(text=date_one,pos_hint={"center_x":0.92,"center_y": 0.7},size_hint=(0.1,0.1))
        self.add_widget(self.date_input_one)
        self.add_widget(self.date_label_one)
        self.add_widget(self.text_input_one)
        self.set_date_one = Button(text="set",pos_hint={"center_x":0.82,"center_y": 0.7},size_hint=(0.05,0.1),on_press=lambda x:self.add_date(self.date_input_one,self.date_label_one,'text_files/date_one.txt'))
        self.add_widget(self.set_date_one)

        #adding all elements for the second reminder
        self.text_input_two= TextInput(text=reminder_two,pos_hint={"center_x":0.37,"center_y": 0.5},size_hint=(0.6,0.1))
        self.date_input_two = TextInput(pos_hint={"center_x":0.75,"center_y": 0.5},size_hint=(0.1,0.1))
        self.date_label_two = Label(text=date_two,pos_hint={"center_x":0.92,"center_y": 0.5},size_hint=(0.1,0.1))
        self.add_widget(self.date_input_two)
        self.add_widget(self.date_label_two)
        self.add_widget(self.text_input_two)
        self.set_date_two = Button(text="set",pos_hint={"center_x":0.82,"center_y": 0.5},size_hint=(0.05,0.1),on_press=lambda x:self.add_date(self.date_input_two,self.date_label_two,'text_files/date_two.txt'))
        self.add_widget(self.set_date_two)

        #adding all elements for the third reminder
        self.text_input_three= TextInput(text=reminder_three,pos_hint={"center_x":0.37,"center_y": 0.3},size_hint=(0.6,0.1))
        self.date_input_three = TextInput(pos_hint={"center_x":0.75,"center_y": 0.3},size_hint=(0.1,0.1))
        self.date_label_three = Label(text=date_three,pos_hint={"center_x":0.92,"center_y": 0.3},size_hint=(0.1,0.1))
        self.add_widget(self.date_input_three)
        self.add_widget(self.date_label_three)
        self.add_widget(self.text_input_three)
        self.set_date_three = Button(text="set",pos_hint={"center_x":0.82,"center_y": 0.3},size_hint=(0.05,0.1),on_press=lambda x:self.add_date(self.date_input_three,self.date_label_three,'text_files/date_three.txt'))
        self.add_widget(self.set_date_three)

        #adding all elements for the forth reminder
        self.text_input_four= TextInput(text=reminder_four,pos_hint={"center_x":0.37,"center_y": 0.1},size_hint=(0.6,0.1))
        self.date_input_four = TextInput(pos_hint={"center_x":0.75,"center_y": 0.1},size_hint=(0.1,0.1))
        self.date_label_four = Label(text=date_four,pos_hint={"center_x":0.92,"center_y": 0.1},size_hint=(0.1,0.1))
        self.add_widget(self.date_input_four)
        self.add_widget(self.date_label_four)
        self.add_widget(self.text_input_four)
        self.set_date_four = Button(text="set",pos_hint={"center_x":0.82,"center_y": 0.1},size_hint=(0.05,0.1),on_press=lambda x:self.add_date(self.date_input_four,self.date_label_four,'text_files/date_four.txt'))
        self.add_widget(self.set_date_four)

        #adding the save all button
        self.button= Button(text="Save All", size_hint=(0.1,0.1), pos_hint={"center_x":0.9, "center_y":0.88},on_press=lambda x:self.save_reminders(self.text_input_one.text,self.text_input_two.text,self.text_input_three.text,self.text_input_four.text,'text_files/reminder_one.txt','text_files/reminder_two.txt','text_files/reminder_three.txt','text_files/reminder_four.txt'))
        self.add_widget(self.button)
        self.add_widget(self.label)


#The goals class
class Goals_Screen(Screen):

    #method to save the goals in the files
    def save_goals(self,goal_one,goal_two,goal_three,goal_four,fileName_one,fileName_two,fileName_three,fileName_four):
        fob = open(fileName_one,'w')
        fob.write(goal_one)
        fob.close()

        fob_two = open(fileName_two,'w')
        fob_two.write(goal_two)
        fob_two.close()

        fob_three = open(fileName_three,'w')
        fob_three.write(goal_three)
        fob_three.close()

        fob_four = open(fileName_four,'w')
        fob_four.write(goal_four)
        fob_four.close()

    #method to get the goals from the files
    def open_goal(self,fileName):
        goal = ""
        fob = open(fileName,'r')
        for line in fob.readlines():
            goal += line
        return goal

    #method to add the goal progress
    def goal_progress(self,checkbox):
        if  checkbox.active:
            self.progressbar.value += 25
        else:
            self.progressbar.value -= 25

        if self.progressbar.value == 100:
            self.label.color = (0,1,0,1)
            self.label.font_size = 30
            self.label.text = "  Congratulations! Now go set new goals!"
        else:
            self.label.color=(1,0,0,1)
            self.label.font_size=(45)
            self.label.text = "Set your Goals"

    #main method of the goals class
    def __init__(self, **args):
        Screen.__init__(self, **args)
        #declaring the goals and giving them values
        goal_one = self.open_goal('text_files/goal_one.txt')
        goal_two = self.open_goal('text_files/goal_two.txt')
        goal_three = self.open_goal('text_files/goal_three.txt')
        goal_four = self.open_goal('text_files/goal_four.txt')



        #adding the progressbar
        self.progressbar = ProgressBar(value=0, max=100,size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y": 0.85})
        self.add_widget(self.progressbar)
        #label set your goals
        self.label = Label(text="Set your Goals", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.5, "center_y":0.95})

        #goal input one
        self.text_input_one= TextInput(text=goal_one,pos_hint={"center_x":0.4,"center_y": 0.7},size_hint=(0.7,0.1))
        self.checkbox_one = CheckBox(pos_hint={"center_x":0.9,"center_y": 0.7},size_hint=(0.1,0.1),on_press=lambda x:self.goal_progress(self.checkbox_one))
        self.add_widget(self.text_input_one)
        self.add_widget(self.checkbox_one)

        #goal input two
        self.text_input_two= TextInput(text=goal_two,pos_hint={"center_x":0.4,"center_y": 0.5},size_hint=(0.7,0.1))
        self.checkbox_two = CheckBox(pos_hint={"center_x":0.9,"center_y": 0.5},size_hint=(0.1,0.1),on_press=lambda x:self.goal_progress(self.checkbox_two))
        self.add_widget(self.text_input_two)
        self.add_widget(self.checkbox_two)

        #goal input three
        self.text_input_three= TextInput(text=goal_three,pos_hint={"center_x":0.4,"center_y": 0.3},size_hint=(0.7,0.1))
        self.checkbox_three = CheckBox(pos_hint={"center_x":0.9,"center_y": 0.3},size_hint=(0.1,0.1),on_press=lambda x:self.goal_progress(self.checkbox_three))
        self.add_widget(self.text_input_three)
        self.add_widget(self.checkbox_three)

        #goal input four
        self.text_input_four= TextInput(text=goal_four,pos_hint={"center_x":0.4,"center_y": 0.1},size_hint=(0.7,0.1))
        self.checkbox_four = CheckBox(pos_hint={"center_x":0.9,"center_y": 0.1},size_hint=(0.1,0.1),on_press=lambda x:self.goal_progress(self.checkbox_four))
        self.add_widget(self.text_input_four)
        self.add_widget(self.checkbox_four)

        self.add_widget(self.label)

        #button to save all the goals
        self.button= Button(text="Save All", size_hint=(0.1,0.1), pos_hint={"center_x":0.9, "center_y":0.88},on_press=lambda x:self.save_goals(self.text_input_one.text,self.text_input_two.text,self.text_input_three.text,self.text_input_four.text,'text_files/goal_one.txt','text_files/goal_two.txt','text_files/goal_three.txt','text_files/goal_four.txt'))
        self.add_widget(self.button)


#The other notes class
class Other_Notes_Screen(Screen):

    #method to save the other notes in the files
    def save_other_notes(self,other_notes,fileName):
        fob = open(fileName,'w')
        fob.write(other_notes)
        fob.close()

    #method to get the other notes from the files
    def open_other_notes(self,fileName):
        notes = ""
        fob = open(fileName,'r')
        for line in fob.readlines():
            notes += line
        return notes
    #main method of the other notes
    def __init__(self, **args):
        Screen.__init__(self, **args)

        #give value to other notes
        notes= self.open_other_notes('text_files/other_notes.txt')

        #all other notes inputs
        self.textLabel = Label(text="Other Notes", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.53, "center_y":0.9})
        self.text_input= TextInput(text=notes,pos_hint={"center_x":0.515,"center_y": 0.4},size_hint=(0.9,0.8),scroll_y=100)
        self.add_widget(self.textLabel)
        self.add_widget(self.text_input)

        #the button to save all other notes
        self.button= Button(text="Save All", size_hint=(0.1,0.1), pos_hint={"center_x":0.91, "center_y":0.88},on_press=lambda x:self.save_other_notes(self.text_input.text,'text_files/other_notes.txt'))
        self.add_widget(self.button)



#The calculator class
class Calculator_Screen(Screen):

    #main method of calculator class
    def __init__(self, **args):
        number_result =  0
        Screen.__init__(self, **args)

        #add labels to the calculator class
        self.label = Label(text="Calculator", color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.55, "center_y":0.95})
        self.labelText = Label(text=str(number_result), color=(1,0,0,1), font_size=(45),size_hint=(0.1,0.1), pos_hint={"center_x":0.55, "center_y":0.1})
        self.labelSign = Label(text= "Sign", color=(1,1,1,1), font_size=(16),size_hint=(0.1,0.1), pos_hint={"center_x":0.55, "center_y":0.835})
        self.add_widget(self.label)
        self.add_widget(self.labelText)
        self.add_widget(self.labelSign)

    #add method of the class
    def adding(self, number_one,number_two):
        try:
            number_result = float(number_one) + float(number_two)
            self.labelText.text = str(number_result)
            self.labelSign.text = "+"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")

    #subtract method of the class
    def subtracting(self,number_one,number_two):
        try:
            number_result = float(number_one) - float(number_two)
            self.labelText.text = str(number_result)
            self.labelSign.text = "-"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")

    #multiply method of the class
    def multiplication(self,number_one,number_two):
        try:
            number_result = float(number_one) * float(number_two)
            self.labelText.text = str(number_result)
            self.labelSign.text = "*"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")

    #divide method of the class
    def division(self,number_one,number_two):
        try:
            number_result = float(number_one) / float(number_two)
            self.labelText.text = str(number_result)
            self.labelSign.text = "/"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")
        except ZeroDivisionError as er:
            self.labelText.text = "No Zero Division"
    #power method of the class
    def power(self,number_one,number_two):
        try:
            number_result = float(number_one) ** float(number_two)
            self.labelText.text = str(number_result)
            self.labelSign.text = "^"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")

    #inverse power method of the class
    def powerInverse(self,number_one,number_two):
        try:
            number_result = float(number_two) ** (1/float(number_one))
            self.labelText.text = str(number_result)
            self.labelSign.text = "√"
            print(number_result)
        except ValueError as err:
            self.labelText.text = "Add correct values to continue!"
            print("Please add both values to continue")
        except ZeroDivisionError as er:
            self.labelText.text = "No Zero Division"
# Create the screen manager
sm = ScreenManager()
sm.add_widget(Main_Screen(name='main_screen'))
sm.add_widget(New_Ideas_Screen(name='new_ideas_screen'))
sm.add_widget(Learning_Notes_Screen(name='learning_notes_screen'))
sm.add_widget(Reminders_Screen(name='reminders_screen'))
sm.add_widget(Goals_Screen(name='goals_screen'))
sm.add_widget(Other_Notes_Screen(name='other_notes_screen'))
sm.add_widget(Calculator_Screen(name='calculator_screen'))

#the main class to build everything
class TestApp(App):

    def build(self):
        return sm

#run the app
if __name__ == '__main__':
    TestApp().run()
