# importing library
import requests
from bs4 import BeautifulSoup
import webbrowser


def get_weather_report():
    city = "kolkata"

    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city
    webbrowser.open(url)
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all data
    
    return f"{city} Weather Informatio\n temperature is {temp} \n, time {time} \n Sky Description {sky}"
