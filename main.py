import requests
from kivy.utils import platform
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from plyer import gps

Window.size = (350, 600)

kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    MDLabel:
        text: "WingCalculator"
        pos_hint: {"center_x": .5, "center_y": .89}
        halign: "center"
        font_size: "20sp"        
'''


class WingCalculatorApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.winddirection = None
        self.windgust = None
        self.wind = None
        self.lon = None
        self.lat = None

    def build(self):
        return Builder.load_string(kv)

    def runGPS(self):
        if platform == 'android':
            from android.permissions import Permission, request_permissions

            def callback(permission, results):
                if all([res for res in results]):
                    print("Permissions granted")
                else:
                    print("Permissions denied")

            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)

        gps.configure(on_location=self.gps_location, on_status=self.on_auth_status)
        gps.start(minTime=1000, minDistance=0)

    def gps_location(self, *args, **kwargs):
        self.lat = kwargs['lat']
        self.lon = kwargs['long']
        print(f"GPS position {self.lat}, {self.lon}")
        return self.lat, self.lon

    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()

    def open_gps_access_popup(self):
        dialog = MDDialog(title="GPS Error", text="Please enable GPS access")
        dialog.size_hint = [.8, .8]
        dialog.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog.open()

    def get_wind(self):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=6ece76affa411be60affa4ee66ee2d62&units=imperial"
            response = requests.get(url)
            x = response.json()
            if x["cod"] != "404":
                self.name = x["name"]
                self.wind = float(x["wind"]["speed"] * 0.869)
                try:
                    self.windgust = float(x["wind"]["gust"] * 0.869)
                except KeyError:
                    self.windgust = None
                self.winddirection = None
                degrees = float(x["wind"]["deg"])
                if degrees >= 348.75 or degrees <= 33.74:
                    winddirection = "North"
                elif 33.75 <= degrees <= 78.74:
                    winddirection = "Northeast"
                elif 75.75 <= degrees <= 123.74:
                    winddirection = "East"
                elif 123.75 <= degrees <= 168.74:
                    winddirection = "Southeast"
                elif 168.75 <= degrees <= 213.74:
                    winddirection = "South"
                elif 213.75 <= degrees <= 258.74:
                    winddirection = "Southwest"
                elif 258.75 <= degrees <= 303.74:
                    winddirection = "West"
                elif 303.75 <= degrees <= 348.74:
                    winddirection = "Northwest"
                return self.wind, self.windgust, self.winddirection, self.name
        except requests.ConnectionError:
            return "No Internet Connection"

    def wingcalculator(self, weight, skill, style):
        if weight <= 74:
            return "Rider's weight is below minimum value"
        if weight >= 251:
            return "Rider's Weight is above maximum value"
        if skill:
            if self.wind <= 13.9:
                return "Wind speed is below recommend level for beginners"
            if self.wind >= 21:
                return "Wind speed is above recommend level for beginners"
            elif 14 <= self.wind <= 20 and 75 <= weight <= 99 and style:
                return "3-4 meter wing recommended"
            elif 14 <= self.wind <= 20 and 75 <= weight <= 99:
                return "5 meter wing recommended"
            elif 14 <= self.wind <= 20 and 100 <= weight <= 124 and style:
                return "4 meter wing recommended"
            elif 14 <= self.wind <= 20 and 100 <= weight <= 124:
                return "5 meter wing recommended"
            elif 14 <= self.wind <= 20 and 125 <= weight <= 149 and style:
                return "4-5 meter wing recommended"
            elif 14 <= self.wind <= 20 and 125 <= weight <= 149:
                return "6 meter wing recommended"
            elif 14 <= self.wind <= 20 and 150 <= weight <= 174 and style:
                return "5-6 meter wing recommended"
            elif 14 <= self.wind <= 20 and 150 <= weight <= 174:
                return "7 meter wing recommended"
            elif 14 <= self.wind <= 20 and 175 <= weight <= 199 and style:
                return "6 meter wing recommended"
            elif 14 <= self.wind <= 20 and 175 <= weight <= 199:
                return "7 meter wing recommended"
            elif 14 <= self.wind <= 20 and 200 <= weight <= 250 and style:
                return "7 meter wing recommended"
            elif 14 <= self.wind <= 20 and 200 <= weight <= 250:
                return "8 meter wing recommended"
        if self.wind <= 9.99:
            return "Wind speed is below recommend levels"
        if self.wind >= 33.1:
            return "Wind speed is above recommend levels"
        elif 10 <= self.wind <= 14.9 and 75 <= weight <= 99 and style:
            return "3 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 75 <= weight <= 99:
            return "4 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 100 <= weight <= 124 and style:
            return "4 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 100 <= weight <= 124:
            return "5 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 125 <= weight <= 149 and style:
            return "4 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 125 <= weight <= 149:
            return "5 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 150 <= weight <= 174 and style:
            return "5 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 150 <= weight <= 174:
            return "6 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 175 <= weight <= 199 and style:
            return "5-6 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 175 <= weight <= 199:
            return "7-8 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 200 <= weight <= 224 and style:
            return "6 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 200 <= weight <= 224:
            return "7-8 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 225 <= weight <= 250 and style:
            return "7 meter wing recommended"
        elif 10 <= self.wind <= 14.9 and 225 <= weight <= 250:
            return "8 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 75 <= weight <= 99 and style:
            return "2 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 75 <= weight <= 99:
            return "3 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 100 <= weight <= 124 and style:
            return "3 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 100 <= weight <= 124:
            return "4 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 125 <= weight <= 149 and style:
            return "4 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 125 <= weight <= 149:
            return "5 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 150 <= weight <= 174 and style:
            return "4 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 150 <= weight <= 174:
            return "5 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 175 <= weight <= 199 and style:
            return "5 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 175 <= weight <= 199:
            return "6 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 200 <= weight <= 224 and style:
            return "5 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 200 <= weight <= 224:
            return "6 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 225 <= weight <= 250 and style:
            return "6 meter wing recommended"
        elif 15 <= self.wind <= 19.9 and 225 <= weight <= 250:
            return "7 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 75 <= weight <= 99 and style:
            return "2 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 75 <= weight <= 99:
            return "3 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 100 <= weight <= 124 and style:
            return "3 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 100 <= weight <= 124:
            return "4 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 125 <= weight <= 149 and style:
            return "3 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 125 <= weight <= 149:
            return "4 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 150 <= weight <= 174 and style:
            return "4 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 150 <= weight <= 174:
            return "5 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 175 <= weight <= 199 and style:
            return "4 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 175 <= weight <= 199:
            return "5 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 200 <= weight <= 224 and style:
            return "5 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 200 <= weight <= 224:
            return "6 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 225 <= weight <= 250 and style:
            return "5 meter wing recommended"
        elif 20 <= self.wind <= 24.9 and 225 <= weight <= 250:
            return "6 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 75 <= weight <= 99 and style:
            return "1 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 75 <= weight <= 99:
            return "2 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 100 <= weight <= 124 and style:
            return "2 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 100 <= weight <= 124:
            return "3 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 125 <= weight <= 149 and style:
            return "2 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 125 <= weight <= 149:
            return "3 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 150 <= weight <= 174 and style:
            return "3 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 150 <= weight <= 174:
            return "4 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 175 <= weight <= 199 and style:
            return "3 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 175 <= weight <= 199:
            return "4 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 200 <= weight <= 224 and style:
            return "4 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 200 <= weight <= 224:
            return "5 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 225 <= weight <= 250 and style:
            return "4 meter wing recommended"
        elif 25 <= self.wind <= 27.9 and 225 <= weight <= 250:
            return "5 meter wing recommended"
        elif 28 <= self.wind <= 33 and 75 <= weight <= 99 and style:
            return "1 meter wing recommended"
        elif 28 <= self.wind <= 33 and 75 <= weight <= 99:
            return "2 meter wing recommended"
        elif 28 <= self.wind <= 33 and 100 <= weight <= 124 and style:
            return "1 meter wing recommended"
        elif 28 <= self.wind <= 33 and 100 <= weight <= 124:
            return "2 meter wing recommended"
        elif 28 <= self.wind <= 33 and 125 <= weight <= 149 and style:
            return "2 meter wing recommended"
        elif 28 <= self.wind <= 33 and 125 <= weight <= 149:
            return "3 meter wing recommended"
        elif 28 <= self.wind <= 33 and 150 <= weight <= 174 and style:
            return "2 meter wing recommended"
        elif 28 <= self.wind <= 33 and 150 <= weight <= 174:
            return "3 meter wing recommended"
        elif 28 <= self.wind <= 33 and 175 <= weight <= 199 and style:
            return "2 meter wing recommended"
        elif 28 <= self.wind <= 33 and 175 <= weight <= 199:
            return "3 meter wing recommended"
        elif 28 <= self.wind <= 33 and 200 <= weight <= 224 and style:
            return "3 meter wing recommended"
        elif 28 <= self.wind <= 33 and 200 <= weight <= 224:
            return "4 meter wing recommended"
        elif 28 <= self.wind <= 33 and 225 <= weight <= 250 and style:
            return "3 meter wing recommended"
        elif 28 <= self.wind <= 33 and 225 <= weight <= 250:
            return "4 meter wing recommended"


if __name__ == '__main__':
    WingCalculatorApp().run()
