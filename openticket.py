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

    if 'cat_id' not in form or len(lst_detail) == 0:
        t.redirect()
    else:
        lst_detail = lst_detail[0]
        print '<div class="box">'
        print '<div class="box-form">'
        print '<div class="box-header">'
        print '<h2> open ticket </h2>'
        print '</div>'
        print '<div class="box-body">'
        # action="/cgi-enabled/checkvalue.py" method="post" name="ticket_form"
        print '<form class="form-horizontal" id="form_openticket">'

        print '<div class="form-group">'
        print '<label class="control-label col-sm-2" for="status"> Status </label>'
        print '<div class="col-sm-4">'
        print '<input type="text" readonly class="form-control" id="status" name="status" value="open">'
        print '</div>'
        print '</div>'

        print '<div class="form-group">'
        print '<label class="control-label col-sm-2" for="catid"> CAT ID <font color="red">*</font></label>'
        print '<div class="col-sm-4">'
        print '<input type="text" class="form-control" id="catid" name="catid" value="{0}">'.format(lst_detail['cat_id'])
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
    t.print_header()
    t.print_menu()

    open_ticket()
    t.print_close()
