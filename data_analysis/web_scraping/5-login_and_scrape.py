#!/usr/bin/env python3
"""Module that logs into a website and scrapes quotes as that user."""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log into the quotes site and scrape the first page of quotes.

    Fetches the login form to read its CSRF token, submits the
    credentials with a session so cookies persist, then scrapes the
    page returned after login.

    Args:
        login_url (str): The login page URL
            (e.g. https://quotes.toscrape.com/login).
        user (str): The username to log in with.
        pwd (str): The password to log in with.

    Returns:
        list: A list of quote dicts, each with the keys "text" (str),
            "author" (str) and "tags" (list of str).
    """
    session = requests.Session()
    response = session.get(login_url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    token_input = soup.find("input", {"name": "csrf_token"})
    payload = {
        "csrf_token": token_input["value"],
        "username": user,
        "password": pwd
    }
    response = session.post(login_url, data=payload, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all("div", class_="quote"):
        quotes.append({
            "text": quote.find("span", class_="text").get_text(),
            "author": quote.find("small", class_="author").get_text(),
            "tags": [tag.get_text()
                     for tag in quote.find_all("a", class_="tag")]
        })
    return quotes
