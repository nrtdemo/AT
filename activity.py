#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src_script.template import template_AT
import cgitb

t = template_AT()
cgitb.enable()


def index():
    import cgi
    import json
    import random
    from src_script.MySQL import Database
    form = cgi.FieldStorage()
    db = Database()
    select_catid = """SELECT * FROM tts WHERE ticketNo = '{0}' LIMIT 1""".format(form["TicketNo"].value)
    lst_catid = db.query(select_catid)

    if 'TicketNo' not in form or len(lst_catid) == 0:
        t.redirect()
    else:
        lst_catid = lst_catid[0]
        activity = json.loads(lst_catid['activity'])

        print '<div class="box">'
        print '<div class="box-body container">'

        print '<div class="col-lg-6">'
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Ticket No:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['ticketNo'])

        print """
                <div class="row form-group">
                    <div class="col-lg-3">Incident id:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['incident_id'])
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Cat id:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['cat_id'])
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Affected item:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['affected_item'])
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Status:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['status'])
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Problem status:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['problem_status'])
        print """
                <div class="row form-group">
                    <div class="col-lg-3">Address:</div>
                    <div class="col-lg-9">{0}</div>
                </div>
                """.format(lst_catid['address'])
        print '</div>'

        print '<div class="col-lg-6">'
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Downtime start:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['downtime_start'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Downtime:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['downtime_time'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Owner group:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['owner_group'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Repairteam:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['repairteam'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Source:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['oss_source'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Destination:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['oss_destination'])
        print """
               <div class="row form-group">
                   <div class="col-lg-3">Bandwidth:</div>
                   <div class="col-lg-9">{0}</div>
               </div>
               """.format(lst_catid['bandwidth'])
        print '</div>'

        # INFORMATION LINK
        print '''
        <div class="col-lg-12">
            <div class="row form-group">
                <div class="col-lg-2" >Title:</div>
                <div class="col-lg-10"><input type="text" class="form-control" value="{}" readonly></div>
            </div>
            <div class="row form-group">
                <div class="col-lg-2" >Description:</div>
                <div class="col-lg-10"><textarea class="form-control" rows="20" readonly >{}</textarea></div>
            </div>
        </div>
        '''.format(lst_catid['title'], lst_catid['description'])

        # TABLE ACTIVITY
        print '<div class="col-lg-12">'
        print """
        <div class="row form-group">
            <div class="col-lg-2"> Activities:</div>
            <div class="col-lg-10 table-responsive">
                <table class="table table-bordered table-striped">
                    <thead>
                        <tr class="Bg-head-table">
                            <th class="col-lg-1 text-center"> Number </th>
                            <th class="col-lg-2 text-center"> Datetime </th>
                            <th class="col-lg-2 text-center"> Operator </th>
                            <th class="col-lg-2 text-center"> Division </th>
                            <th class="col-lg-3 text-center"> Description </th>
                            <th class="col-lg-1 text-center"> Type </th>
                        </tr>
                    </thead>
                    <tbody>
        """
        for i in activity:
            print '<tr>'
            print '<td class="text-center" >{0}</td>'.format(i['number'])
            print '<td class="text-center" >{0}</td>'.format(i['datestamp'])
            print "<td>{0}</td>".format(i['operator'].encode('utf-8'))
            print "<td>{0}</td>".format(i['division'].encode('utf-8'))
            print "<td>{0}</td>".format(i['description'].encode('utf-8'))
            print "<td>{0}</td>".format(i['type'])
            print "</tr>"
        print """
                    </tbody>
                </table>
            </div>
        </div>
        """
        print "</div>"

        ###############################
        print "</div>"
        print "</div>"


if __name__ == "__main__":
    t.print_header()
    t.print_menu()
    index()
    t.print_close()
