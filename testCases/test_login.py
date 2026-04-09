import pytest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("***********Test_001_Login*************")
        self.logger.info("***********Verifying HomePage Title*************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("***********HomePage Title is passed*************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***********HomePage Title is failed*************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***********Verifying Login Test*************")
        self.driver = setup 
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)           
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***********Login Test is passed*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("***********Login Test is failed*************")
            # print("Actual title is:", act_title)
            assert False