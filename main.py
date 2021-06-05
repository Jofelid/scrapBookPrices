from helpers import get_categories, get_books_from_category, get_book_data
from helpers import write_csv, download_image
from os import makedirs

download_dir = './downloads/'
makedirs(download_dir, exist_ok=True)

url = 'http://books.toscrape.com/'

print('getting categories')
categories = get_categories(url)

for category in categories:
    print('\n' + 'getting books from ' + category['title'] + ':')
    books = get_books_from_category(category['url'])

    books_data = []
    for book in books:
        books_data.append(get_book_data(book, category['title']))
        print(' ' + books_data[-1]['title'])

    print('\n' + 'writing ' + category['title'] + '.csv')
    write_csv(download_dir + category['title'] + '.csv', books_data)

    print('')

    images_dir = download_dir + category['title'] + '/'
    makedirs(images_dir, exist_ok=True)

    for data in books_data:
        file_name = data['title'].replace("/", " - ") + ' - ' + \
                    data['universal product code (upc)'] + '.jpg'

        print('downloading ' + file_name)
        download_image(data['image url'], images_dir + file_name)
