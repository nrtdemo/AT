#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    print '<div class ="box">'
    print '<div class ="box-body container">'
    print '<div class ="box-form">'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right"> TicketNo:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['ticketNo'])
    print '<div class ="col-lg-2 text-right" > Downtime_start:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['downtime_start'])
    print '</div>'

    print '<div class ="row form-group" >'
    print '<div class ="col-lg-2 text-right" > Incident_id:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['incident_id'])
    print '<div class ="col-lg-2 text-right" > Downtime_time:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['downtime_time'])
    print '</div>'

    print '<div class ="row form-group" >'
    print '<div class ="col-lg-2 text-right"> Affected_item:</div>'
    print '<div class ="col-lg-4">{0}</div>'.format(lst_catid['affected_item'])
    print '<div class ="col-lg-2 text-right"> Owner_group:</div>'
    print '<div class ="col-lg-4">{0}</div>'.format(lst_catid['owner_group'])
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right" > Cat_id:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['cat_id'])
    print '<div class ="col-lg-2 text-right" > Repairteam: </div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['repairteam'])
    print '</div>'

    print '<div class ="row form-group" >'
    print '<div class ="col-lg-2 text-right" > Status:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['status'])
    print '<div class ="col-lg-2 text-right" > Oss_source:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['status'])
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right"> Problem_status:</div>'
    print '<div class ="col-lg-4" >{0}</div>'.format(lst_catid['problem_status'])
    print '<div class ="col-lg-2 text-right"> Oss_destination:</div>'
    print '<div class ="col-lg-4">{0}</div>'.format(lst_catid['oss_destination'])
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right" > Address:</div>'
    print '<div class ="col-lg-10 " >{0}</div>'.format(lst_catid['address'])
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right"> Title:</div>'
    print '<div class ="col-lg-10 ">{0}</div>'.format(lst_catid['title'])
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right" > Description:</div>'
    print '<div class ="col-lg-10 ">'
    print '<textarea class="form-control" rows="20" readonly >{0}</textarea>'.format(lst_catid['description'])
    print '</div>'
    print '</div>'

    print '<div class ="row form-group">'
    print '<div class ="col-lg-2 text-right"> Activities:</div>'
    print '<div class ="col-lg-10 table-responsive">'
    print '<table class ="table table-bordered table-striped">'
    print '<thead>'
    print '<tr class ="Bg-head-table">'
    print '<th class ="col-lg-1 text-center"> Number </th>'
    print '<th class ="col-lg-2 text-center"> Datetime </th>'
    print '<th class ="col-lg-2 text-center"> Operator </th>'
    print '<th class ="col-lg-2 text-center"> Division </th>'
    print '<th class ="col-lg-3 text-center"> Description </th>'
    print '<th class ="col-lg-1 text-center"> Type </th>'
    print '</tr>'
    print '</thead>'

    print '<tbody>'
    for i in activity:
        print '<tr>'
        print '<td class ="text-center" >{0}</td>'.format(i['number'])
        print '<td class ="text-center" >{0}</td>'.format(i['datestamp'])
        print "<td>{0}</td>".format(i['operator'].encode('utf-8'))
        print "<td>{0}</td>".format(i['division'].encode('utf-8'))
        print "<td>{0}</td>".format(i['description'].encode('utf-8'))
        print "<td>{0}</td>".format(i['type'])
        print "</tr>"
    print "</tbody>"
    print "</table>"

    print "</div>"
    print "</div>"
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
