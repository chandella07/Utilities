import requests
from lxml import html


s = requests.session()

url = "https://www.amazon.in/"

r = s.get(url)

tree = html.fromstring(r.content)

discounts = tree.xpath("//span[@class='red-sticker']")

print discounts
