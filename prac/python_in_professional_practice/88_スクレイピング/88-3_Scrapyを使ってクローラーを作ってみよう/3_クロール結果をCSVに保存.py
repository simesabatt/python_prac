# 実行
# $ scrapy crawl complex -o item_list.csv
# $ cat item_list.csv

import scrapy


class ComplexSpider(scrapy.Spider):
    name = 'complex'
    allowed_domains = ['docs.pyq.jp']
    start_urls = [
        'https://docs.pyq.jp/_static/assets/scraping/item-list.html'
    ]

    def parse(self, response):
        # 商品情報を格納するリスト
        items = []

        div_item_list = response.css('div.item-list')[0]
        for div_item in div_item_list.css('div.item'):
            # 商品名の取得
            item_name = div_item.css('a.item-name::text').get()
            item_name = item_name.strip()

            # 商品リンクURLの取得
            item_link = div_item.css('a.item-name::attr(href)').get()
            item_link = item_link.strip()

            item_info = {
                'name': item_name,
                'link': item_link,
            }

            # 商品情報の辞書をリストに追加
            items.append(item_info)

        return items