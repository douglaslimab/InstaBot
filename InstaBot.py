from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

path = "C:\Program Files (x86)\chromedriver.exe"
service = Service(path)
options = webdriver.ChromeOptions()


class Instabot:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.driver = webdriver.Chrome(executable_path=path, service=service, options=options)

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')

        Element_cookie = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        time.sleep(1)
        Element_username = driver.find_element_by_name('username').send_keys(self.user_name)
        Element_password = driver.find_element_by_name('password').send_keys(self.password)
        Element_submit = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        time.sleep(5)
#        Element_notification = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    def open_explore(self):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/')
        time.sleep(3)

    def open_tag(self, tag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + tag + '/')
        time.sleep(2)

    def open_first_post(self):
        driver = self.driver

        # when using for tags
        Element_First = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()

        # when using for explore
#        Element_First = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/div/div[1]/div[2]').click()
        time.sleep(1)

    def like_post(self):
        driver = self.driver
        Element_Like = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
        time.sleep(1)

    def next_post(self):
        driver = self.driver
        try:
            Element_Next = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button/div').click()
            self.scroll_down()
        except:
            Element_Next = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button/div').click()
        time.sleep(1)

    def close_post(self):
        driver = self.driver
        Element_Close = driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
        time.sleep(1)

    def scroll_down(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def follow(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
        time.sleep(1)
