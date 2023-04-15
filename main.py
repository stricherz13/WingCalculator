from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from plyer import gps

kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
'''


class WingCalculatorApp(MDApp):
    def on_start(self):
        gps.configure(on_location=self.on_gps_location)
        gps.start()

    def on_gps_location(self, **kwargs):
        kwargs['lat'] = 10.0
        kwargs['lon'] = 10.0
        print(kwargs)

    def calculateWingSize(self):
