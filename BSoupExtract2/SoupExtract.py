from bs4 import BeautifulSoup as bs
import requests

domain = "https://www.ncei.noaa.gov/" #Insert base web domain here#
url = "https://www.ncei.noaa.gov/data/snowstorm-database/archive/" #Insert the url you will pull files from here#
filetype = ".gz" #Insert file type identifier here#

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

for link in get_soup(url).find_all('a'):
    file_link = link.get('href')
    if filetype in file_link:
        print(file_link)
        with open(link.text, 'wb') as file:
            response = requests.get(url + file_link)
            file.write(response.content)