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
    print '<input type="text" class="form-control" id="informant" name="informant" value="CATMA">'
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
    print '<label class="control-label col-sm-2"> Category <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="category" name="category" value="\x49\x6E\x63\x69\x64\x65\x6E\x74\x20\x0A">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Bandwidth <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="bandwidth" name="bandwidth" value="{0}">'.format(lst_detail['bandwidth'])
    print '</div>'
    print '<label class="control-label col-sm-2"> area </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="subcategory" name="subcategory" value="\x66\x61\x69\x6C\x75\x72\x65\x0A">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Partners Name </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="partnername" name="partnername">'
    print '</div>'
    print '<label class="control-label col-sm-2"> subarea </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="product_type" name="product_type" value="system down">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Carrier Name </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="carrier.name" name="carrier.name">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Impact <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="impact" name="impact" value="\x33\x20\x2D\x20\x4D\x75\x6C\x74\x69\x70\x6C\x65\x20\x55\x73\x65\x72\x73">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Carrier Ticket </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="carrier.ticket" name="carrier.ticket">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Urgency <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="urgency" name="urgency" value="\x33\x20\x2D\x20\x41\x76\x65\x72\x61\x67\x65">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Affected Service <font color="red">*</font> </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="affectedservice" name="affectedservice" value="\xE0\xB8\x9A\xE0\xB8\xA3\xE0\xB8\xB4\xE0\xB8\x81\xE0\xB8\xB2\xE0\xB8\xA3\x20\x43\x41\x54\x20\x45\x50\x4C\x20\x2D\x20\x44\x6F\x6D\x65\x73\x74\x69\x63\x0A">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Affected Cl <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="affected_cl" name="affected_cl">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Owner Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="owner.group" name="owner.group" value="{0}" readonly>'.format(
        lst_detail['owner_group'])
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Fault Time <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="faulttime" name="faulttime" value="{0}">'.format(datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%d/%m/%Y %H:%M:%S'))
    print '</div>'
    print '<label class="control-label col-sm-2"> Assignment Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="assignment" name="assignment" value="\xE0\xB8\xA1\xE0\xB8\x82\x2E\x20\x43\x6F\x72\x65\x20\x4E\x65\x74\x77\x6F\x72\x6B\x2F\xE0\xB8\xA1\xE0\xB8\xA1\x2E">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Up Time <font color="red">*</font></label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="uptime" name="uptime">'
    print '</div>'
    print '<label class="control-label col-sm-2"> EndToEnd Group </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="EndToEnd_group" name="EndToEnd_group">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Total Down Time </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="totaltime" name="totaltime">'
    print '</div>'
    print '<label class="control-label col-sm-2"> Repair Team </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" id="repair_team" name="repair_team">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> SLA Target Date </label>'
    print '<div class="col-sm-4">'
    print '<input type="text" class="form-control" readonly="" id="sla_target_date" name="sla_target_date">'
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
