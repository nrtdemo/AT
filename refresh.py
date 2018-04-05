#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import cgi
from link.FortyFiftyGbE import FF
from link.PEbangkok import PE

form = cgi.FieldStorage()
cgitb.enable()

if __name__ == "__main__":
    print "Content-type: text/html\n\n"
    print
    if 'link' in form:
        Link = form['link'].value
        if Link == "40G100G":
            FF().link()
        if Link == "PE":
            PE().link()
    else:
        FF().link()
