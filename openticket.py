#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
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
    db = Database()
    query_detail = """SELECT * FROM tts WHERE cat_id = '{0}'""".format(form["cat_id"].value)
    query_splunk = """SELECT * FROM splunk WHERE cat_id = '{0}'""".format(form["cat_id"].value)
    lst_detail = db.query(query_detail)
    lst_splunk = db.query(query_splunk)
    lst_splunk=lst_splunk[0]

    if len(lst_detail) > 0:
        lst_detail = lst_detail[0]
    else:
        lst_detail = collections.OrderedDict()
        lst_detail['ticketNo'] = None
        lst_detail['incident_id'] = None
        lst_detail['affected_item'] = None
        lst_detail['cat_id'] = None
        lst_detail['status'] = None
        lst_detail['problem_status'] = None
        lst_detail['downtime_start'] = None
        lst_detail['downtime_time'] = None
        lst_detail['owner_group'] = None
        lst_detail['repairteam'] = None
        lst_detail['oss_source'] = None
        lst_detail['oss_destination'] = None
        lst_detail['address'] = None
        lst_detail['title'] = None
        lst_detail['description'] = None
        lst_detail['activity'] = None
        lst_detail['bandwidth'] = None
    print '<input type=hidden id=CatID name=CatID value="{}">'.format(form["cat_id"].value)

    print '<div class="box">'
    print '<div class="box-form">'
    print '<div class="box-header">'
    print '<h2> open ticket </h2>'
    print '</div>'
    print '<div class="box-body">'
    # action="/cgi-enabled/checkvalue.py" method="post" name="ticket_form"

    print '<form id="form_openticket">'

    print '<div class="column col-lg-5">'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right" for="status"> Status </label>'
    print '<div class="col-sm-9">'
    print '<input type="text" readonly class="form-control" id="status" name="status" value="open">'
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right" for="catid"> CAT ID <font color="red">*</font></label>'
    print '<div class="col-sm-9">'
    print '<input type="text" readonly  class="form-control" id="catid" name="catid" value="{0}">'.format(form.getvalue('cat_id'))
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right" for="catid"> Hostname </label>'
    print '<div class="col-sm-9">'
    print '<input type="text" readonly  class="form-control" id="hostname" name="hostname" value="{0}">'.format(
       lst_splunk['hostname'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right" for="catid"> IP</label>'
    print '<div class="col-sm-9">'
    print '<input type="text" readonly  class="form-control" id="ip" name="ip" value="{0}">'.format(
        lst_splunk['host'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right" for="catid"> Source Interface </label>'
    print '<div class="col-sm-9">'
    print '<input type="text" readonly  class="form-control" id="interface" name="interface" value="{0}">'.format(
        lst_splunk['src_interface'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Name <font color="red">*</font></label>'
    print '<div class="col-sm-9">'
    print '<input type="text" class="form-control" id="source" name="source" value="{0}" readonly>'.format(
        lst_detail['oss_source'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Destination</label>'
    print '<div class="col-sm-9">'
    print '<input type="text" class="form-control" id="destination" name="destination" value="{0}" readonly>'.format(
        lst_detail['oss_destination'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Address </label>'
    print '<div class="col-sm-9">'
    print '<textarea type="text" class="form-control" id="address" name="address" rows="5" readonly>{0}</textarea>'.format(
        lst_detail['address'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Bandwidth <font color="red">*</font> </label>'
    print '<div class="col-sm-9">'
    print '<input type="text" class="form-control" id="bandwidth" name="bandwidth" value="{0}" readonly>'.format(
        lst_detail['bandwidth'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Fault Time <font color="red">*</font></label>'
    print '<div class="col-sm-9">'
    print '<input type="text" class="form-control" id="faulttime" name="faulttime" value="{0}" readonly>'.format(
        datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%d/%m/%Y %H:%M:%S'))
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-3 text-right"> Owner Group <font color="red">*</font></label>'
    print '<div class="col-sm-9">'
    print '<input type="text" class="form-control" id="owner.group" name="owner.group" value="{0}" readonly>'.format(
        lst_detail['owner_group'])
    print '</div>'
    print '</div>'

    print '</div>'

    print '<div class="column col-lg-7">'
    print '<div class="form-group row">'
    print '<label class="control-label col-sm-2 text-right"> Title <font color="red">*</font></label>'
    print '<div class="col-sm-10">'
    print """
        <select class="form-control" name="title">
            <option value="Down">Down</option>
            <option value="Up-Down/Bouncing/Flapping/TimeOut/Drop/Loss">Up-Down/Bouncing/Flapping/TimeOut/Drop/Loss</option>
            <option value="Error">Error</option>
            <option value="ช้า/Delay/Low Speed/ใช้งานได้ไม่เต็ม Bandwidth">ช้า/Delay/Low Speed/ใช้งานได้ไม่เต็ม Bandwidth</option>
            <option value="ลูกค้าขอเช็ค Alarm<">ลูกค้าขอเช็ค Alarm</option>
            <option value="ลูกค้าขอ Monitor">ลูกค้าขอ Monitor</option>
            <option value="ลูกค้าขอ Test">ลูกค้าขอ Test</option>
            <option value="SmartSignOn ใช้งานไม่ได้">SmartSignOn ใช้งานไม่ได้</option>
            <option value="C internet Login ไม่ได้">C internet Login ไม่ได้</option>
            <option value="C internet เปิดเว็บไม่ได้">C internet เปิดเว็บไม่ได้</option>'
            <option value="C internet รับ-ส่ง Email Outlook ไม่ได้">C internet รับ-ส่ง Email Outlook ไม่ได้</option>
            <option value="C internet ค่า Ping Time สูง">C internet ค่า Ping Time สูง</option>
            <option value="Config อุปกรณ์ไม่ได้">Config อุปกรณ์ไม่ได้</option>
            <option value="ทำ VPN ไม่ได้">ทำ VPN ไม่ได้</option>
            <option value="ทำ Load balance ไม่ได้">ทำ Load balance ไม่ได้</option>
            <option value="ภัยพิบัติ">ภัยพิบัติ</option>
            <option value="Phishing">Phishing</option>
            <option value="Attack">Attack</option>
            <option value="IP Phishing">IP Phishing</option>
            <option value="IP Attack">IP Attack</option>
            <option value="IP Hacking">IP Hacking</option>
            <option value="IP RBL">IP RBL</option>
            <option value="High Latency">High Latency</option>
            <option value="สาเหตุอื่นๆ">สาเหตุอื่นๆ</option>
            <option value="Down 3G">Down 3G</option>
            <option value="Down 3G/SA1">Down 3G/SA1</option>
            <option value="Down 3G/SA2">Down 3G/SA2</option>
            <option value="Down 3G/SA3">Down 3G/SA3</option>
            <option value="Down 3G/SA4">Down 3G/SA4</option>
            <option value="Down 3G/NSA1">Down 3G/NSA1</option>
            <option value="Down 3G/NSA2">Down 3G/NSA2</option>
            <option value="Down 3G/NSA3">Down 3G/NSA3</option>
            <option value="Down 3G/NSA4">Down 3G/NSA4</option>
            <option value="Help check: Link status (Up/Down)">Help check: Link status (Up/Down)</option>
            <option value="Help check: Power of equipment status (On/Off)">Help check: Power of equipment status (On/Off)</option>
            <option value="Help check: Power system down">Help check: Power system down</option>
        </select>
    """
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-2 text-right"> Description <font color="red">*</font></label>'
    print '<div class="col-sm-10">'
    print """<textarea type="text" class="form-control" id="description" name="description" rows="10">พบ Link_Down
ข้อมูลต้นทาง
   Nodename :{0}
   IP  :{1}
   Interface :{2}
   Location : 
   TX power : 
   RX power: 
   Log :

ข้อมูลปลายทาง
   Nodename :
   IP  :
   Interface :
   Location : 
   TX power : 
   RX power: 
   Log :</textarea>""".format(lst_splunk['hostname'], lst_splunk['host'], lst_splunk['src_interface'])
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '<label class="control-label col-sm-2 text-right"> comment </label>'
    print '<div class="col-sm-10">'
    print '<textarea type="text" class="form-control" id="comment" name="comment" rows="5"></textarea>'
    print '</div>'
    print '</div>'

    print '<div class="form-group row">'
    print '''
    <div class="pull-right">
        <div class="col-lg-6">
            <a class="btn btn-default pull-right" href="index.py">Cancel</a>
        </div>
        <div class="col-lg-6">
            <button class="btn btn-default pull-right" type="submit">Submit</button>
        </div>
    </div>'''
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
