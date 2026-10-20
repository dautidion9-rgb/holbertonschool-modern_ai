#!/usr/bin/env python3
"""Module that extracts quotes from JSON-LD embedded in a web page."""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Pull quotes from embedded JSON-LD blocks on a page.

    Args:
        url (str): The Quotes List endpoint
            (e.g. "https://quotes.toscrape.com/").

    Returns:
        list: A list of quote dicts, each with the keys "text" (str),
            "author" (str) and "tags" (list of str).
    """
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for script in soup.find_all("script", type="application/ld+json"):
        data = json.loads(script.string)
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            if item.get("@type") != "Quote":
                continue
            tags = item.get("keywords", [])
            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(",")]
            quotes.append({
                "text": item.get("text"),
                "author": item.get("author", {}).get("name"),
                "tags": tags
            })
    return quotes
