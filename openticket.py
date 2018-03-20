#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
from src_script.template import template_AT

cgitb.enable()
t = template_AT()


def open_ticket():
    import datetime
    import pytz
    import cgi
    from src_script.MySQL import Database
    form = cgi.FieldStorage()
    db = Database(host='localhost', username='root', password='', db='alarm_ticket')
    query_detail = """SELECT * FROM tts WHERE cat_id = '{0}'""".format(form["cat_id"].value)
    lst_detail = db.query(query_detail)

    lst_detail = lst_detail[0]
    print '<div class="box">'
    print '<div class="box-form">'
    print '<div class="box-header">'
    print '<h2> open ticket </h2>'
    print '</div>'
    print '<div class="box-body">'
    # action="/cgi-enabled/checkvalue.py" method="post" name="ticket_form"

    print '<form class="form-horizontal" id="form_openticket">'

    print '<div class="column">'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="status"> Status </label>'
    print '<div class="col-sm-6">'
    print '<input type="text" readonly class="form-control" id="status" name="status" value="open">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2" for="catid"> CAT ID <font color="red">*</font></label>'
    print '<div class="col-sm-6">'
    print '<input type="text" readonly  class="form-control" id="catid" name="catid" value="{0}">'.format(lst_detail['cat_id'])
    print '</div>'
    print '</div>'

    if lst_detail['oss_source']== None:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Name <font color="red">*</font></label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="source" name="source" value="">'
        print '</div>'
        print '</div>'
    else:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Name <font color="red">*</font></label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="source" name="source" value="{0}" readonly>'.format(
            lst_detail['oss_source'])
        print '</div>'
        print '</div>'

    if lst_detail['oss_destination']=='':
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Destination</label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="destination" name="destination" value="">'
        print '</div>'
        print '</div>'
    else:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Destination</label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="destination" name="destination" value="{0}" readonly>'.format(
            lst_detail['oss_destination'])
        print '</div>'
        print '</div>'

    if lst_detail['address'] == '':
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Address </label>'
        print '<div class="col-sm-6">'
        print '<textarea type="text" class="form-control" id="address" name="address" rows="5"></textarea>'
        print '</div>'
        print '</div>'
    else:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Address </label>'
        print '<div class="col-sm-6">'
        print '<textarea type="text" class="form-control" id="address" name="address" rows="5" readonly>{0}</textarea>'.format(
            lst_detail['address'])
        print '</div>'
        print '</div>'


    if lst_detail['bandwidth'] == '':
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Bandwidth <font color="red">*</font> </label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="bandwidth" name="bandwidth" value="">'
        print '</div>'
        print '</div>'
    else:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Bandwidth <font color="red">*</font> </label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="bandwidth" name="bandwidth" value="{0}" readonly>'.format(
            lst_detail['bandwidth'])
        print '</div>'
        print '</div>'



    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Fault Time <font color="red">*</font></label>'
    print '<div class="col-sm-6">'
    print '<input type="text" class="form-control" id="faulttime" name="faulttime" value="{0}" readonly>'.format(
        datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%d/%m/%Y %H:%M:%S'))
    print '</div>'
    print '</div>'


    if lst_detail['owner_group'] == '':
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Owner Group <font color="red">*</font></label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="owner.group" name="owner.group" value="">'
        print '</div>'
        print '</div>'
    else:
        print '<div class="form-group">'
        print '<label class="control-label col-sm-2"> Owner Group <font color="red">*</font></label>'
        print '<div class="col-sm-6">'
        print '<input type="text" class="form-control" id="owner.group" name="owner.group" value="{0}" readonly>'.format(
            lst_detail['owner_group'])
        print '</div>'
        print '</div>'
    print '</div>'

    print '<div class="column">'
    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Title <font color="red">*</font></label>'
    print '<div class="col-sm-6">'
    print '<input type="text" class="form-control" id="title" name="title">'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> Description <font color="red">*</font></label>'
    print '<div class="col-sm-6">'
    print '<textarea type="text" class="form-control" id="description" name="description" rows="5"></textarea>'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print '<label class="control-label col-sm-2"> comment </label>'
    print '<div class="col-sm-6">'
    print '<textarea type="text" class="form-control" id="comment" name="comment" rows="5"></textarea>'
    print '</div>'
    print '</div>'

    print '<div class="form-group">'
    print ' <div class="col-sm-8">'
    print '     <button class="btn btn-default pull-right" type="submit">Submit</button>'
    print ' </div>'
    print '</div>'

    print '</div>'
    print '</div>'

    print '</form>'

    print '</div>'
    print '</div>'
    print '</div>'


if __name__ == "__main__":
    t.print_header()
    t.print_menu()

    open_ticket()
    t.print_close()
