import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
r.text
demo = r.text
print(r.text)
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())

