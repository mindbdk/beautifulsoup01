import requests
from bs4 import BeautifulSoup

res='''

<html>
<head> <title class="t" id="ti"> 웹 사이트 제목 </title> </head>
<body> 
<p>p태그1</p>
<p>p태그2</p>
<p>p태그3</p>
</body> 
</html>
'''
soup=BeautifulSoup (res, 'html.parser')
tagP=soup.p
tagP_child=tagP.contents
print(tagP_child)