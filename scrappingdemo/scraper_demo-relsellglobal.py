import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.relsellglobal.in/')
# print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

path_to_follow = ["mbr-section article mbr-section__container","container","row","col-xs-12 lead"]


readTag = '';
for tag in path_to_follow:
    # print(tag)
    readTag = soup.find(class_=tag)

print(readTag.text)


