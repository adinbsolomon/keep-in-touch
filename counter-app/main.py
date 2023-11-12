
import logging

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout

class CounterApp(MDApp):

    def build(self):
        self.set_colors()
        return self.set_up_widgets()
        
    def set_colors(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

    def set_up_widgets(self):
        self.screen = MDScreen()
        self.button = MDRectangleFlatButton(
            text = "hello world",
            on_release = self.button_press
        )
        self._counter = 0
        self.label = MDLabel(text = str(self._counter))
        self.screen.add_widget(self.button)
        self.screen.add_widget(self.label)
        return self.screen

    def button_press(self, _):
        self._counter += 1
        self.label.text = str(self._counter)


if __name__ == "__main__":
    CounterApp().run()
