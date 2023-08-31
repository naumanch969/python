import requests
from bs4 import BeautifulSoup


url = 'https://www.codewithtomi.ml/'
response = requests.get(url)

soup = BeautifulSoup(response.content,'lxml')

titles = soup.find_all('h2',{'class':'post-title'})

for title in titles:
    print(f'{title.getText()}\n')