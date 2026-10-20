#!/usr/bin/env python3
"""Module that scrapes quotes from a static quotes page."""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Scrape the first page of quotes from quotes.toscrape.com.

    Args:
        url (str): The Quotes List endpoint
            (e.g. https://quotes.toscrape.com/).

    Returns:
        list: A list of dicts, one per quote, each with the keys
            "text" (str), "author" (str) and "tags" (list of str).
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for quote in soup.find_all("div", class_="quote"):
        quotes.append({
            "text": quote.find("span", class_="text").get_text(),
            "author": quote.find("small", class_="author").get_text(),
            "tags": [tag.get_text()
                     for tag in quote.find_all("a", class_="tag")]
        })
    return quotes
