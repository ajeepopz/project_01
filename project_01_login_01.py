# test case ID:TC_LOGIN_02

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class LoginAutomation: #for login
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self): #boot the windows and get url
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, second):
        sleep(second)

    def inputBox(self, value, keys): #find the element by name and send the key
        self.driver.find_element(by=By.NAME, value=value).send_keys(keys)
        self.sleep(5)

    def submitBtn(self): #find the login button and click
        self.driver.find_element(by=By.TAG_NAME, value='button').click()
        self.sleep(10)


    def quit(self):
        self.driver.quit()

    def login(self):  #main process
        try:
           self.boot()
           self.inputBox('username', self.username)
           self.inputBox('password', self.password)
           self.submitBtn()

           print('the user is logged in successfully')
        except NoSuchElementException:
            print('A valid error message for invalid credentials is displayed')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
obj = LoginAutomation(url, 'Admin', 'admin123')
obj.login()