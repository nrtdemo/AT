import urllib, httplib2
from xml.dom import minidom
import xmltodict, re, time, json

class SPLUNK_PATH(object):
    auth = '/services/auth/login'
    job_create = '/services/search/jobs'
    job_status = '/services/search/jobs/{0}'
    job_result = '/services/search/jobs/{0}/results'


class SPLUNK(object):
    baseurl = ''
    username = ''
    password = ''
    sessionKey = None

    def __init__(self, username, password, baseurl='https://10.4.0.136:8089'):
        self.baseurl = baseurl
        self.username = username
        self.password = password

    def GetData(self, url, method='GET', headers=None, body=None):
        if self.sessionKey and headers == None:
            headers = {'Authorization': 'Splunk %s' % self.sessionKey}
        else:
            headers = {}
        if body:
            resp = httplib2.Http(disable_ssl_certificate_validation=True).request(url, method, headers=headers, body=urllib.urlencode(body))
        else:
            resp = httplib2.Http(disable_ssl_certificate_validation=True).request(url, method, headers=headers)
        return resp

    def Auth(self):
        if not self.sessionKey:
            resp = self.GetData(self.baseurl + SPLUNK_PATH.auth, 'POST', {}, {'username': self.username, 'password': self.password})
            self.sessionKey = minidom.parseString(resp[1]).getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue

    def CreateSearch(self, search_query, timerange='-24h'):
        self.Auth()
        search_query = search_query.strip()
        if not (search_query.startswith('search') or search_query.startswith('|')):
            search_query = 'search ' + search_query
        resp = self.GetData(self.baseurl + SPLUNK_PATH.job_create, 'POST', None, {'search': search_query, 'earliest': timerange, 'latest': 'now'})
        d = xmltodict.parse(resp[1])
        sid = d['response']['sid']
        return sid

    def GetSearchStatus(self, search_id):
        self.Auth()
        resp = self.GetData(self.baseurl + SPLUNK_PATH.job_status.format(search_id), 'GET')
        matchobj = re.search('<s:key name="dispatchState">([^\\<]*)</s:key>', resp[1])
        if matchobj:
            return matchobj.group(1)
        return

    def GetSearchResult(self, search_id):
        self.Auth()
        resp = self.GetData(self.baseurl + SPLUNK_PATH.job_result.format(search_id), 'GET', None, {'output_mode': 'json'})
        d = json.loads(resp[1])
        lst = d['results']
        return lst
