from selenium.webdriver.common.by import By

class testSawg:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.ID,"user-name")
        self.password=(By.ID,"password")
        self.button=(By.ID,"login-button")
        self.sukses=(By.XPATH,"//span[@class='title']")
        self.gagal=(By.XPATH,"//h3[@data-test='error']")

    def masukanUsername(self,usernameNya):
        self.driver.find_element(*self.username).send_keys(usernameNya)
    def masukanPassword(self,passwordNya):
        self.driver.find_element(*self.password).send_keys(passwordNya)
    def tombol(self):
        self.driver.find_element(*self.button).click()
    def get_sukses(self):
        return self.driver.find_element(*self.sukses)
    def get_gaga(self):
        return self.driver.find_element(*self.gagal)