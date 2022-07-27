from bs4 import BeautifulSoup
import requests
authors_name=[]
book_name=[]
stars=[]
URL="https://www.audible.com/search?keywords=book&node=18573211011"
response = requests.get(URL)
response=response.text
soup = BeautifulSoup(response,"html.parser")
# print(soup.prettify())
rating=soup.find_all(name="span",class_="bc-pub-offscreen")
for items in rating:
    stars.append(items.text)
name_book=soup.select("ul li h3  a ")
for items in name_book:
    book_name.append(items.text)

author=soup.find_all(name="li",class_="authorLabel")
for items in author:
    authors_name.append(items.text)

print(authors_name)
print(book_name)
print(stars)
for items in authors_name:
    new =items.replace("\n"," ")
authors_name= new.replace("By:"," ")

print(authors_name)
with open ("authors_name.txt","w")as file:
    for items in author:
        file.write(str(items) + "\n")
with open ("book_name.txt","w")as file:
    for items in book_name:
        file.write(str(items) + "\n")
with open("rating.txt","w") as file:
    for items in stars:
        file.write(str(items) + "\n")