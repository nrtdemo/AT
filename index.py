#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import cgi

form = cgi.FieldStorage()
cgitb.enable()


def FortyFiftyGb():
    from link.FortyFiftyGbE import FF
    ff = FF()
    ff.headerlink()
    print " <tbody id='content_info'>"
    ff.link()
    print " </tbody>"
    ff.bottomlink()


def PEBankok():
    from link.PEbangkok import PE
    pe = PE()
    pe.headerlink()
    print " <tbody id='content_info'>"
    pe.link()
    print " </tbody>"
    pe.bottomlink()


def main():
    if 'link' in form:
        Link = form['link'].value
        if Link == "40G100G":
            FortyFiftyGb()
        elif Link == "PE":
            PEBankok()
    else:
        FortyFiftyGb()


if __name__ == "__main__":
    from src_script.template import template_AT

    t = template_AT()
    t.print_header()
    t.print_menu()

    main()

    t.print_close()
