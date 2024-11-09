import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()

def spider_urls(url,keyWord):
    try:
        response = requests.get(url)
    except:
        print(f"Request Failed {url}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content,"html.parser")

        a_tag = soup.find_all('a')
        urls = []

        for tag in a_tag:
            href = tag.get("href")

            if href is not None and href != "":
                urls.append(href)


        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)

                if keyWord in url_join:
                    print(url_join)
                    spider_urls(url_join, keyWord)
            else:
                pass

        

target_url = input("Enter Your Target URL")
target_keyWord = input("Enter Your Target KeyWord")
spider_urls(target_url,target_keyWord)