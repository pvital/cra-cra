#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from utils import get_protocol, get_html, extract_links, clean_links

class SiteMap:
    """
    cra-cra SiteMap class
    """

    def __init__(self, url):
        self.seed = url
        self.protocol = get_protocol(url)
        self.index = []
        self._crawl()

    def get_index(self):
        return self.index

    def reset_index(self):
        self.index = {}

    def _crawl(self):
        print "Getting info for %s" % self.seed
        html = get_html(self.seed)
        links = extract_links(html)
        self.index = clean_links(links)

    def print_sitemap(self):
        """Print the SiteMap of a specific URL."""
        for link in self.get_index():
            print "\t |-> %s" % link

        print "\t |_ \n"


if __name__ == "__main__":
   print
