import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.relsellglobal.in/')
# print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

# get the repo list
section = soup.find(class_="mbr-section article mbr-section__container")
container = section.find(class_="container")
row = container.find(class_="row")
desiredTag = row.find(class_="col-xs-12 lead")
print(desiredTag)

# find all instances of that class (should return 25 as shown in the github main page)
# repo_list = repo.find_all(class_='col-12 d-block width-full py-4 border-bottom')

# print(len(repo_list))