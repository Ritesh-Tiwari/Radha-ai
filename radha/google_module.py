# importing library
import requests
from bs4 import BeautifulSoup
import webbrowser

def search(query):

    # creating url and requests instance
    url = "https://www.google.com/search?q="+query
    # webbrowser.open(url)
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    target_div = soup.find('div', class_='yuRUbf')

    if target_div:
        # Find the first <a> tag within the specific <div>
        link = target_div.find('a')

        if link and 'href' in link.attrs:
            # Print the href attribute of the link
            print(f"Found link: {link['href']}")
        else:
            print("No link found in the target div.")
    else:
        print("Target div not found.")


search("what is chatgpt")