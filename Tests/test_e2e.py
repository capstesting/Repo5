import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Application started")
        homepage.shopItems().click()
        log.info("Shops Page started")

        checkout = CheckoutPage(self.driver)
        cards = checkout.cardTitles()
        log.info("Cards Selected")
        log.info(len(cards))
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                checkout.addProduct()[i].click()
        checkout.checkOut().click()

        confirmPage = ConfirmPage(self.driver)
        confirmPage.CartPage()
        confirmPage.CountrySelect().send_keys("ind")
        self.verifyLinkPresence("India", 7)
        self.driver.find_element_by_link_text("India").click()
        confirmPage.CheckBoxTerms()
        confirmPage.submitButton()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText
