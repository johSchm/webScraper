"""
author:     Digital Engineering Team
date:       12.04.2019
version:    1.0 (ALPHA) (test-version)
descr:      Simple web scraping tool in python.
execution:  python3 scraper.py
"""

from webScraperAdapter import WebScraperAdapter


class Scraper:
    """ Web scraping tool.

    :parameter
        search term
    """
    if __name__ == "__main__":
        """ Main method.
        """
        dictionary = {
            'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'engine': 'google',
            'tld': 'com',
            'term': 'backpack'
        }
        a = WebScraperAdapter(dictionary)
        a.exploit()
        a.print()
