#News Article specific reader

#import nltk 
#from nltk import send_tokenize
#from nltk import word_tokenize
import requests
from bs4 import BeautifulSoup
from newspaper import Article

def news():
    #target we want to open 
    url = 'https://www.cnn.com/travel/article/qantas-california-desert-a380s-rattlesnakes/index.html'

    #open with GET method
    resp = requests.get(url)
    #http_respone 200 means link works
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("the news are as follow :-\n")

        article = Article(url)
        article.download()

        article.parse()
        article.nlp()
        text = article.text

        print (type(text))
        print("\n")

        print(text)
        print("\n")
        print(len(text))
        print(article.keywords)
        
    else:
        print("Error")
news()



