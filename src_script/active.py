#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgitb
import cgi
import collections
from MySQL import Database

form = cgi.FieldStorage()
cgitb.enable()

db = Database(host='127.0.0.1', username='root', password='', db='alarm_ticket')


def addactive(catid):
    select_active = db.query("SELECT * FROM online_active WHERE catid = '{}' LIMIT 1".format(catid))
    if len(select_active) == 0:
        db.insert("""INSERT INTO online_active (catid) VALUE ('{}')""".format(catid))
    else:
        select_active = select_active[0]
        db.insert("""UPDATE online_active SET active = '{1}' WHERE catid = '{0}'""".format(catid, select_active['active'] + 1))


def reduceactive(catid):
    select_active = db.query("SELECT * FROM online_active WHERE catid = '{}' LIMIT 1".format(catid))
    if not len(select_active) == 0:
        select_active = select_active[0]
        active_count = select_active['active']
        if active_count == 0:
            db.insert("""UPDATE online_active SET active = '{1}' WHERE catid = '{0}'""".format(catid, 0))
        else:
            db.insert("""UPDATE online_active SET active = '{1}' WHERE catid = '{0}'""".format(catid, active_count - 1))


def getactive(catid):
    data = collections.OrderedDict()
    data['catid'] = catid
    data['active'] = 0

    select_active = db.query("SELECT * FROM online_active WHERE catid = '{}' LIMIT 1".format(catid))
    if not len(select_active) == 0:
        select_active = select_active[0]
        data['active'] = select_active['active']
    return data


if __name__ == "__main__":
    type_func = form['type'].value

    if type_func == 'get':
        pass
    elif type_func == 'add':
        pass
    elif type_func == 'reduce':
        pass
