import time
# from selenium_profiles.webdriver import Chrome
# from selenium_profiles.profiles import profiles
from seleniumwire import webdriver
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth

# from pathlib import Path
# curdir = Path(__file__).resolve().parent
# module_path = curdir / 'undetected-chromedriver'
# sys.path.insert(0, str(module_path))
# print(sys.path)
# import undetected_chromedriver as uc

useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", 
]


def interceptor(request):
    del request.headers["User-Agent"]
    del request.headers["Accept-Language"]
    del request.headers["Sec-Ch-Ua"]
    del request.headers["Sec-Ch-Ua-Mobile"]
    del request.headers["Sec-Ch-Ua-Platform"]

    # add the missing headers
    request.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    request.headers["Accept-Language"] = "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,tr;q=0.4,es;q=0.3,it;q=0.2"
    request.headers["Sec-Ch-Ua"] = "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\""
    request.headers["Sec-Ch-Ua-Mobile"] = "?0"
    request.headers["Sec-Ch-Ua-Platform"] = "\"Windows\""
    request.headers["Dnt"] = "1"


# Configure Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")


webdriver_service = Service('C:/Apps/selenium/chromedriver-win64/chromedriver.exe')
# webdriver_service = Service('C:/Apps/selenium/msedgedriver/msedgedriver.exe')

# profile = profiles.Windows()
options = webdriver.ChromeOptions()
# Adding argument to disable the AutomationControlled flag
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# options.add_argument("start-maximized")
# options.add_argument("--headless")  # Ensure GUI is off
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_experimental_option("detach", True)
# options.add_experimental_option("detach", True)
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=webdriver_service, options=options)
# driver = webdriver.Edge(service=webdriver_service)
# driver = uc.Chrome(headless=False, use_subprocess=True, options=options)

driver.request_interceptor = interceptor

# stealth(driver,
#         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
#         languages=["fr-FR", "fr"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

# webdriver_service = Service('C:/Apps/chromedriver-win64')  # Change this to your chromedriver path
# driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Target URL
URL = "https://www.seloger.com/list.htm?projects=1&types=2,1&places=[{%22inseeCodes%22:[920032]}]&price=600/900&sort=d_px&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_hp_last"
# URL = "https://www.google.com"


def scrape_titles(url):
    try:
        # rnd_idx = random.randint(0, len(useragents) - 1)
        # driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragents[rnd_idx]})
        # print(driver.execute_script("return navigator.userAgent;"))
        driver.get(url)
        # time.sleep(5)  # Wait for the page to fully load
        # search = driver.find_element("name", "q")
        # search.send_keys("google search through python")
        # search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(300)  # sleep for 5 seconds so you can see the results
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_titles(URL)
    # scrape_titles('https://httpbin.io/headers')


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
