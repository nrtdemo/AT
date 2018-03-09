#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()
def send_value():
    from models.Ticket import Ticket
    from src_script.tts_v1 import TTS
    form = cgi.FieldStorage()
    ticket = Ticket(form)
    # tts = TTS()
    getvalue = ticket.getData()


    print getvalue['catid'].value
    #tts.Open_Ticket(getvalue['catid'])

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







