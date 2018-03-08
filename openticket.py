#!/usr/bin/env python

import cgitb

cgitb.enable()


def open_ticket():
    import datetime
    import pytz
    import cgi
    from src_script.MySQL import Database
    form = cgi.FieldStorage()
    db = Database(host='localhost', username='root', password='', db='alarm_ticket')
    query_detail = """SELECT * FROM tts WHERE cat_id = '{0}'""".format(form["cat_id"].value)
    lst_detail = db.query(query_detail)[0]

    print '<div class="box">'
    print '<div class="box-form">'
    print '<div class="box-header">'
    print '<h2> open ticket </h2>'
    print '</div>'
    print '<div class="box-body">'

    print '<form class="form-horizontal" action="/cgi-enabled/checkvalue.py" method="post" name="ticket_form">'
    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="interaction"> interaction ID(Ticket) </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" readonly class="form-control" id="interaction" name="interaction">'
    print '</div>'
    print '<label class="control-label col-sm-2" for="customertype"> Customer Type </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="customertype" name="customertype">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="status"> Status </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" readonly class="form-control" id="status" name="status" value="open">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Recipients </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" readonly class="form-control" id="recipients" name="recipients" value="catma">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="incidentid"> Incident ID </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" readonly class="form-control" id="incident" name="incident">'
    print '</div>'
    print '<label class="control-label col-sm-2" for="informant"> Informant </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="informant" name="informant" value="catma">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="catid"> CAT ID <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="catid" name="catid" value="{0}">'.format(lst_detail['cat_id'])
    print '</div>'
    print '<label class="control-label col-sm-2" for="email"> E-mail </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="email" name="email" value="catma@ait.co.th">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Name <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="source" name="source" value="{0}">'.format(lst_detail['oss_source'])
    print '</div>'
    print '<label class="control-label col-sm-2"> Phone number </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="phonenumber" name="phonenumber" value="021041761">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Destination</label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="destination" name="destination" value="{0}">'.format(lst_detail['oss_destination'])
    print '</div>'
    print '<label class="control-label col-sm-2">SMS</label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="sms" name="sms">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Address </label>'
    print '<div class="col-sm-4">'
    print '<textarea type="text" class="form-control" id="address" name="address" rows="5">{0}</textarea>'.format(lst_detail['address'])
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Bandwidth <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="bandwidth" name="bandwidth">'
    print '</div>'
    print '<label class="control-label col-sm-2"> area </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="category" name="category">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Partners Name </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="partnername" name="partnername">'
    print '</div>'
    print '<label class="control-label col-sm-2"> subarea </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="subcategory" name="subcategory">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Carrier Name </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="carrier.name" name="carrier.name">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Impact <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="impact" name="impact">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Carrier Ticket </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="carrier.ticket" name="carrier.ticket">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Urgency <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="urgency" name="urgency">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Affected Service <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="affectedservice" name="affectedservice">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Affected Cl <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="affected_cl" name="affected_cl">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Urgency </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="severity" name="severity">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Fault Time <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="faulttime" name="faulttime" value="{0}">'.format(datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%d/%m/%Y %H:%M:%S'))
    print '</div>'
    print '<label class="control-label col-sm-2"> Owner Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="owner.group" name="owner.group" value="{0}">'.format(lst_detail['owner_group'])
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Up Time <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="uptime" name="uptime">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Assignment Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="assignment" name="assignment">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Total Down Time </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="totaltime" name="totaltime">'
    print '</div>'
    print '<label class="control-label col-sm-2"> EndToEnd Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="EndToEnd_group" name="EndToEnd_group">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> SLA Target Date </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="sla_target_date" name="sla_target_date">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Repair Team </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="repair_team" name="repair_team">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Title <font color="red">*</font></label>'
    print '<div class="col-sm-10">'
    print '<input type="text" class="form-control" id="title" name="title">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Description <font color="red">*</font></label>'
    print '<div class="col-sm-2"></div>'
    print '<div class="col-sm-10">'
    print '<textarea type="text" class="form-control" id="description" name="description" rows="5"></textarea>'
    print '</div>'
    print '<label class="control-label col-sm-2"> comment </label>'
    print '<div class="col-sm-2"></div>'
    print '<div class="col-sm-10">'
    print '<textarea type="text" class="form-control" id="comment" name="comment" rows="5"></textarea>'
    print '</div>'
    print '</div>'
    print '<div class="form-group">'
    print ' <div class="col-sm-12">'
    print '     <button class="btn btn-default pull-right" type="submit">Submit</button>'
    print ' </div>'
    print '</div>'


    print '</form>'

    print '</div>'
    print '</div>'


if __name__ == "__main__":
    from src_script.template import template_AT

    t = template_AT()
    t.print_header()
    t.print_menu()

    open_ticket()
    t.print_close()
