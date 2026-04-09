import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtTest_xpath = "//input[@id='customer_attribute_1']"
    txtcustomerRoles_xpath = "//ul[@class='select2-selection__rendered']"
    lstitemAdministrators_xpath = "//li[@title='Administrators']"
    lstitemRegistered_xpath = "//li[@title='Registered']"
    lstitemGuests_xpath = "//li[@title='Guests']"
    lstitemVendors_xpath = "//li[@title='Vendors']"
    drpmgrOfVendor_xpath = "//span[@id='select2-VendorId-container']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)   

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()  

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)    

    def setTest(self, test):
        self.driver.find_element(By.XPATH, self.txtTest_xpath).send_keys(test)             

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)

        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)

        elif role=='Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()