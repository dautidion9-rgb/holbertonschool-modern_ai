#!/usr/bin/env python3
"""Module that scrapes quote data from a site's JSON API."""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Fetch quote data from all of the quotes API pages.

    Args:
        base_url (str): The root URL of the site
            (e.g. "https://quotes.toscrape.com").

    Returns:
        list: A list of quote dicts, each with the keys "text" (str),
            "author" (str) and "tags" (list of str).
    """
    quotes = []
    page = 1
    while True:
        endpoint = "{}/api/quotes?page={}".format(base_url, page)
        payload = json.loads(fetch_html(endpoint))
        for quote in payload["quotes"]:
            quotes.append({
                "text": quote["text"],
                "author": quote["author"]["name"],
                "tags": quote["tags"]
            })
        if not payload.get("has_next"):
            break
        page += 1
    return quotes
