#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import cgi
import collections
import datetime
import time
import pytz
from MySQL import Database

form = cgi.FieldStorage()
cgitb.enable()

db = Database()


def addactive(catid):
    select_active = db.query("SELECT * FROM online_active WHERE catid = '{}'".format(catid))
    if len(select_active) > 0:
        select_active = select_active[0]
        now = datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%Y-%m-%d %H:%M:%S')
        db.insert("""UPDATE online_active SET timestamp = '{1}' WHERE catid = '{0}'""".format(catid, now))
    else:
        now = datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).strftime('%Y-%m-%d %H:%M:%S')
        db.insert("""INSERT INTO online_active (catid, timestamp) VALUE ('{0}', '{1}')""".format(catid, now))

def getactive(catid):
    data = collections.OrderedDict()
    data['catid'] = catid
    data['timestamp'] = '1997-01-01 00:00:00'

    select_active = db.query("SELECT * FROM online_active WHERE catid = '{}' LIMIT 1".format(catid))
    if not len(select_active) == 0:
        select_active = select_active[0]
        data['timestamp'] = select_active['timestamp']
        t = datetime.datetime.strptime(str(data['timestamp']), '%Y-%m-%d %H:%M:%S')
        while abs(time.mktime(t.timetuple()) - time.mktime(datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).timetuple())) < 60:
            data['active'] = True
    return data


if __name__ == "__main__":
    print "Content-type: application/x-www-form-urlencoded\n\n"
    # print "Content-type: text/html\n\n"
    # print
    # t = datetime.datetime.strptime(str(db.query("SELECT * FROM online_active WHERE catid = '{}' LIMIT 1".format('TBB160382'))[0]['timestamp']), '%Y-%m-%d %H:%M:%S')
    # print abs(time.mktime(t.timetuple()) - time.mktime(datetime.datetime.now(tz=pytz.timezone('Asia/Bangkok')).timetuple()))
    type_func = form['type'].value
    if type_func == 'get':
        pass
        # print getactive(form['CatID'].value)
    elif type_func == 'report':
        addactive(form['CatID'].value)
    elif type_func == 'reduce':
        pass

