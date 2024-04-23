# Test case ID:TC_PIM_01

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class PIM01: # for get url and for login
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self): # boot the windows and get url
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, second):
        sleep(second)

    def inputBox(self, value, keys): #find the element by name
        self.driver.find_element(by=By.NAME, value=value).send_keys(keys)
        self.sleep(5)



    def submitBtn(self): #click the login button
        self.driver.find_element(by=By.TAG_NAME, value='button').click()
        self.sleep(10)

    def quit(self):
        self.driver.quit()

    def findElementByXpath(self, xpath): #find the element by xpath
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def login(self, data1, data2, data3): # main process
        try:
            self.boot()
            self.inputBox('username', self.username)
            self.inputBox('password', self.password)
            self.submitBtn()
            self.sleep(3)

            #login in webpage
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            self.sleep(5)

            #go to PIM left pane to the webpage
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
            self.sleep(5)

            #add the new employee details in add employee
            self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').click()
            firstNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
            firstNameElement.send_keys(data1)

            #second name element for fill the middle name
            self.sleep(5)
            self.action.send_keys(Keys.TAB).perform()
            secondNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')
            secondNameElement.send_keys(data2)
            self.sleep(3)
            self.action.send_keys(Keys.TAB).perform()

            #third name element for fill the last name
            thirdNameElement = self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
            thirdNameElement.send_keys(data3)
            self.sleep(3)
            #TAB keys is used for skip to other employee box

            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(Keys.TAB).perform()

            self.findElementByXpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
            self.sleep(10)

            print('The new employee is successful added')
        except NoSuchElementException:
            print('no new employee is added')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
obj = PIM01(url, 'Admin', 'admin123')
obj.login('Ajith', 'Kumar', 'E')



