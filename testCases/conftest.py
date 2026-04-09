import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

# To run test parallel :-  pytest -v -s -n=2 testCases\test_login.py --browser chrome

# different browsers
@pytest.fixture()
def setup(browser):
    if browser == "chrome":             # pytest -v -s testCases\test_login.py --browser chrome
        driver = webdriver.Chrome()
        print("Launching chrome browser .............")
    elif browser == "microsoft":        # pytest -v -s testCases\test_login.py --browser edge
        driver = webdriver.Edge()    
        print("Launching MicrosoftEdge browser .............")
    else:
         driver = webdriver.Ie()   
    return driver


def pytest_addoption(parser):  # This will get the value from CLI hooks
    parser.addoption("--browser") 

@pytest.fixture()
def browser(request):           # This will return the broser value to the setup method.
    return request.config.getoption("--browser")    


################### Pytest HTML Report #############################

# pytest -v -s -n=2 --html=Reports\report.html testCases\test_login.py --browser chrome

# This hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nop Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Gupta Jii"    

# This hook for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)