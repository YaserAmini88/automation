from selenium import webdriver
from confidential import username, password

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def parscoders(self):
        self.driver.get("https://parscoders.com/")
        login = self.driver.find_element_by_link_text("ورود")
        login.click()

        user = self.driver.find_element_by_id("username")
        user.click()
        user.send_keys("yaser.amini67@gmail.com")

        pwd = self.driver.find_element_by_id("password")
        pwd.click()
        pwd.send_keys("Devilwontcry1367")

        btn = self.driver.find_element_by_xpath("/html/body/div[4]/form/div[4]/button")
        btn.click()

bot = Bot()
bot.parscoders()