import requests
from bs4 import BeautifulSoup

res='''

<html>
<head> <title> 웹 사이트 제목 </title> </head>
<body> 
<ul>
    <li>hello</li>
    <li>사과</li>
    <li>떡볶이</li>
<ul>
</body> 
</html>
'''

soup=BeautifulSoup (res, 'html.parser')
ul=soup.findAll('ul')

