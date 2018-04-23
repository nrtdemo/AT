#!/usr/bin/env python
#
# Copyright 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""A command line utility for executing Splunk searches."""

from __future__ import absolute_import
import sys, os, json
from xml.etree import cElementTree as ET
from collections import defaultdict
from time import sleep
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from splunklib.binding import HTTPError
import splunklib.client as client
sys.path.append("/var/www/html/cgi-enabled")
from src_script.MySQL import Database
import re
db = Database(host='127.0.0.1', username='root', password='', db='alarm_ticket')

try:
    from utils import *
except ImportError:
    raise Exception("Add the SDK repository to your PYTHONPATH to run the examples "
                    "(e.g., export PYTHONPATH=~/splunk-sdk-python.")

FLAGS_TOOL = [ "verbose" ]

FLAGS_CREATE = [
    "earliest_time", "latest_time", "now", "time_format",
    "exec_mode", "search_mode", "rt_blocking", "rt_queue_size",
    "rt_maxblocksecs", "rt_indexfilter", "id", "status_buckets",
    "max_count", "max_time", "timeout", "auto_finalize_ec", "enable_lookups",
    "reload_macros", "reduce_freq", "spawn_process", "required_field_list",
    "rf", "auto_cancel", "auto_pause",
]

FLAGS_RESULTS = [
    "offset", "count", "search", "field_list", "f", "output_mode"
]
def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update((k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

def cmdline(argv, flags, **kwargs):
    """A cmdopts wrapper that takes a list of flags and builds the
       corresponding cmdopts rules to match those flags."""
    rules = dict([(flag, {'flags': ["--%s" % flag]}) for flag in flags])
    return parse(argv, rules, ".splunkrc", **kwargs)

def main_search(argv):
    usage = 'usage: %prog [options] "search"'

    flags = []
    flags.extend(FLAGS_TOOL)
    flags.extend(FLAGS_CREATE)
    flags.extend(FLAGS_RESULTS)
    opts = cmdline(argv, flags, usage=usage)

    if len(opts.args) != 1:
        error("Search expression required", 2)
    search = opts.args[0]

    verbose = opts.kwargs.get("verbose", 0)

    kwargs_splunk = dslice(opts.kwargs, FLAGS_SPLUNK)
    kwargs_create = dslice(opts.kwargs, FLAGS_CREATE)
    kwargs_results = dslice(opts.kwargs, FLAGS_RESULTS)

    service = client.connect(**kwargs_splunk)

    try:
        service.parse(search, parse_only=True)
    except HTTPError as e:
        cmdopts.error("query '%s' is invalid:\n\t%s" % (search, str(e)), 2)
        return

    job = service.jobs.create(search, **kwargs_create)
    while True:
        while not job.is_ready():
            pass
        stats = {'isDone': job['isDone'],
                 'doneProgress': job['doneProgress'],
                 'scanCount': job['scanCount'],
                 'eventCount': job['eventCount'],
                 'resultCount': job['resultCount']}
        progress = float(stats['doneProgress'])*100
        scanned = int(stats['scanCount'])
        matched = int(stats['eventCount'])
        results = int(stats['resultCount'])
        if verbose > 0:
            status = ("\r%03.1f%% | %d scanned | %d matched | %d results" % (
                progress, scanned, matched, results))
            sys.stdout.write(status)
            sys.stdout.flush()
        if stats['isDone'] == '1':
            if verbose > 0: sys.stdout.write('\n')
            break
        sleep(2)

    if 'count' not in kwargs_results: kwargs_results['count'] = 0
    results = job.results(**kwargs_results)

    strxml=""
    while True:
        content = results.read(1024)
        if len(content) == 0: break
        strxml+=content

        # sys.stdout.write(content.decode('utf-8'))
    # a=xmltodict.parse(strxml)
    # print a
    e = ET.XML(strxml)

    #print etree_to_dict(e)
    #print type(etree_to_dict(e))
    #tmp = json.loads(etree_to_dict(e))

    host=''
    host_name_1=''
    srcinterface=''
    catid=''
    cat_id=''
    link_flap=''
    devicetime=''
    portstatus=''
    tmps=etree_to_dict(e)
    for tmp in tmps['results']['result']:
        test_string=tmp
        field_data=test_string['field']
        offset=test_string['offset']
        # print field_data
        # print offset
        if offset =='0':
            for i in test_string['field']:
                a = i['k']
                b=i['value']['text']
                data_splunk=a+' '+b
                lst=data_splunk.split()
                if lst[0]=='host':
                    host=lst[1]
                if lst[0]=='hostname':
                    host_name_1=lst[1]
                if lst[0]=='src_interface':
                    srcinterface=lst[1]
                if lst[0]=='cat_id':
                    cat_id=lst[1].split('_')
                    catid=cat_id[0]
                if lst[0]=='flap':
                    link_flap=lst[1]
                if lst[0]=='device_time':
                    devicetime=lst[1]
                if lst[0]=='port_status':
                    portstatus=lst[1]

                insert_query = """INSERT INTO splunk
                                                (cat_id, path, port_status, src_interface, host, flap, hostname, device_time)
                                                VALUES
                                                """

                if len(catid) >= 9:
                    check_query = """
                                      SELECT splunk_id FROM splunk WHERE host='{0}' AND hostname='{1}' AND path='{2}' AND src_interface='{3}'
                                    """.format(host, host_name_1, catid, srcinterface)
                    getsplunk = db.query(check_query)
                    if len(getsplunk) > 0:
                        getsplunk = getsplunk[0]
                        sql_update_port_status = """
                                                      UPDATE `splunk` SET `port_status`='{0}',`flap`='{1}', cat_id='{3}' WHERE splunk_id='{2}'
                                                    """.format(str(portstatus), str(link_flap), getsplunk['splunk_id'], str(catid))
                        db.insert(sql_update_port_status)
                        print sql_update_port_status
                        print "UPDATE DONE"
                    else:
                        insert_query += "('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
                            str(catid), str(cat_id), str(portstatus), str(srcinterface),
                            str(host), str(link_flap), str(host_name_1), str(devicetime))
                        db.insert(insert_query)
                        print insert_query
                        print "INSERT DONE"
                else:
                    insert_query += "('', '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(
                        str(cat_id), str(portstatus), str(srcinterface),
                        str(host), str(link_flap), str(host_name_1), str(devicetime))
                    db.insert(insert_query)
                    print "INSERT DONE"

        sys.stdout.write('\n')

        #print str(tmp)+"  /n/n"

    #print test_string['field']
    # for i in temps_string['offset']:
    #     print i+"  /n/n"
    sys.stdout.flush()

    # sys.stdout.write('\n')
    job.cancel()

if __name__ == "__main__":
    main_search(sys.argv[1:])