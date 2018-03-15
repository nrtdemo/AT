import collections


class Ticket(object):
    data = collections.OrderedDict()

    def __init__(self, val):
        # self.data["interaction"] = ""
        # self.data["status"] = ""
        # self.data["incident"] = ""

        self.data["customertype"] = ""
        self.data["recipients"] = ""

        self.data["informant"] = "CATMA"
        self.data["email"] = "catma@ait.co.th"
        self.data["phonenumber"] = "021041761"
        self.data["sms"] = ""

        if val['catid'] is not None and val['catid'].value != '':
            self.data["catid"] = val['catid'].value
        else:
            raise ValueError("Only require to need CAT ID")

        if val['source'] is not None and val['source'].value != '':
            self.data["source"] = val['source'].value
        else:
            raise ValueError("Only require to need source")

        if val['destination'] is not None and val['destination'].value != '':
            self.data["destination"] = val['destination'].value
        else:
            raise ValueError("Only require to need destination")

        if val['address'] is not None and val['address'].value != '':
            self.data["address"] = val['address'].value
        else:
            raise ValueError("Only require to need address")

        if val['bandwidth'] is not None and val['bandwidth'].value != '':
            self.data["bandwidth"] = val['bandwidth'].value
        else:
            raise ValueError("Only require to need bandwidth")

        self.data["projectname"] = ""
        self.data["partnername"] = ""

        self.data["category"] = "Incident "
        self.data["subcategory"] = "failure"
        self.data["product_type"] = "system down"
        self.data["impact"] = "3"
        self.data["urgency"] = "2"

        self.data["affectedservice"] = "\xE0\xB8\x9A\xE0\xB8\xA3\xE0\xB8\xB4\xE0\xB8\x81\xE0\xB8\xB2\xE0\xB8\xA3\x20\x43\x41\x54\x20\x45\x50\x4C\x20\x2D\x20\x44\x6F\x6D\x65\x73\x74\x69\x63"
        self.data["affected_cl"] = ""
        self.data["assignment"] = "\xE0\xB8\xA1\xE0\xB8\x82\x2E\x20\x43\x6F\x72\x65\x20\x4E\x65\x74\x77\x6F\x72\x6B\x2F\xE0\xB8\xA1\xE0\xB8\xA1\x2E"

        if val['title'] is not None and val['title'].value != '':
            self.data["title"] = val['title'].value
        else:
            raise ValueError("Only require to need Title")
        if val['description'] is not None or val['description'].value != '':
            self.data["description"] = val['description'].value
        else:
            raise ValueError("Only require to need Description")
        if val['comment'] is not None and val['comment'].value != '':
            self.data["comment"] = val['comment'].value
        else:
            self.data["comment"] = ""


    def getData(self):
        return self.data

    def resetData(self):
        self.data = collections.OrderedDict()
