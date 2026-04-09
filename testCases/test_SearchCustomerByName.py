import time
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:

    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):

        self.logger.info("************* TC_SearchCustomerByName_005 **********")

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
        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()

        self.addcust.clickOnCustomersMenuItem()

        time.sleep(3)


        # SEARCH CUSTOMER
        self.logger.info("************* Searching customer by Name **********")

        searchcust = SearchCustomer(self.driver)

        searchcust.setFirstName("Victoria")

        searchcust.setLastName("Terces")

        searchcust.clickSearch()

        time.sleep(5)


        status = searchcust.searchCustomerByName("Victoria Terces")


        if status == True:

            assert True

            self.logger.info("*********** Search Customer By Name Test Passed ***********")

        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchByName.png")

            self.logger.error("*********** Search Customer By Name Test Failed ***********")

            assert False


        self.driver.close()


        self.logger.info("*************** TC_SearchCustomerByName_005 Finished ***********")