#News Article specific reader

#import nltk 
#from nltk import send_tokenize
#from nltk import word_tokenize
import requests
import newspaper
from bs4 import BeautifulSoup as bs
from newspaper import Article

def news():
    #target we want to open 
    url = 'https://www.cnn.com'
    
    papertest = newspaper.build(url)

    for article in papertest.articles:
        print(article.url)


    #open with GET method
    resp = requests.get(url)
    #http_respone 200 means link works
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("the news are as follow :-\n")

    #    article = Article(url)
    #    article.download()

    #    article.parse()
    #    article.nlp()
    #    text = article.text

    #    print (type(text))
    #    print("\n")

    #    print(text)
    #    print("\n")
    #    print(len(text))
    #    print(article.keywords)
        
    else:
        print("Error")
#news()


def news2():
    #url = 'https://www.cnn.com/politics'
    url = 'https://www.foxnews.com/politics'
    #open with GET method
    resp = requests.get(url)

    soup = bs(resp.text, 'html.parser')
    rawtext = soup.get_text()

    #http_respone 200 means link works
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("the news are as follow :-\n")
        for link in soup.find_all('a'):
            print(link.get('href'))
    
    else:
        print("Error")



news2()
