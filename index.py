#!/usr/bin/env python

import cgitb
cgitb.enable()

def index():
    from src_script.MySQL import Database
    db = Database(host='localhost', username='root',
                  password='', db='alarm_ticket')
    select_catid = """SELECT * FROM splunk LEFT JOIN tts ON (splunk.cat_id LIKE tts.cat_id)"""
    lst_catid = db.query(select_catid)

    print '<div class="box">'
    print '<div class="box-body ">'
    print '<div class="table-responsive">'
    print '<table class="table table-bordered table-striped" id="alarmtickets">'
    print "<thead>"
    print '<tr class="Bg-head-table">'
    print '<th class="col-lg-1">Ticket No.</th>'
    print '<th class="col-lg-1">Cat ID</th>'
    print '<th class="col-lg-1">Source Interface</th>'
    print '<th class="col-lg-1">Host</th>'
    print '<th class="col-lg-1">Hostname</th>'
    print '<th class="col-lg-1">device_time</th>'
    print '<th class="col-lg-1 text-center">Port Status</th>'
    print '<th class="col-lg-1">Path</th>'
    print '<th class="col-lg-1">flap</th>'
    print '<th class="col-lg-1">Ticket Status</th>'
    print '<th class="col-lg-1">Affected Service</th>'
    print '<th class="col-lg-1"></th>'
    print "</tr>"
    print "</thead>"
    print "<tbody>"
    for l in lst_catid:
        print '<tr class="Bg-head-table">'
        if l['incident_id'] is not None:
            print '<td class="col-lg-1"><a href="/cgi-enabled/activity.py?TicketNo={0}">{0}</a></td>'.format(
                l['ticketNo'])
        else:
            print '<td class="col-lg-1"></td>'
        if len(l['cat_id']) < 12:
            print '<td class="col-lg-1">{0}</td>'.format(l['cat_id'])
        else:
            print '<td class="col-lg-1"></td>'
        print '<td class="col-lg-1">{0}</td>'.format(l['src_interface'])
        print '<td class="col-lg-1">{0}</td>'.format(l['host'])
        print '<td class="col-lg-1">{0}</td>'.format(l['hostname'])
        print '<td class="col-lg-1">{0}</td>'.format(l['device_time'])
        if l['port_status'] == 'Down':
            css_portstatus = 'danger'
        else:
            css_portstatus = 'success'
        print '<td class="col-lg-1 text-center {1}">{0}</td>'.format(
            l['port_status'], css_portstatus)
        print '<td class="col-lg-1">{0}</td>'.format(
            l['path'])
        print '<td class="col-lg-1">{0}</td>'.format(l['flap'])
        if l['status'] is not None:
            print '<td class="col-lg-1">{0}</td>'.format(l['problem_status'])
        else:
            print '<td class="col-lg-1"></td>'
        print '<td class="col-lg-1">{0}</td>'.format(l['affected_item'])
        print '<td class="col-lg-1"></td>'
        print "</tr>"

    print "</tbody>"
    print "</table>"
    print "</div>"
    print "</div>"
    print "</div>"


if __name__ == "__main__":
    from src_script.template import template_AT
    t = template_AT()
    t.print_header()
    t.print_menu()

    index()

    t.print_close()