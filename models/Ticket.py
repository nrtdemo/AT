import collections

class Ticket(object):

    data = collections.OrderedDict()

    def __init__(self, val):
        # self.data["interaction"] = ""
        self.data["status"] = ""
        # self.data["incident"] = ""

        self.data["customertype"] = ""
        self.data["recipients"] = "catma"

        self.data["informant"] = ""
        self.data["email"] = "catma@ait.co.th"
        self.data["phonenumber"] = "021041761"
        self.data["sms"] = ""

        if val['catid'] is not None and val['catid'].value != '':
            self.data["catid"] = val['catid']
        else:
            raise ValueError("Only require to need CAT ID")

        self.data["source"] = ""
        self.data["destination"] = ""
        self.data["address"] = ""
        if val['bandwidth'] is not None and val['bandwidth'].value != '':
            self.data["bandwidth"] = ""
        else:
            raise ValueError("Only require to need band")

        self.data["projectname"] = ""
        self.data["partnername"] = ""

        self.data["category"] = ""
        self.data["subcategory"] = ""
        self.data["product_type"] = ""

        self.data["impact"] = ""
        self.data["urgency"] = ""

        self.data["affectedservice"] = ""
        self.data["affected_cl"] = ""
        self.data["faulttime"] = ""
        self.data["uptime"] = ""

        # self.data["totaltime"] = ""

        self.data["assignment"] = ""
        self.data["EndToEnd_group"] = ""
        self.data["sla_target_date"] = ""
        self.data["repair_team"] = ""

        if val['title'] is not None and val['title'].value != '':
            self.data["title"] = val['title']
        else:
            raise ValueError("Only require to need Title")
        if val['description'] is not None or val['description'].value != '':
            self.data["description"] = ""
        else:
            raise ValueError("Only require to need Description")
        self.data["comment"] = ""

    # def redirect_page(self, form):
    #

    def getData(self):
        return self.data

    def resetData(self):
        self.data = collections.OrderedDict()


