#!/usr/bin/python -u
import time
import re
import threading

from MySQL import Database
from tts_v1 import TTS
from splunk import SPLUNK

db = Database(host='127.0.0.1', username='root', password='', db='alarm_ticket')

# SPLUNK
splunk_baseurl = 'https://10.4.0.136:8089'
# splunk_baseurl = 'https://192.168.100.2:8089'
splunk = SPLUNK('admin', 'P@ssw0rd', splunk_baseurl)

# TTS
TTS_basehost = "122.155.137.214"
tts = TTS('catma', 'ait@1761', TTS_basehost)


def get_catid(l):
    cat_id = l['host'] + l['src_interface']
    splitcatid = l['cat_id'].split('_')

    if len(splitcatid[0]) >= 9:
        cat_id = re.search('(\w+)', splitcatid[0])
        if cat_id:
            cat_id = cat_id.group(1)
            if len(cat_id) < 9:
                cat_id = l['host'] + l['src_interface']
    elif len(splitcatid[1]) >= 9:
        cat_id = re.search('(\w+)', splitcatid[1])
        if cat_id:
            cat_id = cat_id.group(1)
            if len(cat_id) < 9:
                cat_id = l['host'] + l['src_interface']
    elif splitcatid[0] == 'MPLS':
        sub_catid = re.search('CATID:(.*)', l['cat_id'])
        if sub_catid:
            cat_id = sub_catid.group(1)
            if len(cat_id) < 9:
                cat_id = l['host'] + l['src_interface']
    return cat_id


def insert_Splunk(lst_splunk):
    for l in lst_splunk:
        catid = get_catid(l)
        insert_query = """
                            INSERT INTO splunk
                            (cat_id, path, port_status, src_interface, host, flap, hostname, device_time)
                            VALUES
                            """

        if len(catid) >= 9:
            check_query = """
                SELECT splunk_id FROM splunk WHERE host='{0}' AND hostname='{1}' AND path='{2}' AND src_interface='{3}'
                """.format(l['host'], l['hostname'], l['cat_id'], l['src_interface'])
            getsplunk = db.query(check_query)
            if len(getsplunk) > 0:
                getsplunk = getsplunk[0]
                sql_update_port_status = """
                                UPDATE `splunk` SET `port_status`='{0}',`flap`='{1}', cat_id='{3}' WHERE splunk_id='{2}'
                                """.format(l['port_status'], l['flap'], getsplunk['splunk_id'], catid)
                db.insert(sql_update_port_status)
                print "UPDATE DONE"
            else:
                insert_query += "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
                    str(catid), str(l['cat_id']), str(l['port_status']), str(l['src_interface']),
                    str(l['host']), str(l['flap']), str(l['hostname']), str(l['device_time']))
                db.insert(insert_query)
                print "INSERT DONE"
        else:
            insert_query += "('', '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(
                str(l['cat_id']), str(l['port_status']), str(l['src_interface']),
                str(l['host']), str(l['flap']), str(l['hostname']), str(l['device_time']))
            db.insert(insert_query)
            print "INSERT DONE"


def insert_TTS(lst_catid):
    lst = []
    for c in lst_catid:
        if len(c['cat_id']) < 10:
            lst.append(tts.Search(c['cat_id']))

    for l in lst:
        if l is not None:
            activity_table = ""
            ticket_info = tts.Get_TicketInfo(l['incident_id'])
            for t in ticket_info['activity_table']:
                date = str(t['datestamp']).split('/')
                year = date[2].split(' ')
                datetime = year[0] + '-' + date[1] + '-' + date[0] + ' ' + year[1]

                activity = '''"number": {0}, "datestamp": "{1}", "operator": "{2}", "division": "{3}", "description": "{4}", "type": "{5}"'''.format(
                    t['number'], datetime, t['operator'].encode('utf-8'), t['division'].encode('utf-8'),
                    t['description'].encode('utf-8'), t['type'].encode('utf-8')
                )
                activity = '{' + activity + '},'
                activity_table = activity_table + activity
            activity_table = activity_table[:-1]
            activity_table = '[' + activity_table + ']'

            insert_query = """INSERT INTO `tts`(`ticketNo`,`incident_id`, `affected_item`, `cat_id`, `status`, `problem_status`, `downtime_start`, `downtime_time`, `owner_group`, `repairteam`, `oss_source`, `oss_destination`, `address`, `title`, `description`, `activity`, `bandwidth`) VALUES """
            value = "\n('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}')".format(
                l['incident_id'], l['number'], l['affected_item'].encode('utf-8'), l['catid'].encode('utf-8'), l['status'], l['problem_status'], l['downtime_start'], l['downtime'],
                l['owner_group'].encode('utf-8'), l['repairteam'].encode('utf-8'), l['oss_source'].encode('utf-8'), l['oss_destination'].encode('utf-8'),
                ticket_info['instance/oss.address/oss.address'].encode('utf-8'), ticket_info['instance/brief.description'].encode('utf-8'),
                ticket_info['instance/action/action'].encode('utf-8'), activity_table, ticket_info['instance/oss.bandwidth'].encode('utf-8')
            )
            query = "{0} {1}".format(insert_query, value)
            # PrintDebug(query)
            resp_status = db.insert(query)
            if not resp_status:
                update_query = """ UPDATE `tts` SET `affected_item`='{0}',`status`='{1}',`problem_status`='{2}',`downtime_start`='{3}',`downtime_time`='{4}', `description`='{6}', `activity`='{7}' WHERE `ticketNo`='{5}' """.format(
                    l['affected_item'].encode('utf-8'), l['status'], l['problem_status'], l['downtime_start'], l['downtime'], l['incident_id'],
                    ticket_info['instance/action/action'].encode('utf-8'), activity_table)
                db.insert(update_query)
                # PrintDebug(update_query)
                # print 'UPDATE'
            else:
                print 'DONE'
    print 'ENDED TTS'


def job_SPLUNK(searchQuery):
    print 'Doing SPLUNK...'
    sid = splunk.CreateSearch(searchQuery, timerange="24hr")  # defind timerange query data
    # sid = splunk.CreateSearch(searchQuery)  # defind timerange query data
    print (sid)
    rs = splunk.GetSearchStatus(sid)
    while not rs == 'DONE':
        print rs
        time.sleep(15)
        rs = splunk.GetSearchStatus(sid)
    lst = splunk.GetSearchResult(sid)
    insert_Splunk(lst)
    print 'ENDED SPLUNK'


def job_TTS():
    print 'Doing TTS...'
    select_catid = """ SELECT `cat_id`,`host` FROM `splunk` GROUP BY cat_id"""
    lst_catid = db.query(select_catid)
    insert_TTS(lst_catid)


def PrintDebug(msg):
    if True:
        print msg


if __name__ == "__main__":
    search_link = 'cat_id="*TPK*" OR cat_id="*TBB*" eventtype="cisco_ios-port_down" OR eventtype="cisco_ios-port_up" host="10.5.0.*" OR "10.126.0.*" src_interface="POS*" OR "HundredGigE*" OR "TenGigE*" OR "TenGigabitEthernet*" | stats count as flap, latest(port_status) AS port_status, latest(device_time) AS device_time by host, hostname, src_interface, cat_id'
    search_link_40G_100GbE = 'eventtype="cisco_ios-port_down" OR eventtype="cisco_ios-port_up" cat_id="*TPK*" OR cat_id="*TBB*" host="10.126.0.*" src_interface="POS*" OR "HundredGigE*" | stats count as flap,latest(device_time) AS device_time,latest(port_status) AS port_status by host,hostname,src_interface,cat_id'
    search_link_PE_Bangkok_Flap = 'eventtype="cisco_ios-port_down" OR eventtype="cisco_ios-port_up" cat_id="*TPK*" OR cat_id="*TBB*" host="10.5.0.*" | stats count as flap,latest(device_time) AS device_time,latest(port_status) AS port_status by host,hostname,src_interface,cat_id'

    # job_SPLUNK(search_link)
    # job_TTS()

    t1 = threading.Thread(name='search_link_40G_100GbE', target=job_SPLUNK, args=(search_link_40G_100GbE,))
    t2 = threading.Thread(name='search_link_PE_Bangkok_Flap', target=job_SPLUNK, args=(search_link_PE_Bangkok_Flap,))
    t1.start()
    t2.start()

    while t1.isAlive() or t2.isAlive():
        print 'Script is working!!'
        time.sleep(30)
    job_TTS()
