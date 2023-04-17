from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
'''


class WingCalculatorApp(MDApp):
    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'
        # Initialize GPS
        GpsHelper().run()

    def calculateWingSize(self):
