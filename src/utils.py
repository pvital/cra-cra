
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

import types
import requests


VALID_PROTOCOLS = ['http', 'https', 'ftp']


def is_valid_protocol(url):
    """Verifies if the given URL has a valid protocol (http, https or ftp)."""
    if not get_protocol(url) in VALID_PROTOCOLS:
        return False
    return True



def get_protocol(url):
    """Returns the protocol of a given URL."""
    try:
        return url.split("://")[0]
    except:
        return ""


def get_html(url):
    """Establishes a connection to a given URL, reads the source code or the
    html code and returns it."""
    try:
        return requests.get(url).text
    except:
        return ""


def get_url(link):
    """Returns only the URL of a given href block"""
    if not link.startswith("href="):
        return ""

    # The URL is located right before the = of href quote.
    # Since we garantee that link starts with "href=", we know the position
    # of the first = and where the url begins. Then we need find the next "
    # which is the end of the URL.
    begin = 6
    end = link[begin:].find("\"")

    # If end is -1, we could not find the ".
    if (end == -1):
         end = link[begin:].find("\'")

    url = link[begin:begin+end]

    if is_valid_protocol(url):
        return url
    else:
        return ""


def extract_links(html):
    """Extract all links from a given HTML code and return then in a list."""
    links = []
    begin = html.find("href=")

    while (begin >= 0):
        end = html[begin:].find(">") + 1
        link = html[begin:begin+end]
        links.append(get_url(link))
        html = html[begin+end:]
        begin = html.find("href=")

    return links


def clean_links(arg):
    """Clean a given list removing duplicates and blank values."""
    # Clean the given structure only if it's a list, otherwise return arg.
    if isinstance(arg, types.ListType):
        # Let only the valid URLs in the list
        x = [item for item in arg if is_valid_protocol(item)]

        # Remove duplicates
        arg = list(set(x))

    return arg


if __name__ == "__main__":
   print
