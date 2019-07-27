# required packages
import urllib.request
from bs4 import BeautifulSoup as BS

# url to scrap
url = 'https://en.wikipedia.org/wiki/Jacqueline_Fernandez'

# getting html from url
htmlData = urllib.request.urlopen(url)

# parsing html data
soup = BS(htmlData, features="lxml")

# prettifying htmlData
soup.prettify()

# getting title of paga
print('Title -> ' + soup.title.string)

briefDetail =soup.find('table', class_='infobox biography vcard')


for row in briefDetail.findAll("tr"):
    head = row.findAll('th')
    data = row.findAll('td')

    if(len(head) > 0 and len(data) > 0):
        print(head[0].text + ' -> ' + data[0].text)