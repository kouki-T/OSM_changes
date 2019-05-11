# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

number = 70133061
# アクセスするURL
url = "https://www.openstreetmap.org/changeset/"

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url + str(number))

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# div要素全てを摘出する→全てのdiv要素が配列に入ってかえされます\
td = soup.find_all("td")

OSM_change = ""

# for分で全てのdiv要素の中からClass="mkc-stock_prices"となっている物を探します
for tag in td:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にbrowse-tag-vと設定されているかを調べます
        if string_ in "browse-tag-v":
            # browse-tag-vが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            OSM_change = tag.string
            # 摘出が完了したのでfor分を抜けます
            break
    except:
        # パス→何も処理を行わない
        pass

# 摘出した日経平均株価を出力します。
print(OSM_change)
