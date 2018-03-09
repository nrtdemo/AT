#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()


def send_value():
    from models.Ticket import Ticket
    from src_script.tts_v1 import TTS

    form = cgi.FieldStorage()
    TTS_basehost = "122.155.137.214"
    tts = TTS('catma', 'ait@1761', TTS_basehost)

    for f in form:
        print "{}: {}</br>".format(f, form[f].value)
    # print "</br>{}</br>".format(tts.test_url().encode('utf-8'))
    if 'description' in form and 'title' in form and 'bandwidth' in form:
        ticket = Ticket(form)
        ticket_info = ticket.getData()
        for t in ticket_info:
            print "<div class='row'><div class='col-lg-1'>{}</div><div class='col-lg-3'>{}</div></div>".format(t, ticket_info[t])
    else:
        print 'error'



    # print getvalue['catid'].value
    # tts.Open_Ticket(getvalue['catid'])

    # if(getvalue['bandwidth'].value is ''):
    #     #redirect('/cgi-enabled/openticket.py?cat_id=TBB147536')
    #     print 'no bandwidth'
    # elif(getvalue['title'].value is ''):
    #     print 'no title'
    # elif (getvalue['description'].value is ''):
    #     print 'no description'


if __name__ == '__main__':
    from src_script.template import template_AT

    template = template_AT()
    template.print_header()
    template.print_menu()

    send_value()

    template.print_close()
