import requests


def get_wind(lat, lon, ):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=6ece76affa411be60affa4ee66ee2d62&units=imperial"
        response = requests.get(url)
        x = response.json()
        if x["cod"] != "404":
            wind = float(x["wind"]["speed"] * 0.869)
            windgust = float(x["wind"]["gust"] * 0.869)
            winddirection = None
            degrees = float(x["wind"]["deg"])
            if degrees >= 348.75 or degrees <= 33.74:
                winddirection = "N"
            elif 33.75 <= degrees <= 78.74:
                winddirection = "NE"
            elif 75.75 <= degrees <= 123.74:
                winddirection = "E"
            elif 123.75 <= degrees <= 168.74:
                winddirection = "SE"
            elif 168.75 <= degrees <= 213.74:
                winddirection = "S"
            elif 213.75 <= degrees <= 258.74:
                winddirection = "SW"
            elif 258.75 <= degrees <= 303.74:
                winddirection = "W"
            elif 303.75 <= degrees <= 348.74:
                winddirection = "NW"
            return wind, windgust, winddirection
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
    if wind <= 9.9:
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


wind = round(get_wind("38.721089", "-90.479698")[0], 2)
windgust = round(get_wind("38.721089", "-90.479698")[1], 2)
winddirection = get_wind("38.721089", "-90.479698")[2]

# print(wingcalculator(wind, 170, False, False))
print(wingcalculator(wind, 210, True, False))

print(
    f"At your current location the wind speed is {wind} kts with gusts {windgust} kts with a direction of {winddirection}.")
