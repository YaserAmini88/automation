from selenium import webdriver

class Music():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def play(self):
        name = input("Enter a channel name: ")
        self.driver.get("https://www.youtube.com/c/" + name + "/videos")
        new = self.driver.find_element_by_xpath('//*[@id="dismissible"]', "https://www.youtube.com/embed")
        new.click()

bot = Music()
bot.play()
