import requests


def get_wind(lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=6ece76affa411be60affa4ee66ee2d62&units=imperial"
        response = requests.get(url)
        x = response.json()
        if x["cod"] != "404":
            name = x["name"]
            wind = float(x["wind"]["speed"] * 0.869)
            try:
                windgust = float(x["wind"]["gust"] * 0.869)
            except KeyError:
                windgust = None
            winddirection = None
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
            return wind, windgust, winddirection, name
    except requests.ConnectionError:
        return "No Internet Connection"


def wingcalculator(wind, weight, skill, style):
    if weight <= 74:
        return "Rider's weight is below minimum value"
    if weight >= 251:
        return "Rider's Weight is above maximum value"
    if skill:
        if wind <= 13.9:
            return "Wind speed is below recommend level for beginners"
        if wind >= 21:
            return "Wind speed is above recommend level for beginners"
        elif 14 <= wind <= 20 and 75 <= weight <= 99 and style:
            return "3-4 meter wing recommended"
        elif 14 <= wind <= 20 and 75 <= weight <= 99:
            return "5 meter wing recommended"
        elif 14 <= wind <= 20 and 100 <= weight <= 124 and style:
            return "4 meter wing recommended"
        elif 14 <= wind <= 20 and 100 <= weight <= 124:
            return "5 meter wing recommended"
        elif 14 <= wind <= 20 and 125 <= weight <= 149 and style:
            return "4-5 meter wing recommended"
        elif 14 <= wind <= 20 and 125 <= weight <= 149:
            return "6 meter wing recommended"
        elif 14 <= wind <= 20 and 150 <= weight <= 174 and style:
            return "5-6 meter wing recommended"
        elif 14 <= wind <= 20 and 150 <= weight <= 174:
            return "7 meter wing recommended"
        elif 14 <= wind <= 20 and 175 <= weight <= 199 and style:
            return "6 meter wing recommended"
        elif 14 <= wind <= 20 and 175 <= weight <= 199:
            return "7 meter wing recommended"
        elif 14 <= wind <= 20 and 200 <= weight <= 250 and style:
            return "7 meter wing recommended"
        elif 14 <= wind <= 20 and 200 <= weight <= 250:
            return "8 meter wing recommended"
    if wind <= 9.99:
        return "Wind speed is below recommend levels"
    if wind >= 33.1:
        return "Wind speed is above recommend levels"
    elif 10 <= wind <= 14.9 and 75 <= weight <= 99 and style:
        return "3 meter wing recommended"
    elif 10 <= wind <= 14.9 and 75 <= weight <= 99:
        return "4 meter wing recommended"
    elif 10 <= wind <= 14.9 and 100 <= weight <= 124 and style:
        return "4 meter wing recommended"
    elif 10 <= wind <= 14.9 and 100 <= weight <= 124:
        return "5 meter wing recommended"
    elif 10 <= wind <= 14.9 and 125 <= weight <= 149 and style:
        return "4 meter wing recommended"
    elif 10 <= wind <= 14.9 and 125 <= weight <= 149:
        return "5 meter wing recommended"
    elif 10 <= wind <= 14.9 and 150 <= weight <= 174 and style:
        return "5 meter wing recommended"
    elif 10 <= wind <= 14.9 and 150 <= weight <= 174:
        return "6 meter wing recommended"
    elif 10 <= wind <= 14.9 and 175 <= weight <= 199 and style:
        return "5-6 meter wing recommended"
    elif 10 <= wind <= 14.9 and 175 <= weight <= 199:
        return "7 meter wing recommended"
    elif 10 <= wind <= 14.9 and 200 <= weight <= 224 and style:
        return "6 meter wing recommended"
    elif 10 <= wind <= 14.9 and 200 <= weight <= 224:
        return "7 meter wing recommended"
    elif 10 <= wind <= 14.9 and 225 <= weight <= 250 and style:
        return "7 meter wing recommended"
    elif 10 <= wind <= 14.9 and 225 <= weight <= 250:
        return "8 meter wing recommended"
    elif 15 <= wind <= 19.9 and 75 <= weight <= 99 and style:
        return "2 meter wing recommended"
    elif 15 <= wind <= 19.9 and 75 <= weight <= 99:
        return "3 meter wing recommended"
    elif 15 <= wind <= 19.9 and 100 <= weight <= 124 and style:
        return "3 meter wing recommended"
    elif 15 <= wind <= 19.9 and 100 <= weight <= 124:
        return "4 meter wing recommended"
    elif 15 <= wind <= 19.9 and 125 <= weight <= 149 and style:
        return "4 meter wing recommended"
    elif 15 <= wind <= 19.9 and 125 <= weight <= 149:
        return "5 meter wing recommended"
    elif 15 <= wind <= 19.9 and 150 <= weight <= 174 and style:
        return "4 meter wing recommended"
    elif 15 <= wind <= 19.9 and 150 <= weight <= 174:
        return "5 meter wing recommended"
    elif 15 <= wind <= 19.9 and 175 <= weight <= 199 and style:
        return "5 meter wing recommended"
    elif 15 <= wind <= 19.9 and 175 <= weight <= 199:
        return "6 meter wing recommended"
    elif 15 <= wind <= 19.9 and 200 <= weight <= 224 and style:
        return "5 meter wing recommended"
    elif 15 <= wind <= 19.9 and 200 <= weight <= 224:
        return "6 meter wing recommended"
    elif 15 <= wind <= 19.9 and 225 <= weight <= 250 and style:
        return "6 meter wing recommended"
    elif 15 <= wind <= 19.9 and 225 <= weight <= 250:
        return "7 meter wing recommended"
    elif 20 <= wind <= 24.9 and 75 <= weight <= 99 and style:
        return "2 meter wing recommended"
    elif 20 <= wind <= 24.9 and 75 <= weight <= 99:
        return "3 meter wing recommended"
    elif 20 <= wind <= 24.9 and 100 <= weight <= 124 and style:
        return "3 meter wing recommended"
    elif 20 <= wind <= 24.9 and 100 <= weight <= 124:
        return "4 meter wing recommended"
    elif 20 <= wind <= 24.9 and 125 <= weight <= 149 and style:
        return "3 meter wing recommended"
    elif 20 <= wind <= 24.9 and 125 <= weight <= 149:
        return "4 meter wing recommended"
    elif 20 <= wind <= 24.9 and 150 <= weight <= 174 and style:
        return "4 meter wing recommended"
    elif 20 <= wind <= 24.9 and 150 <= weight <= 174:
        return "5 meter wing recommended"
    elif 20 <= wind <= 24.9 and 175 <= weight <= 199 and style:
        return "4 meter wing recommended"
    elif 20 <= wind <= 24.9 and 175 <= weight <= 199:
        return "5 meter wing recommended"
    elif 20 <= wind <= 24.9 and 200 <= weight <= 224 and style:
        return "5 meter wing recommended"
    elif 20 <= wind <= 24.9 and 200 <= weight <= 224:
        return "6 meter wing recommended"
    elif 20 <= wind <= 24.9 and 225 <= weight <= 250 and style:
        return "5 meter wing recommended"
    elif 20 <= wind <= 24.9 and 225 <= weight <= 250:
        return "6 meter wing recommended"
    elif 25 <= wind <= 27.9 and 75 <= weight <= 99 and style:
        return "1 meter wing recommended"
    elif 25 <= wind <= 27.9 and 75 <= weight <= 99:
        return "2 meter wing recommended"
    elif 25 <= wind <= 27.9 and 100 <= weight <= 124 and style:
        return "2 meter wing recommended"
    elif 25 <= wind <= 27.9 and 100 <= weight <= 124:
        return "3 meter wing recommended"
    elif 25 <= wind <= 27.9 and 125 <= weight <= 149 and style:
        return "2 meter wing recommended"
    elif 25 <= wind <= 27.9 and 125 <= weight <= 149:
        return "3 meter wing recommended"
    elif 25 <= wind <= 27.9 and 150 <= weight <= 174 and style:
        return "3 meter wing recommended"
    elif 25 <= wind <= 27.9 and 150 <= weight <= 174:
        return "4 meter wing recommended"
    elif 25 <= wind <= 27.9 and 175 <= weight <= 199 and style:
        return "3 meter wing recommended"
    elif 25 <= wind <= 27.9 and 175 <= weight <= 199:
        return "4 meter wing recommended"
    elif 25 <= wind <= 27.9 and 200 <= weight <= 224 and style:
        return "4 meter wing recommended"
    elif 25 <= wind <= 27.9 and 200 <= weight <= 224:
        return "5 meter wing recommended"
    elif 25 <= wind <= 27.9 and 225 <= weight <= 250 and style:
        return "4 meter wing recommended"
    elif 25 <= wind <= 27.9 and 225 <= weight <= 250:
        return "5 meter wing recommended"
    elif 28 <= wind <= 33 and 75 <= weight <= 99 and style:
        return "1 meter wing recommended"
    elif 28 <= wind <= 33 and 75 <= weight <= 99:
        return "2 meter wing recommended"
    elif 28 <= wind <= 33 and 100 <= weight <= 124 and style:
        return "1 meter wing recommended"
    elif 28 <= wind <= 33 and 100 <= weight <= 124:
        return "2 meter wing recommended"
    elif 28 <= wind <= 33 and 125 <= weight <= 149 and style:
        return "2 meter wing recommended"
    elif 28 <= wind <= 33 and 125 <= weight <= 149:
        return "3 meter wing recommended"
    elif 28 <= wind <= 33 and 150 <= weight <= 174 and style:
        return "2 meter wing recommended"
    elif 28 <= wind <= 33 and 150 <= weight <= 174:
        return "3 meter wing recommended"
    elif 28 <= wind <= 33 and 175 <= weight <= 199 and style:
        return "2 meter wing recommended"
    elif 28 <= wind <= 33 and 175 <= weight <= 199:
        return "3 meter wing recommended"
    elif 28 <= wind <= 33 and 200 <= weight <= 224 and style:
        return "3 meter wing recommended"
    elif 28 <= wind <= 33 and 200 <= weight <= 224:
        return "4 meter wing recommended"
    elif 28 <= wind <= 33 and 225 <= weight <= 250 and style:
        return "3 meter wing recommended"
    elif 28 <= wind <= 33 and 225 <= weight <= 250:
        return "4 meter wing recommended"


wind = round(get_wind("38.719489", "-90.478666")[0], 2)
if get_wind("38.719489", "-90.478666")[1] is not None:
    windgust = round(get_wind("38.719489", "-90.478666")[1], 2)
else:
    windgust = None
winddirection = get_wind("38.719489", "-90.478666")[2]
name = get_wind("38.719489", "-90.478666")[3]

# print(wingcalculator(wind, 170, False, False))
print(wingcalculator(wind, 170, False, False))

if windgust is not None and windgust > (wind * 1.75):
    print(f"At {name} the wind speed is {wind} kts with gusts of {windgust} kts at a direction of {winddirection}."
          f"\n*Wind gust warning. Recommend using less power setting")
elif windgust is not None:
    print(f"At {name} the wind speed is {wind} kts with gusts of {windgust} kts at a direction of {winddirection}.")
else:
    print(f"At {name} the wind speed is {wind} kts with a direction of {winddirection}.")