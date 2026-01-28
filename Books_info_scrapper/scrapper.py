import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin
import re

url="https://books.toscrape.com/catalogue/page-"
page=1
data=[]
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

rating_map={
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }
while True:
    try:
        response=requests.get(url+str(page)+".html",headers=headers,timeout=10)
        if response.status_code!=200:
            print(f"Stopped at page: {page} and Status code : {response.status_code}")
            break
        soup=BeautifulSoup(response.text,"html.parser")
        cards=soup.find_all("article",class_="product_pod")
        if not cards:
            print("Extraction completed")
            break
        for card in cards:
            try:
                title=card.find("h3").find("a").get("title")
            except:
                title="N/A"
            

            try:
                price_text=card.find("p",class_="price_color").get_text()
                price = float(re.search(r"\d+\.\d+",price_text).group())
            except:
                price="N/A"

            try:
                availability=card.find("p",class_="instock availability").get_text(strip=True)
            except:
                availability="N/A"
            
            try:
                ratingtag=card.find("p",class_="star-rating")
                rating=rating_map.get(ratingtag["class"][1],"NA")
            except:
                rating="NA"

            product_tag=card.find("a")
            product_url=product_tag.get("href")
            product_page_url=urljoin("https://books.toscrape.com/catalogue/",product_url)

            time.sleep(0.3)

            

            try:
                category_response=requests.get(product_page_url,headers=headers,timeout=10)
                category_soup=BeautifulSoup(category_response.text,"html.parser")
                breadcrumb=category_soup.find("ul",class_="breadcrumb")
                category=breadcrumb.find_all("li")[-1].text.strip()
            except:
                category="N/A"
            
            data.append({
                "Book Title":title,
                "Price":price,
                "Availability":availability,
                "Star Rating":rating,
                "Product page URL":product_page_url,
                "Category":category
            })
        page+=1
        time.sleep(1+random.random())
        if page==3:
            break
    


    

    except requests.exceptions.RequestException as e:
        print("Network error",e)
        break

df=pd.DataFrame(data)
df.to_csv("Books_info.csv",index=False)
