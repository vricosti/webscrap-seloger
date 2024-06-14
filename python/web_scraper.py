from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


webdriver_service = Service()
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=webdriver_service, options=options)

#webdriver_service = Service('C:/Apps/chromedriver-win64')  # Change this to your chromedriver path
#driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Target URL
URL = "https://www.seloger.com/list.htm?projects=1&types=2,1&places=[{%22inseeCodes%22:[920032]}]&price=600/900&sort=d_px&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_hp_last"

def scrape_titles(url):
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load
        titles = driver.find_elements(By.TAG_NAME, 'h2')
        for title in titles:
            print(title.text)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_titles(URL)


# import requests
# from bs4 import BeautifulSoup

# #Louer en IDF
# #https://www.seloger.com/list.htm?projects=1&places=[{%22divisions%22:[2238]}]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results


# BASE_URL = "https://www.seloger.com"
# URL = "https://www.seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&div=2238&idtt=2,5&naturebien=1,2,4&m=search_hp_new"

# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,tr;q=0.4,es;q=0.3,it;q=0.2",
#     "Referer": "https://www.seloger.com/",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
# }


# def scrape_titles(url):
#     session = requests.Session()
#     response = session.get(url, headers=HEADERS)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         titles = soup.find_all('h2')
#         for title in titles:
#             print(title.get_text())
#     else:
#             print(f"Failed to retrieve the page. Status code: {response.status_code}")

# if __name__ == "__main__":
#     scrape_titles(URL)
