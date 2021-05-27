import requests
from bs4 import BeautifulSoup

# il faut récupérer le noms des catégories et les liens
# resultat de sortie : list de dictionaires
def get_categories():
    return []


# retourne une liste avec les liens des détails des livres
def get_books_from_category(url_category):
    return []


def get_book_data(url_book, category):
    book_data = []
    r = requests.get(url_book)

    if r.ok:
        soup = BeautifulSoup(r.text, 'html.parser')

        title = soup.find('div', {'class': 'product_main'}).h1.text
        product_description = soup.find('article').find('p', recursive = False).text
        review_rating = soup.find('p', {'class': 'star-rating'})['class'][1]

        image_url = \
            url_book.replace('index.html', '') + \
            soup.find('div', {'class': 'thumbnail'}).img['src']

        table_dictionary = {}
        table = soup.find('table', {'class': 'table-striped'})
        rows = table.find_all('tr')
        for row in rows:
            table_dictionary[row.th.text] = row.td.text

        upc = table_dictionary['UPC']
        price_including_tax = table_dictionary['Price (incl. tax)']
        price_excluding_tax = table_dictionary['Price (excl. tax)']
        number_available = table_dictionary['Availability']

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


def download_image(url_image, folder_destination):
    pass


# fonction tourner les pages