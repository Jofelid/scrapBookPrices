from helpers import get_book_data
from pprint import pprint

url = 'http://books.toscrape.com/catalogue/do-androids-dream-of-electric-sheep-blade-runner-1_149/index.html'

a = get_book_data(url, 'category')

print(a['product description'])

