"""
author:     Digital Engineering Team
date:       12.04.2019
version:    1.0 (ALPHA) (test-version)
descr:      Headline object for search engine results.
execution:  ---
"""


class Headline:
    """ Headline object for search engine results.
    """

    def __init__(self, title="", link="", description=""):
        """ Initialization method.
        """
        self.title = title
        self.link = link
        self.description = description

    def print(self):
        """ Prints the headline.
        """
        print("Title: {0}".format(self.title))
        print("Link: {0}".format(self.link))
        print("Description: {0}".format(self.description))
