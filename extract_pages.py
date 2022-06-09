from re import S
from bs4 import BeautifulSoup as bs4
from typing import List
import urllib3
from tqdm import tqdm

LINK = "https://www.aljazeera.com/where/mozambique/"


def extract_text(url: str) -> str:
    https = urllib3.PoolManager()
    r = https.request("GET", url)
    soup = bs4(r.data, features="html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    return "\n".join(chunk for chunk in chunks if chunk)


def extract_data_from_aljazeera(n: int = 10) -> List[List[str]]:
    https = urllib3.PoolManager()
    r = https.request("GET", LINK)

    soup = bs4(r.data, "lxml")
    news_feed = soup.findAll("section", {"id": "news-feed-container"})
    articles = news_feed[0].findAll("article")[:n]
    hrefs = list(map(lambda x: x.a["href"], articles))
    headings = list(map(lambda x: x.a.span.text, articles))
    links = list(map(lambda x: "https://www.aljazeera.com" + x, hrefs))
    results = []
    for heading, url in tqdm(list(zip(headings, links)), desc="Extracting Articles"):
        results.append([heading, extract_text(url)])
    return results


if __name__ == "__main__":
    print(extract_data_from_aljazeera()[0])
