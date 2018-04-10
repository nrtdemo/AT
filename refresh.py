#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import cgi
from link.FortyFiftyGbE import FF
from link.PEbangkok import PE

form = cgi.FieldStorage()
cgitb.enable()

if __name__ == "__main__":
    print "Content-type: application/json\n\n"
    print
    if 'link' in form:
        Link = form['link'].value
        if Link == "40G100G":
            ff = FF()
            ff.jsonlink()
        if Link == "PE":
            pe = PE()
            pe.jsonlink()
    else:
        ff = FF()
        ff.jsonlink()
