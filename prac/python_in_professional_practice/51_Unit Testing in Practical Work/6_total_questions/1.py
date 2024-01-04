import csv
from datetime import datetime, timedelta


def get_now():  # pragma:nocover (カバレッジ対象外の指定)
    return datetime.now()


class Purchase:
    def __init__(self, bought_datetime, purchase_detail, amount):
        self.bought_datetime = bought_datetime
        self.purchase_detail = purchase_detail
        self.amount = amount


def load_accounting_file(filepath):
    """ 会計ログCSVファイル filepath を読み込んで
    Purchase クラスのリストで返す

    CSVの各行の形式は `購入日,購入したものの名前,金額` 。

    * 購入日: `YYYYmmdd` 形式の日。
    * 内容: 文字列
    * 金額: 数値
    """
    purchases = []
    with open(filepath, encoding='utf-8') as f:
        for row in csv.reader(f):
            bought_date_str, purchase_detail, amount = row
            bought_datetime = datetime.strptime(bought_date_str, '%Y%m%d')
            amount = int(amount)
            purchases.append(Purchase(bought_datetime, purchase_detail, amount))
    return purchases


def past_days_accounting(filepath, days=3):
    """
    会計ログファイル filepath から過去 days 日間前に
    購入したものの合計金額を算出する
    """
    to_datetime = get_now()
    from_datetime = to_datetime - timedelta(days=days)
    purchases = load_accounting_file(filepath)
    total = 0
    for purchase in purchases:
        if from_datetime <= purchase.bought_datetime < to_datetime:
            total += purchase.amount
    return total