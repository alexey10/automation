# coding=utf-8
from datetime import datetime
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import HTMLTestRunner

# -*- coding: utf-8 -*-

class TrustArc(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.example.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.FirstName = "One"
        self.LastName = "Two"
        self.Company = "Three"
        self.Email = "name@domainame.com"
        self.Phone = "4151231234"
        self.Title = "automation"

     

    def fill_form(self):
        driver = self.driver
        driver.get(self.base_url + "about/contact")
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys(self.FirstName)
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys(self.LastName)
        driver.find_element_by_id("Company").clear()
        driver.find_element_by_id("Company").send_keys(self.Company)
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys(self.Email)
        driver.find_element_by_id("Phone").clear()
        driver.find_element_by_id("Phone").send_keys(self.Phone)
        Select(driver.find_element_by_id("Function__c")).select_by_visible_text("IT / Security")
        driver.find_element_by_id("Title").clear()
        driver.find_element_by_id("Title").send_keys(self.Title)
        Select(driver.find_element_by_id("Country")).select_by_visible_text("US")
        Select(driver.find_element_by_id("State")).select_by_visible_text("CA")
        driver.find_element_by_link_text("Get Started").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main(verbosity=2)
    # if __name__ == "__main__":
    unittest.main()





       