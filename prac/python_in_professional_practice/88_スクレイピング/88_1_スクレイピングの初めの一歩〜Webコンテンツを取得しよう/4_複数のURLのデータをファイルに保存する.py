import time
import requests

# 取得したいURL書きましょう
url_html = "https://docs.pyq.jp/_static/assets/scraping/ensyu1.html"
url_csv = "https://docs.pyq.jp/_static/assets/scraping/ensyu1.csv"

# HTMLの取得
response = requests.get(url_html)
response.encoding = response.apparent_encoding

ensyu_html = response.text

# 1秒スリープ
time.sleep(1)

# CSVの取得
response = requests.get(url_csv)
response.encoding = response.apparent_encoding

ensyu_csv = response.text

# ファイルの保存
with open('ensyu1.html', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_html)

with open('ensyu1.csv', mode='w', encoding='utf-8') as fp:
    fp.write(ensyu_csv)

print("保存完了")