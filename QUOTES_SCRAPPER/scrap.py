import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

url="https://quotes.toscrape.com/page/"
page=1
data=[]
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}
while True:
    try:
        response=requests.get(url+str(page),timeout=10,headers=headers)

        if response.status_code!=200:
            print(f"stopped at page: {page}, status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text,"html.parser")
        cards = soup.find_all("div",class_="quote")

        if not cards:
            print("No more data found")
            break
        for card in cards:
            text=card.find("span",class_="text")
            Author=card.find("small",class_="author")
            tags=card.find_all("a",class_="tag")

            data.append({
            "Text":text.text.strip() if text else "N/A",
            "Author":Author.text.strip() if Author else "N/A",
            "Tags": ", ".join([tag.text.strip() for tag in tags]) if tags else "N/A"
            })
        
        page+=1
        time.sleep(1+random.random())

    except requests.exceptions.RequestException as e:
        print("Network error :",e)
        break

df= pd.DataFrame(data)
df.to_csv("Quotes.csv",index=False)






        




