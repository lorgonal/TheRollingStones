import http.client
import json
import ssl
import urllib.parse as parse
from config import API_TOKEN


HOST = 'weather.visualcrossing.com'


def get_weather(location):
    location=parse.quote(location)
    conn = http.client.HTTPSConnection(HOST,context = ssl._create_unverified_context())

    query_data = f'/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={API_TOKEN}&&contentType=json'
    conn.request("GET", query_data)

    res = conn.getresponse()
    data = res.read()
    # print(data.decode('UTF-8'))
    return json.loads(data.decode("utf-8"))








