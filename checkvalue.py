#!/usr/bin/env python
# -*- coding: utf-8 -*-
# enable debugging

import cgitb
import cgi

form = cgi.FieldStorage()
cgitb.enable()

from models.Ticket import Ticket
from src_script.tts_v1 import TTS
from src_script.AutoOpenTicket import OpenTicketCatTTS

TTS_basehost = "122.155.137.214"
tts = TTS('catma', 'ait@1761', TTS_basehost)

openTicket = OpenTicketCatTTS(url='http://122.155.137.214/sm/ess.do?lang=en&mode=ess.do&essuser=true')

if __name__ == "__main__":
    if 'catid' in form and 'description' in form and 'title' in form:
        print "Content-type: application/x-www-form-urlencoded\n\n"
        ticket_info = Ticket(form).getData()
        openTicket.auto_openticket(ticket_info)

        # tts.test_url(ticket_info)
        # tts.Open_Ticket(ticket_info)
