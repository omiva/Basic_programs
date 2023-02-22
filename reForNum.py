# import re
#
# x = input("input the value to check: ")
# rex = re.compile(r'(\d{,3})(,\d{3})*')
# find = rex.search(x)     #42 1,234 6,368,745 12,34,567 1234
# # print(find.group())
# if x == find.group():
#     print(find.group(), "value matched")
# else:
#     print("no match")
import certifi
import requests
from bs4 import BeautifulSoup

url = 'https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg'
reqs = requests.get(url, allow_redirects=True)
open('bird.jpg', 'wb').write(reqs.content)
# soup = BeautifulSoup(reqs.text, 'html.parser')
#
# urls = []
# for link in soup.find_all('a'):
#     print(link.get('href'))