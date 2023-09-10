from kivy.extras.highlight import KivyLexer
from kivy.uix.button import Button

from kivy.app import App

from kivy.uix.codeinput import CodeInput
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.html import HtmlLexer

from kivy.core.window import Window
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

_fixed_size = (640, 480)

def reSize(*args):
   Window.size = _fixed_size
   return True
Window.bind(on_resize = reSize)

class MyApp(App):
    def build(self):
        s = Scatter()
        f1 = FloatLayout(size = (300, 300))
        s.add_widget(f1)
        f1.add_widget(Button(
            text = 'This is my button',
            font_size = 16,
            on_press = self.btn_press,
            background_color = [.32, .85, .94, 1],
            background_normal = '',
            size_hint = (.5, .25),
            pos = (640 / 2 - 160, 480 / 2 - (480 * .25 / 2)),
        ))
        return s
    def btn_press(self, instance):
        print('The Button is on press')
        instance.text = 'Im on press'


if __name__ == '__main__':
    MyApp().run()
