from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

def scrape_forever21(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', {'class': 's-item'})

        scraped_data = []

        for product in products:
            name = product.find('p', {'class': 's-item__title'}).text.strip()
            price = product.find('span', {'class': 's-item__price'}).text.strip()
            scraped_data.append({'name': name, 'price': price})
        print("Scraping complete.")
        return scraped_data
    else:
        print("Failed to retrieve page.")
        return []

@app.route('/')
def index():
    url = "https://www.forever21.com/us/shop/catalog/category/f21"  # URL of Forever 21 Women's Clothing section
    data = scrape_forever21(url)
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
