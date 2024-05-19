# importing requests package
import requests	 
from output_module import output
from internet import check_internet_connection

def get_news():
    if check_internet_connection():
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "36d926210c6e4011a09ff7f8f2aff9ac"
        }
        main_url = " https://newsapi.org/v1/articles"

        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will 
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            
            # printing all trending news
            output(str(i + 1) +" "+ str(results[i]))
        return "so these are the top news from today"
    
    else:
        output ("Please check your internet conection")
        
