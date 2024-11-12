from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text=" ", font_size='20sp')
        self.add_widget(self.label)
        self.text_input = TextInput(hint_text="Enter text", multiline=False)
        self.add_widget(self.text_input)
        self.button = Button(text="Submit", size_hint=(1, 0.5))
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.label.text = f" {self.text_input.text}"
        self.text_input.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
