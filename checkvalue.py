#!/usr/bin/env python

import cgi
import cgitb
import json
print "Content-type: application/json\n\n"
cgitb.enable()
def read_text():
    raw = cgi.FieldStorage()

    # form = cgi.FieldStorage()
    # variable = ""
    # value = ""
    # r = ""
    # for key in form.keys():
    #     variable = str(key)
    #     value = str(form.getvalue(variable))
    #     r += variable + ":" + value + "\n"
    # fieds = str(r)



    # values={}
    # values["interaction"]=raw.getvalue('interaction')
    # values["customertype"] = raw.getvalue('customertype')
    # values["status"] = raw.getvalue('status')
    # values["recipients"] = raw.getvalue('recipients')
    # values["incident"] = raw.getvalue('incident')
    # values["informant"] = raw.getvalue('informant')
    # values["catid"] = raw.getvalue('catid')
    # values["email"] = raw.getvalue('email')
    # values["source"] = raw.getvalue('source')
    # values["recipients"] = raw.getvalue('recipients')
    # values["phonenumber"] = raw.getvalue('phonenumber')
    # values["address"] = raw.getvalue('address')
    # values["sms"] = raw.getvalue('sms')
    # values["projectname"] = raw.getvalue('projectname')
    # values["bandwidth"] = raw.getvalue('bandwidth')
    # values["recipients"] = raw.getvalue('recipients')
    # values["partnername"] = raw.getvalue('partnername')
    # values["impact"] = raw.getvalue('impact')
    # values["urgency"] = raw.getvalue('urgency')
    # values["affectedservice"] = raw.getvalue('affectedservice')
    # values["affected_cl"] = raw.getvalue('affected_cl')
    # values["faulttime"] = raw.getvalue('faulttime')
    # values["recipients"] = raw.getvalue('recipients')
    # values["uptime"] = raw.getvalue('uptime')
    # values["assignment"] = raw.getvalue('assignment')
    # values["totaltime"] = raw.getvalue('totaltime')
    # values["EndToEnd_group"] = raw.getvalue('EndToEnd_group')
    # values["sla_target_date"] = raw.getvalue('sla_target_date')
    # values["EndToEnd_group"] = raw.getvalue('EndToEnd_group')
    # values["repair_team"] = raw.getvalue('repair_team')
    # values["title"] = raw.getvalue('title')
    # values["description"] = raw.getvalue('description')
    # values["comment"] = raw.getvalue('comment')
    # print "{0}".format(values)




if __name__ == '__main__':
    # read_text()
    raw = cgi.FieldStorage()
    if raw.getvalue('form_ticket'):
        text_content = raw.getvalue('cat_id')
    else:
        text_content = "Not entered"

    print text_content

    cat_id=raw.getvalue('cat_id')
    cat_id = raw.getvalue('cat_id')
    print cat_id
