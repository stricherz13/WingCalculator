import requests
from kivy.utils import platform
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from plyer import gps

KV = '''
MDScreen:

    MDRectangleFlatButton:
        text: "Hello, World"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class WingCalculatorApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.winddirection = None
        self.windgust = None
        self.wind = None
        # self.name = None
        self.lon = None
        self.lat = None

    def flip(self):
        print("working...")

    def build(self):
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDTopAppBar(title="Wing Calculator")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # Logo
        screen.add_widget(Image(source="wingman.jpg", pos_hint={"center_x": 0.5, "center_y": 0.5}))

        # Input fields
        self.weight = MDTextField(
            text="Enter your weight in pounds",
            halign="left",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.25, "center_y": 0.75},
            font_size=20
        )
        screen.add_widget(self.weight)

        # Calculate button
        screen.add_widget(MDFillRoundFlatButton(
            text="Calculate",
            font_size=26,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.flip
        ))

        return screen

    # def on_start(self):
    #     self.runGPS()
    #     self.get_wind()

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
                self.wind = round(float(x["wind"]["speed"] * 0.869), 2)
                try:
                    self.windgust = round(float(x["wind"]["gust"] * 0.869), 2)
                except KeyError:
                    self.windgust = None
                degrees = float(x["wind"]["deg"])
                if degrees >= 348.75 or degrees <= 33.74:
                    self.winddirection = "North"
                elif 33.75 <= degrees <= 78.74:
                    self.winddirection = "Northeast"
                elif 75.75 <= degrees <= 123.74:
                    self.winddirection = "East"
                elif 123.75 <= degrees <= 168.74:
                    self.winddirection = "Southeast"
                elif 168.75 <= degrees <= 213.74:
                    self.winddirection = "South"
                elif 213.75 <= degrees <= 258.74:
                    self.winddirection = "Southwest"
                elif 258.75 <= degrees <= 303.74:
                    self.winddirection = "West"
                elif 303.75 <= degrees <= 348.74:
                    self.winddirection = "Northwest"
                return self.wind, self.winddirection, self.windgust
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
            return "7 meter wing recommended"
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

    def get_recommendation(self):
        if self.windgust is not None and self.windgust > (self.wind * 1.75):
            print(f"At {self.name} the wind speed is {self.wind} kts with gusts of {self.windgust} kts at a direction "
                  f"of {self.winddirection}."
                  f"\n*Wind gust warning. Recommend using less power setting")
        elif self.windgust is not None:
            print(f"At {self.name} the wind speed is {self.wind} kts with gusts of {self.windgust} kts at a direction "
                  f"of {self.winddirection}.")
        else:
            print(f"At {self.name} the wind speed is {self.wind} kts with a direction of {self.winddirection}.")


if __name__ == '__main__':
    WingCalculatorApp().run()
