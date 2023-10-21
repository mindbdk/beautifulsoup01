import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'}

url='https://www.naver.com'
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'html.parser')
print(soup)