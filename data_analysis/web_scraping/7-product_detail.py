#!/usr/bin/env python3
"""Module that scrapes the detail page of a single product."""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Scrape one product's detail page after waiting for it to load.

    Args:
        url (str): The product detail page URL
            (e.g. the webscraper.io static product page).
        delay (float): Seconds to wait after loading the page.

    Returns:
        dict: A product dict with the keys "title" (str),
            "price" (str), "description" (str) and "rating" (int).
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)
        title = driver.find_elements("css selector", ".caption h4")[1].text
        price = driver.find_element("css selector", "h4.price").text
        description = driver.find_element(
            "css selector", "p.description").text
        stars = driver.find_elements(
            "css selector", ".ratings .ws-icon.ws-icon-star")
        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": len(stars)
        }
    finally:
        driver.quit()
