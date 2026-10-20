#!/usr/bin/env python3
"""Module that fetches the raw HTML content of a web page."""
import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a web page and return its HTML as text.

    Args:
        url (str): The URL of the page to retrieve.
        headers (dict): Optional HTTP headers (e.g. {"User-Agent": "..."}).
        timeout (int): Seconds to wait before aborting the request.

    Returns:
        str: The full HTML of the response.

    Raises:
        requests.HTTPError: If the response status code is >= 400.
    """
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
