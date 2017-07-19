# scraping related imports
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse


def latest():
    link = "http://comic.naver.com/webtoon/list.nhn?titleId=131385&weekday=thu"
    p_link = urlparse(link)
    base = p_link.scheme+'://'+p_link.netloc
    page = urlopen(link)
    soup = BeautifulSoup(page, "html.parser")
    return base+soup.select('td[class~=title] a')[0]['href']
