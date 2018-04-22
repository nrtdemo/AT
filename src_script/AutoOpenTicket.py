#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import os
import time
import collections
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class OpenTicketCatTTS(object):
    uName = "catma"
    pWord = "ait@1761"
    url = "http://122.155.137.214/sm/ess.do?lang=en&mode=ess.do&essuser=true"
    chromedriver = ""
    firefoxdriver = ""

    def __init__(self, username="catma", password="ait@1761", url=""):
        os.chdir(os.path.dirname(__file__))
        pathdriver = os.getcwd()
        self.chromedriver = pathdriver + "/chromedriver"
        self.uName = username
        self.pWord = password
        self.url = url

    def CAT_TTS(self, driver, data):
        print "Login..."
        user = driver.find_element_by_name("user.id")
        user.send_keys(self.uName)
        pwd = driver.find_element_by_id("LoginPassword")
        pwd.send_keys(self.pWord)

        driver.find_element_by_id("loginBtn").click()

        driver.find_element_by_id("ext-gen158").click()
        time.sleep(1)

        print "Open New Ticket..."
        # chang to another iframe
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_id("X12").send_keys(data['catid'])
        driver.find_element_by_id("X13Btn").click()
        driver.find_element_by_class_name('shadowFocus').click()

        print "New Incident..."
        # Informant
        elem_Informant = driver.find_element_by_name("instance/oss.informant")
        elem_Informant.clear()
        elem_Informant.send_keys("CATMA")
        # E-mail
        elem_Email = driver.find_element_by_name("instance/contact.email")
        elem_Email.clear()
        elem_Email.send_keys("catma@ait.co.th")
        # Phone
        elem_Phone = driver.find_element_by_name("instance/oss.contact.telephone")
        elem_Phone.clear()
        elem_Phone.send_keys("021041761")

        # Urgency
        # elem_btn_Urgency = driver.find_element(By.XPATH, "//input[@dvdvar='instance/severity']")
        elem_btn_Urgency = driver.find_element_by_name("instance/severity")
        elem_btn_Urgency.clear()
        elem_btn_Urgency.send_keys("2 - High")

        # Assignment Group
        elem_btn_Assignment_group = driver.find_element_by_name("instance/assignment")
        elem_btn_Assignment_group.clear()
        elem_btn_Assignment_group.send_keys("มข. THAIPAK".decode('utf-8'))

        # Description
        elem_Description = driver.find_element_by_name("instance/action/action")
        elem_Description.clear()
        elem_Description.send_keys(data['description'])

        # Title and clear title
        elem_btn_Title = driver.find_element_by_name("instance/brief.description")
        elem_btn_Title.clear()
        elem_btn_Title.send_keys("Down")
        elem_Description.click()
        time.sleep(1)
        driver.find_element_by_id("X25Btn").click()

        time.sleep(15)
        driver.save_screenshot('tmp.png')

        # exit form open ticket
        driver.find_element_by_id("X3Btn").click()

        # save & exit open new ticket
        # driver.find_element_by_id("X4Btn").click()

    def auto_openticket(self, data):
        try:
            print "Now to go..."
            print self.url

            # Display
            display = Display(visible=0, size=(1920, 1080))
            display.start()

            # Chrome browser
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-setuid-sandbox")
            driver = webdriver.Chrome(self.chromedriver, chrome_options=chrome_options)

            # Firefox browser
            # firefox_binary = FirefoxBinary('/usr/bin/firefox')
            # driver = webdriver.Firefox(firefox_binary=firefox_binary)

            driver.implicitly_wait(30)
            driver.get(self.url)
            print driver.title.encode('utf8', 'replace')
            driver.save_screenshot('start.png')

            time.sleep(1)
            # print data
            print data['catid'] + "\n" + data['description']
            self.CAT_TTS(driver, data)

            driver.save_screenshot('end.png')
            print "Finished on!!!!"
            display.stop()
            driver.quit()
        except Exception as e:
            raise e


if __name__ == "__main__":
    data = collections.OrderedDict()
    data['catid'] = "TBB147512"
    data['description'] = "ทดสอบ LINK DOWN\nTEST SYSTEM".decode('utf-8')

    tmp = OpenTicketCatTTS(url='http://122.155.137.214/sm/ess.do?lang=en&mode=ess.do&essuser=true')
    tmp.auto_openticket(data)
