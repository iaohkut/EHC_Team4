import requests
from bs4 import BeautifulSoup as bs

url = "https://dantri.com.vn/the-thao.htm"

r = requests.get(url)
soup = bs(r.content, "html.parser")

block_titles1 = soup.select("div.row")
titles1 = block_titles1[0].select("h3.article-title")
for tit in titles1:
    print(tit.text)

# Bởi vì class:row là unique nên chúng ta có thể dùng select_one
# block_titles1 = soup.select_one("div.row")
# titles1 = block_titles1.select("h3.article-title")
# for tit in titles1:
#     print(tit.text)

block_titles = soup.select_one("div.row.line.mt-30")

# Phần "tiêu điểm" có title bị lặp lại nên bị lược bỏ
all_titles = block_titles.select_one("div.col.col-840")

titles2 = all_titles.select("h3.article-title")
for tit in titles2:
    print(tit.text)
