
import requests
from bs4 import BeautifulSoup
import random
import os


def show_tags():
    tags = ["love", "inspirational", "life", "humor", 
            "books", "reading", "friendship", "truth"]
    tag=random.choice(tags) 
    return tag 
    

def add_to_text(quote,author):
    quote_clean = quote.replace('\u201c', '').replace('\u201d', '')
    docs_path = os.path.join(os.path.expanduser("~"), "Documents", "Rainmeter", "Skins", "Quotes", "quote.txt")
    os.makedirs(os.path.dirname(docs_path), exist_ok=True)
    with open(docs_path, "w", encoding="utf-8") as f:
        f.write(f"{quote_clean}\n- {author.text}")
    print(f'Saved in : {docs_path}')


def find_quot():
    random_quote=random.choice(quotes)         
    quote=random_quote.find("span",{'class':'text'})
    author=random_quote.find("small",{'class':'author'})
    quote=quote.text
    return quote,author
    
while True:
    tag=show_tags()
    try:
        numb=random.randint(1,2)
        page=requests.get(f"https://quotes.toscrape.com/tag/{tag}/page/{numb}")
        
        if page.status_code!=200:
            continue
        else:
            source=page.content
            soup=BeautifulSoup(source,'lxml')
            quotes=soup.find_all("div",{'class':'quote'})
            if not quotes :
                numb=1
                page=requests.get(f"https://quotes.toscrape.com/tag/{tag}/page/{numb}")
                source=page.content
                soup=BeautifulSoup(source,'lxml')
                quotes=soup.find_all("div",{'class':'quote'})

            quote,author=find_quot()
            add_to_text(quote,author)
            break
        
  
    except IndexError:
        print("Unvalid tag")
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    