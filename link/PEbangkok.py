#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import datetime
import time
import pytz
import json

cgitb.enable()


class PE(object):
    def headerlink(self):
        print '<div class="box">'
        print '<div class="box-header"><h3 class="box-title">Link PE Bangkok Flap 24hr</h3>'
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
        print '<table class="table table-bordered table-striped" id="alarmtickets">'
        print " <thead>"
        print '     <tr class="Bg-head-table">'
        print '         <th class="col-lg-1">Ticket No.</th>'
        print '         <th class="col-lg-1">Cat ID</th>'
        print '         <th class="col-lg-1">Source Interface</th>'
        print '         <th class="col-lg-1 text-center">Host</th>'
        print '         <th class="col-lg-1 text-center">Port Status</th>'
        print '         <th class="col-lg-1">Path</th>'
        print '         <th class="col-lg-1">flap</th>'
        print '         <th class="col-lg-1">Ticket Status</th>'
        print '         <th class="col-lg-1">Affected Service</th>'
        print '         <th class="col-lg-1"></th>'
        print "     </tr>"
        print " </thead>"

    def bottomlink(self):
        print "</table>"
        print "</div>"
        print "</div>"
        print "</div>"

    def jsonlink(self):
        from src_script.MySQL import Database

        db = Database()
        select_catid = """SELECT * FROM splunk 
                                    LEFT JOIN tts ON (splunk.cat_id = tts.cat_id)
                                    LEFT join online_active ON (splunk.cat_id = online_active.catid) 
                                    WHERE host LIKE '10.5.0%' GROUP BY src_interface, host, hostname, path
                                    ORDER BY ticketNo desc
                                    """
        lst_catid = db.query(select_catid)
        json_data = []
        ''' ticketNo, cat_id, src_interface, host, port_status, path, flap, problem_status, affected_item'''
        for r in lst_catid:
            if r['problem_status'] is None:
                r['problem_status'] = ''
            if r['affected_item'] is None:
                r['affected_item'] = ''

            tmp = """[ "{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}", "{10}", "{11}" ] """.format(
                r['ticketNo'], r['cat_id'], r['src_interface'], r['host'], r['port_status'], r['path'], r['flap'],
                r['problem_status'], r['affected_item'], r['device_time'], r['hostname'], r['timestamp']
            )
            json_data.append(json.loads(tmp))
        print json.dumps(json_data)

    def link(self):
        from src_script.MySQL import Database

        db = Database()
        select_catid = """SELECT * FROM splunk 
                            LEFT JOIN (SELECT * FROM tts ORDER BY ticketNo DESC) AS tts ON (splunk.cat_id = tts.cat_id)
                            LEFT join online_active ON (splunk.cat_id = online_active.catid) 
                            WHERE host LIKE '10.5.0%' 
                            GROUP BY src_interface, host, hostname, path
                            """
        lst_catid = db.query(select_catid)

        for l in lst_catid:
            print '<tr>'
            if l['incident_id'] is not None:
                print '         <td class="col-lg-1"><a href="activity.py?TicketNo={0}">{0}</a></td>'.format(
                    l['ticketNo'])
            else:
                print '         <td class="col-lg-1"></td>'
            if len(l['cat_id']) < 12:
                print '         <td class="col-lg-1">{0}</td>'.format(l['cat_id'])
            else:
                print '         <td class="col-lg-1"></td>'
            print '         <td class="col-lg-1">{0}</td>'.format(l['src_interface'])
            print '         <td class="col-lg-1 text-center"><div data-toggle="tooltip" data-placement="bottom" title="{1}">{0}</div></td>'.format(
                l['host'], l['hostname'])
            # print '<td class="col-lg-1">{0}</td>'.format(l['hostname'])
            # print '<td class="col-lg-1">{0}</td>'.format(l['device_time'])
            if (l['port_status'] == 'down' or l['port_status'] == 'Down'):
                print '         <td class="col-lg-1 port_status_down text-center"><div data-toggle="tooltip" data-placement="bottom" title="{1}">{0}</div></td>'.format(
                    l['port_status'], l['device_time'])
            else:
                print '         <td class="col-lg-1 port_status_up text-center"><div data-toggle="tooltip" data-placement="bottom" title="{1}">{0}</div></td>'.format(
                    l['port_status'], l['device_time'])
            print '         <td class="col-lg-1">{0}</td>'.format(
                l['path'])
            print '         <td class="col-lg-1">{0}</td>'.format(l['flap'])
            if l['problem_status'] is not None:
                print '         <td class="col-lg-1">{0}</td>'.format(l['problem_status'])
            else:
                print '         <td class="col-lg-1"></td>'
            print '         <td class="col-lg-1">{0}</td>'.format(l['affected_item'])
            if l['port_status'] == 'down' or l['port_status'] == 'Down' and (
                    l['problem_status'] == 'Closed' or l['problem_status'] is None):
                if l['timestamp'] is not None:
                    t = datetime.datetime.strptime(str(l['timestamp']), '%Y-%m-%d %H:%M:%S')
                    timediff = abs((time.mktime(t.timetuple()) + 3600) - time.mktime(
                        datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).timetuple()))
                    if timediff < 120:
                        status = 'disabled'
                    else:
                        status = ''
                else:
                    status = ''
                print '         <td class="col-lg-1"><a href="openticket.py?cat_id={0}"><input type="button" class="btn btn-default" value="open ticket" {1}></a></td>'.format(
                    l['cat_id'], status)
            else:
                print '         <td class="col-lg-1"></td>'
            print '</tr>'
