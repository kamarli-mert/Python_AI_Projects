#https://pypi.org/ bütün paketler burda bulunur

#free API'den veri çekme
from requests import get
from pprint import pprint

endpoint = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=4b3e2c332fec45efa30bd394249c29e6"
response = get(endpoint)

data = response.json()
#pprint(data) #bu datanın tipi dictionary.

print(f"Autor: {data.get("articles")[0].get("author")}") 
print(f"Title: {data.get("articles")[0].get("title")}") 
print(f"Content: {data["articles"][0]["content"]}") #iki türlü de olur

#kullanıcıdan yazar ismi alalım ve o yazarın makalesini yazalım
author_name = input("Enter author name: ")
for article in data["articles"]:
    if article["author"] == author_name:
        pprint(article)


