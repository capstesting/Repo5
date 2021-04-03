from selenium import webdriver
import pytest
from time import sleep

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="E:\Python\Selenium\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/broken_images")
sleep(10)

x=driver.find_elements_by_tag_name("img")

for i in x:
    size=i.size
    print(size)
