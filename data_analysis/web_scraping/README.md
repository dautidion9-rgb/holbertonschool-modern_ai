# Web Scraping

Python web scraping project for the Holberton School Modern AI curriculum.

## Description

This project covers fetching and parsing web pages with Python, using
`urllib`, `beautifulsoup4`, and `selenium` to extract data from static
and dynamic websites.

## Requirements

- Ubuntu 20.04 LTS, Python 3.11
- numpy 2.0.2, beautifulsoup4 4.12.2, selenium 4.34.2
- Code follows `pycodestyle` 2.11.1
- All modules, classes, and functions are documented
- All files are executable and start with `#!/usr/bin/env python3`

## Sites used

- https://quotes.toscrape.com/
- https://webscraper.io/test-sites/e-commerce/static
- https://webscraper.io/test-sites/e-commerce/allinone

## Tasks

| File | Description |
| ---- | ----------- |
| `0-fetch_html.py` | Fetch and print the raw HTML content of a web page |
| `1-scrape_basic.py` | Scrape quote text, author and tags from a static quotes page |
| `2-scrape_paginated.py` | Follow "Next" links to scrape quotes from all pages |
| `3-scrape_via_api.py` | Fetch all quotes from the site's JSON API endpoints |
| `4-extract_jsonld.py` | Extract quotes from embedded JSON-LD script blocks |
| `5-login_and_scrape.py` | Log in with a session and CSRF token, then scrape quotes |
| `6-products_list.py` | Scrape product cards from a static page with headless Selenium |
| `7-product_detail.py` | Scrape one product's detail page, counting its star rating |
