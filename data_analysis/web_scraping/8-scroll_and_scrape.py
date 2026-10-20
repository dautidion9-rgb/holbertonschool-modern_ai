#!/usr/bin/env python3
"""Module that scrolls a JS-rendered page and scrapes all products."""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll an infinite-scroll page to the end and scrape products.

    Scrolls to the bottom repeatedly, waiting scroll_pause seconds
    each time, until the page height stops increasing, then extracts
    every product card, skipping duplicates.

    Args:
        url (str): The infinite-scroll page URL
            (e.g. the webscraper.io scroll laptops page).
        scroll_pause (float): Seconds to wait after each scroll.

    Returns:
        list: A list of unique product dicts, each with the keys
            "title" (str), "price" (str), "description" (str)
            and "rating" (int).
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()
    try:
        driver.get(url)
        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title").get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            if (title, price) in seen:
                continue
            seen.add((title, price))
            description = card.find_element(
                "css selector", "p.description").text
            stars = card.find_elements(
                "css selector", ".ratings .ws-icon.ws-icon-star")
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": len(stars)
            })
    finally:
        driver.quit()
    return products
