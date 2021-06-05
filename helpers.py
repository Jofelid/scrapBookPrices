import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


def get_categories(url):
    categories = []

    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.content, 'html.parser')

        table = soup.find('ul', {'class': 'nav nav-list'}).li.find_all('li')
        for row in table:
            categories.append({
                'title': row.text.strip(),
                'url': url + row.a['href']
            })

    return categories


def get_books_from_category(url_category):
    books_from_category = []

    r = requests.get(url_category)
    i = 2
    while r.ok:
        soup = BeautifulSoup(r.content, 'html.parser')

        books = soup.find_all('article', {'class': 'product_pod'})
        for book in books:
            url_book = urljoin(url_category, book.find('a')['href'])
            books_from_category.append(url_book)

        url_next = urljoin(url_category, 'page-' + str(i) + '.html')
        r = requests.get(url_next)
        i += 1

    return books_from_category


def get_book_data(url_book, category):
    book_data = []

    r = requests.get(url_book)
    if r.ok:
        soup = BeautifulSoup(r.content, 'html.parser')

        title = soup.find('div', {'class': 'product_main'}).h1.text
        product_description_p = soup.find('article').find('p', recursive=False)
        product_description = product_description_p.text if product_description_p else ""

        review_rating = soup.find('p', {'class': 'star-rating'})['class'][1]
        image_url = urljoin(url_book, soup.find('div', {'class': 'thumbnail'}).img['src'])

        table = {}
        rows = soup.find('table', {'class': 'table-striped'}).find_all('tr')
        for row in rows:
            table[row.th.text] = row.td.text

        upc = table['UPC']
        price_including_tax = table['Price (incl. tax)']
        price_excluding_tax = table['Price (excl. tax)']
        number_available = table['Availability']

        book_data = {
            'product page url': url_book,
            'universal product code (upc)': upc,
            'title': title,
            'price including tax': price_including_tax,
            'price excluding tax': price_excluding_tax,
            'number available': number_available,
            'product description': product_description,
            'category': category,
            'review rating': review_rating,
            'image url': image_url
        }

    return book_data


def write_csv(file_name, data):
    with open(file_name, 'w') as csv_file:
        headers = data[0].keys()
        writer = csv.DictWriter(csv_file, headers, delimiter=';')
        writer.writeheader()
        writer.writerows(data)


def download_image(url_image, file_name):
    r = requests.get(url_image, stream=True)
    if r.ok:
        with open(file_name, 'wb') as image_file:
            image_file.write(r.content)
