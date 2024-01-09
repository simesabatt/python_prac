import requests
from datetime import datetime
from bs4 import BeautifulSoup

# URLからHTMLを取得します
url = "https://docs.pyq.jp/_static/assets/scraping/item-list.html"
response = requests.get(url)
response.encoding = response.apparent_encoding

min_date = datetime(2017, 5, 1)
max_date = datetime(2017, 8, 31)

results = []

bs = BeautifulSoup(response.text, 'html.parser')

# div.item-list で 囲まれた部分を抽出します
div_item_list = bs.select('div.item-list')

# div.item で囲まれた部分を抽出
for div_item in div_item_list[0].select('div.item'):

    # 発売日の取得
    item_release_date_tags = div_item.select('span.item-release-date')
    item_release_date_tag = item_release_date_tags[0]
    item_release_date = item_release_date_tag.text.strip()
    item_release_date = datetime.strptime(item_release_date, '%Y-%m-%d')
    # 2017-05-01 〜 2017-08-31 の範囲外であればスキップ
    if min_date > item_release_date or max_date < item_release_date:
        continue

    # 商品名の抽出
    item_name_tags = div_item.select('a.item-name')
    item_name_tag = item_name_tags[0]
    item_name = item_name_tag.text.strip()

    # 価格を抽出
    item_price_tags = div_item.select('span.item-price')
    item_price_tag = item_price_tags[0]
    item_price = item_price_tag.text.strip()

    # 合計するために文字列を数値化する
    item_price = item_price.replace('円', '')
    item_price = item_price.replace(',', '')
    item_price = int(item_price)

    # 商品名と価格のペアをリストに保存
    results.append((item_name, item_price))

# 表示する
for row in results:
    print(row[0], row[1])