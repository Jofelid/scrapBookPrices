from helpers import get_categories, get_books_from_category, get_book_data
from helpers import write_csv, download_image
from os import makedirs

download_dir = './downloads/'
makedirs(download_dir, exist_ok=True)

url = 'http://books.toscrape.com/'

print('getting categories')
categories = get_categories(url)

i = 1
for category in categories:
    print('category ' + str(i))
    books = get_books_from_category(category['url'])

    j = 1
    books_data = []
    for book in books:
        print(' book ' + str(j))
        books_data.append(get_book_data(book, category['title']))

        j += 1
        # if j > 3:
        #     break

    print('writing ' + category['title'] + '.csv')
    write_csv(download_dir + category['title'] + '.csv', books_data)

    for data in books_data:
        print('downloading ' + data['title'] + '.jpg')
        download_image(data['image url'], download_dir + data['title'] + '.jpg')
    i += 1
    # if i > 2:
    #     break
