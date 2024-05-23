# importing library
import requests
from bs4 import BeautifulSoup
import webbrowser

def search(query):
    link_list =[]
    # creating url and requests instance
    url = "https://www.google.com/search?q="+query
    webbrowser.open(url)
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        link_list.append({link.text:link.get('href')})

    for i in link_list:
        if 'chatgpt' in i :
            print(i)

    # print(soup)
    # target_div = soup.find('div', class_='yuRUbf')

    # if target_div:
    #     # Find the first <a> tag within the specific <div>
    #     link = target_div.find('a')

    #     if link and 'href' in link.attrs:
    #         # Print the href attribute of the link
    #         print(f"Found link: {link['href']}")
    #     else:
    #         print("No link found in the target div.")
    # else:
    #     print("Target div not found.")

# query = input("Search : ")
search("chat gpt")