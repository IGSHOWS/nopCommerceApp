import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:

    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):

        self.logger.info("************* TC_SearchCustomerByEmail_004 **********")

        self.driver = setup

        self.driver.get(self.baseURL)

        self.driver.maximize_window()


        # LOGIN
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        self.logger.info("************* Login successful **********")


        # OPEN CUSTOMER PAGE
        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()

        self.addcust.clickOnCustomersMenuItem()

        time.sleep(3)


        # SEARCH CUSTOMER
        self.logger.info("************* searching customer by email **********")

        searchcust = SearchCustomer(self.driver)

        searchcust.setEmail("victoria_victoria@nopCommerce.com")

        searchcust.clickSearch()

        time.sleep(5)


        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")


        if status == True:

            assert True

            self.logger.info("*********** Search Customer By Email Test Passed ***********")

        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchByEmail.png")

            self.logger.error("*********** Search Customer By Email Test Failed ***********")

            assert False


        self.driver.close()

        self.logger.info("*************** TC_SearchCustomerByEmail_004 Finished ***********")