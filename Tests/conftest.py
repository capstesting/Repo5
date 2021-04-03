from selenium import webdriver
import pytest

#for getting thebrowser name from command prompt
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
     
    driver=webdriver.Chrome(executable_path="E:\Python\Selenium\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    
