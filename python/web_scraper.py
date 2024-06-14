import requests
from bs4 import BeautifulSoup

#Louer en IDF
#https://www.seloger.com/list.htm?projects=1&places=[{%22divisions%22:[2238]}]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results


BASE_URL = "https://www.seloger.com/list.htm"
URL = "https://www.seloger.com/list.htm?projects=1&places=[{%22divisions%22:[2238]}]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results"


def scrape_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2')
        for title in titles:
            print(title.get_text())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_titles(URL)
