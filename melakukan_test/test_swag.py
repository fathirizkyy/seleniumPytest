import pytest
from .conftest import setup
from .pageLogin import testSawg

@pytest.mark.usefixtures("setup")
class TestSwag:
    def test_sukses(self,setup):
        driver=testSawg(setup)
        setup.get("https://www.saucedemo.com/")
        driver.masukanUsername("standard_user")
        driver.masukanPassword("secret_sauce")
        driver.tombol()
        assert driver.get_sukses().text in "Products"

    def test_usernamesalah(self,setup):
        driver=testSawg(setup)
        setup.get("https://www.saucedemo.com/")
        driver.masukanUsername("standard")
        driver.masukanPassword("secret_sauce")
        driver.tombol()
        assert driver.get_gaga().text in "Epic sadface: Username and password do not match any user in this service"

    def test_passwordsalah(self,setup):
        driver = testSawg(setup)
        setup.get("https://www.saucedemo.com/")
        driver.masukanUsername("standard_user")
        driver.masukanPassword("secret")
        driver.tombol()
        assert driver.get_gaga().text in "Epic sadface: Username and password do not match any user in this service"