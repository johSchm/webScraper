"""
author:     Digital Engineering Team
date:       11.04.2019
version:    1.0 (ALPHA) (test-version)
descr:      Web scraper adapter.
execution:  ---
"""


import requests
import sys
import os
from headline import Headline
from bs4 import BeautifulSoup


""" Default dictionary for the web scraper adapter.
"""
dictionary_default = {

    # @see list of supported browsers: ./resources/user_agents.txt
    # find your user agent under: https://httpbin.org/user-agent
    'user_agent':  'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',

    # @see list of supported search engines: ./resources/engines.txt
    'engine':   'google',

    # (tld: country specific top-level-domain (ccTLD))
    'tld':      'com',

    # search term
    'term':     'test',

    # @see list of supported categories per browser: ./resources/categories.txt
    'category': 'news'
}


""" Path to certain resource files.
"""
CURRENT_DIRECTORY = os.path.dirname(__file__)
RES_PATH_USER_AGENTS = os.path.join(CURRENT_DIRECTORY, '..', 'resources', 'user_agents.txt')


class WebScraperAdapter:
    """ Web scraper adapter class.

    This class provides methods for web searching.
    Therefore, the user needs to provide:
    @see default dictionary

    Further methods are feasible to analyze the fetched HTML code in a given way
    and return or print the result for further exploits.
    """

    def __init__(self, dictionary):
        """ Initialization method.
        :param dictionary
        """
        self.raw_html = None
        self.headlines = []
        self.url = ""
        self.url_header = ""
        self.term = dictionary.get('term')
        self.engine = dictionary.get('engine')
        self.user_agent = dictionary.get('user_agent')
        self.tld = dictionary.get('tld')
        self.category = dictionary.get('category')
        self.concat_url()
        self.config_url_header()

    def concat_url(self):
        """ Concatenate url parameters to a final url.
        """
        self.url = 'https://www.{0}.{1}/search?q={2}&source=lnms'.format(self.engine, self.tld, self.term)

    def config_url_header(self):
        """ Specifies the header dictionary for web requests.
        """
        self.url_header = {'User-Agent': dictionary_default.get('user_agent')}
        try:
            if self.user_agent in open(RES_PATH_USER_AGENTS).read():
                self.url_header = {'User-Agent': self.user_agent}
        except FileNotFoundError:
            print("ERROR: Resource file not found: " + RES_PATH_USER_AGENTS)

    def fetch_html_code(self):
        """ This method is responsible for fetching the whole HTML code with the given configuration.
        """
        response = requests.get(self.url, headers=self.url_header)
        self.raw_html = BeautifulSoup(response.text, "html.parser")

    def extract_headlines(self):
        """ Gather all headline information from the passed html code and return them as a list.
        :return list of headlines
        """
        self.headlines.clear()
        result_block = self.raw_html.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            description = result.find('span', attrs={'class': 'st'})
            if link and title:
                link = link['href']
                title = title.get_text()
                if description:
                    description = description.get_text()
                if link != '#':
                    self.headlines.append(Headline(title, link, description))
        return self.headlines

    def exploit(self):
        """ Starts the web scraper tool and returns the gathered headlines.
        :return: headline list
        """
        self.fetch_html_code()
        self.extract_headlines()
        return self.headlines

    def print(self):
        """ Prints the headline in the terminal.
        """
        for i in range(0, self.headlines.__len__()):
            print("Headline {0}:".format(i))
            self.headlines[i].print()
            print("\n")