# scrapBookPrices

scrapBookPrices is a script to extract books prices from [Book to Scrape](http://books.toscrape.com/), a bookstore website.

For each book category, the script will retrieve the following information:

* Product Page URL
* Universal Product Code (UPC)
* Title
* Price Including Tax
* Price Excluding Tax
* Number Available
* Product Description
* Category
* Review Rating
* Image url

As well as the books covers.

## Installation

In a terminal:

* Get project data.
```bash
git clone https://github.com/Jofelid/scrapBookPrices
```

* In the project folder, create then activate a virtual environment.
```bash
cd scrapBookPrices/
python -m venv env
source env/bin/activate
```

* Use the package manager [pip](https://pip.pypa.io/en/stable/) with the help of the requirement file to install dependencies.
```bash
pip install -r requirements.txt
```

## Usage

In a terminal:

* Run the script.
```bash
python main.py
```

A `downloads` folder will be create.
In which, for each book category, there wille be :
* a `[category].csv` file (delimiter : "**;**" )
* a `[category]` folder containing the books covers
