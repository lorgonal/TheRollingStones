from WeatherAPIHandler import get_weather

dic=get_weather('granada españa')
print(f'input: {dic["address"]}')
print(f'resolved: {dic["resolvedAddress"]}')
print(f'timezone: {dic["timezone"]}')
for day in dic['days']:
    print(f'date: {day["datetime"]}, max temp: {day["tempmax"]}, min temp: {day["tempmin"]}')