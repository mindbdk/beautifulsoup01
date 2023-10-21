import requests
from bs4 import BeautifulSoup

res='''

<html>
<head> <title> 웹 사이트 제목 </title> </head>
<body> 
<p>p태그1</p>
<p>p태그2</p>
<p>p태그3</p>
</body> 
</html>
'''
soup=BeautifulSoup (res, 'html.parser')
