#!/usr/bin/env python

import cgitb
cgitb.enable()

def index():
    import cgi
    import json
    from src_script.MySQL import Database

    form = cgi.FieldStorage()
    db = Database(host='localhost', username='root',
                  password='', db='alarm_ticket')
    select_catid = """SELECT * FROM tts WHERE ticketNo = '{0}' LIMIT 1""".format(form["TicketNo"].value)
    lst_catid = db.query(select_catid)[0]
    activity = json.loads(lst_catid['activity'])

    print '<div class="box">'
    print '<div class="box-body ">'
    print '<pre>{0}</pre>'.format(lst_catid)
    print '</div>'
    print '</div>'

if __name__ == "__main__":
    from src_script.template import template_AT
    t = template_AT()
    t.print_header()
    t.print_menu()
    index()
    t.print_close()

