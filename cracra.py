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

import sys

from src.sitemap import SiteMap
from src.utils import is_valid_protocol

def usage():
    print("usage: cracra [-h] <URL> ")

def main(argv):
    if len(argv) < 1:
        usage()
        sys.exit(2)

    if argv[0] == "-h":
        usage()
        sys.exit(0)

    # check if the given URL (assuming this is always argv[0]) is de facto
    # a valid URL
    if not is_valid_protocol(argv[0]):
        print "ERROR: not a valid protocol"
        sys.exit(1)

    target = SiteMap(argv[0])
    target.print_sitemap()


if __name__ == "__main__":
   main(sys.argv[1:])
   sys.exit(0)
