#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb

cgitb.enable()


def index():
    from src_script.MySQL import Database
    db = Database(host='localhost', username='root',
                  password='', db='alarm_ticket')
    select_catid = """SELECT * FROM splunk LEFT JOIN tts ON (splunk.cat_id = tts.cat_id) WHERE host LIKE '10.126.%' GROUP BY src_interface, host, hostname, path"""
    lst_catid = db.query(select_catid)

    print '<div class="box">'
    print '<div class="box-header"><h3 class="box-title">Monitor Link 40G&100GbE Up_Down</h3>'
    print '<div style="padding-bottom: 0;">'
    print '<div class="row">'
    print '<div class="col-xs-12">'
    print '<div class="form-group">'
    print '<ul class="list-inline" style="padding: 5px;margin-bottom: -10px;font-size: 12px">'
    print '<label for="Up">'
    print '<li style="padding: 2px 15px 2px 2px;border: 1px solid #ccc;border-radius: 2px;cursor: pointer;">'
    print '<input id="0" class="status-filter cb-element" type="checkbox" value="Up">'
    print '<span style="margin-left: 5px;">Up</span>'
    print '</li>'
    print '</label>'
    print '<label for="Down">'
    print '<li style="padding: 2px 15px 2px 2px;border: 1px solid #ccc;border-radius: 2px;cursor: pointer;">'
    print '<input id="1" class="status-filter cb-element" type="checkbox" value="Down">'
    print '<span style="margin-left: 5px;">Down</span>'
    print '</li>'
    print '</label>'
    print '</ul>'
    print '</div>'
    print '</div>'
    print '</div>'
    print '</div>'
    print '</div>'

    print '<div class="box-body">'
    print '<div class="table-responsive">'
    print '<table class="table table-bordered table-hover table-striped" id="alarmtickets">'
    print " <thead>"
    print '     <tr class="Bg-head-table">'
    print '         <th class="col-lg-1">Ticket No.</th>'
    print '         <th class="col-lg-1">Cat ID</th>'
    print '         <th class="col-lg-1">Source Interface</th>'
    print '         <th class="col-lg-1 text-center">Host</th>'
    # print '<th class="col-lg-1">Hostname</th>'
    # print '<th class="col-lg-1">device_time</th>'
    print '         <th class="col-lg-1 text-center">Port Status</th>'
    print '         <th class="col-lg-1">Path</th>'
    print '         <th class="col-lg-1">flap</th>'
    print '         <th class="col-lg-1">Ticket Status</th>'
    print '         <th class="col-lg-1">Affected Service</th>'
    print '         <th class="col-lg-1"></th>'
    print "     </tr>"
    print " </thead>"
    print " <tbody>"
    for l in lst_catid:
        print '<tr>'
        if l['incident_id'] is not None:
            print '         <td class="col-lg-1"><a href="/cgi-enabled/activity.py?TicketNo={0}">{0}</a></td>'.format(
                l['ticketNo'])
        else:
            print '         <td class="col-lg-1"></td>'
        if len(l['cat_id']) < 12:
            print '         <td class="col-lg-1">{0}</td>'.format(l['cat_id'])
        else:
            print '         <td class="col-lg-1"></td>'
        print '         <td class="col-lg-1">{0}</td>'.format(l['src_interface'])
        print '         <td class="col-lg-1 text-center"><div data-original-title="{1}" data-container="body" data-toggle="tooltip" data-placement="bottom" title="">{0}</div></td>'.format(
            l['host'], l['hostname'])
        # print '<td class="col-lg-1">{0}</td>'.format(l['hostname'])
        # print '<td class="col-lg-1">{0}</td>'.format(l['device_time'])
        if l['port_status'] == 'Down':
            css_portstatus = 'danger'
        else:
            css_portstatus = 'success'
        print '         <td class="col-lg-1 text-center {1}"><div data-original-title="{2}" data-container="body" data-toggle="tooltip" data-placement="bottom" title="">{0}</div></td>'.format(
            l['port_status'], css_portstatus, l['device_time'])
        print '         <td class="col-lg-1">{0}</td>'.format(
            l['path'])
        print '         <td class="col-lg-1">{0}</td>'.format(l['flap'])
        if l['problem_status'] is not None:
            print '         <td class="col-lg-1">{0}</td>'.format(l['problem_status'])
        else:
            print '         <td class="col-lg-1"></td>'
        print '         <td class="col-lg-1">{0}</td>'.format(l['affected_item'])
        if l['port_status'] == 'Down' and (l['problem_status'] == 'Closed' or l['problem_status'] is None):
            print '         <td class="col-lg-1"><a href="/cgi-enabled/openticket.py?cat_id={0}"><input type="button" class="btn btn-default" value="open ticket"></a></td>'.format(
                l['cat_id'])
        else:
            print '         <td class="col-lg-1"></td>'
        print '</tr>'

    print " </tbody>"
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
