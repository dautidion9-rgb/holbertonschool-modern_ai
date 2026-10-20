#!/usr/bin/env python3
"""Module that scrapes products from a static e-commerce page."""
import time
from selenium import webdriver


def scrape_products_list(url):
    """Scrape every product from a static product category page.

    Args:
        url (str): The product category page URL
            (e.g. the webscraper.io static laptops page).

    Returns:
        list: A list of product dicts, each with the keys
            "title" (str), "price" (str), "description" (str)
            and "rating" (int).
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    products = []
    try:
        driver.get(url)
        time.sleep(1)
        for card in driver.find_elements("class name", "thumbnail"):
            title = card.find_element(
                "class name", "title").get_attribute("title")
            price = card.find_element("class name", "price").text
            description = card.find_element(
                "class name", "description").text
            rating = card.find_element(
                "css selector", ".ratings p[data-rating]"
            ).get_attribute("data-rating")
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": int(rating)
            })
    finally:
        driver.quit()
    return products


scrape_products = scrape_products_list
