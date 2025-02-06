import re
import lxml
import requests
import pandas as pd
from bs4 import BeautifulSoup


def requestWebsite(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    content = soup.find("div", class_="c-product-list__content js-infiniti-scroll-product-list-content")
    print(content)

    return content


def webScraping(content):
    productName = []
    productCost = []
    productDiscount = []
    products = content.findAll("div", class_="c-product-list__item js-product-list-content")
    for product in products:
        try:
            productName.append(product.find("div",
                                            class_="js-product-cart c-product-box c-product-box--product-card c-product-box--has-overflow c-product-box--card-macro c-product-box--plus-badge").attrs.get(
                'title'))
            productCost.append(product.find("div", class_="c-price__value-wrapper js-product-card-price").text.split('\n')[1])
            productDiscount.append(product.find("div", class_="c-price__discount-oval").text)
        except:
            continue

    df = pd.DataFrame(list(zip(productName, productCost, productDiscount)), columns=['Product Name', 'Cost', 'Discount'])
    return df


def write2File(information):
    information.to_csv("products.csv")


if __name__ == '__main__':
    url = "https://www.digikala.com/incredible-offers/?pageno=2"
    content = requestWebsite(url)
    information = webScraping(content)
    write2File(information)
