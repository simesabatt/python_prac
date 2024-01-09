import requests
from bs4 import BeautifulSoup

# URLからHTMLを取得します
url = "https://docs.pyq.jp/_static/assets/scraping/item-list.html"
response = requests.get(url)
response.encoding = response.apparent_encoding

stock_list = []  # 在庫数を格納
price_list = []  # 価格を格納

bs = BeautifulSoup(response.text, 'html.parser')

# div.item-list で 囲まれた部分を抽出します
div_item_list = bs.select('div.item-list')

# div.item で囲まれた部分を抽出
for div_item in div_item_list[0].select('div.item'):
    
    # 在庫数の取得
    item_stock_tags = div_item.select('span.item-stock')
    item_stock_tag = item_stock_tags[0]
    item_stock = item_stock_tag.text.strip()

    # 在庫が無いものはスキップ
    if item_stock == '無し':
        continue

    # 合計するために文字列を数値化する
    item_stock = item_stock.replace('個', '')
    item_stock = item_stock.replace(',', '')
    item_stock = int(item_stock)
    stock_list.append(item_stock)

    # 価格を抽出
    item_price_tags = div_item.select('span.item-price')
    item_price_tag = item_price_tags[0]
    item_price = item_price_tag.text.strip()

    # 合計するために文字列を数値化する
    item_price = item_price.replace('円', '')
    item_price = item_price.replace(',', '')
    item_price = int(item_price)
    price_list.append(item_price)

print(f'合計在庫数: {sum(stock_list)}個')
print(f'合計金額: {sum(price_list)}円')