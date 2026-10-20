#!/usr/bin/env python3
"""Module that scrapes quotes across every page of a paginated site."""
from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Scrape quotes from every page, following "Next" links.

    Args:
        base_url (str): The first page URL
            (e.g. https://quotes.toscrape.com/).

    Returns:
        list: The full list of quote dicts from all pages, each with
            the keys "text" (str), "author" (str) and "tags"
            (list of str).
    """
    quotes = []
    url = base_url
    while url:
        quotes.extend(scrape_basic(url))
        soup = BeautifulSoup(fetch_html(url), "html.parser")
        next_li = soup.find("li", class_="next")
        if next_li and next_li.find("a"):
            url = parse.urljoin(url, next_li.find("a")["href"])
            time.sleep(1)
        else:
            url = None
    return quotes
