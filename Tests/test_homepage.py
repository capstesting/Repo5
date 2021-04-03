import pytest
from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHome(BaseClass):

    def test_CreateUser(self):
        home= HomePage(self.driver)
        home.Name().send_keys("TEST")
        home.Email().send_keys("abc@fgwek.com")
        home.Password().send_keys("Test")
        home.Check().click()
        home.Gender().click()
        home.Submit()

        message = self.driver.find_element_by_class_name("alert-success").text
        
        assert("Success!" in message)

