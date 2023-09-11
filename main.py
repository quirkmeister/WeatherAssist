from bs4 import BeautifulSoup

import requests

file = open('result.txt', 'w')

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

url = "http://www.accuweather.com/en/us/new-york-ny/10007/weather-forecast/349727"
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

target_span = soup.find('span', class_="label", string="Air Quality")
wind_span = soup.find('span', class_="label", string="Wind")

next_span = target_span.find_next_sibling('span')
wind_next_span = wind_span.findNextSibling('span')

temp = soup.find('div', class_="temp")
real_temp = temp.text
temper = real_temp.strip('C')

file.writelines(["Air Quality : "+ str(next_span.string), "\nWind : " + str(wind_next_span.string
), "\nTemperature : " + temper])



print(temper)