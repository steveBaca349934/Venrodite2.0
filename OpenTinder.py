from selenium import webdriver
import traceback

class OpenTinder(object):

    def __init__(self):
        print("initialized")

    @staticmethod
    def tinderOpen(string):
        x = set()



        #opening up chrome using selenium
        driver = webdriver.Chrome()
        driver.get(string)

        #implicitly wait 20 seconds
        driver.implicitly_wait(20)

        #hitting the login button
        try:
            driver.find_element_by_xpath(
                "//span[contains(@class,'Pos(r) Z(1)') and contains(text(), 'Log in')]").click()
        except Exception:
            traceback.print_exc()



        # ask user for their facebook username and password

        print("please enter your facebook username")
        userName = str(input())
        print("please enter your facebook password")
        passWord = str(input())

        print("your facebook username is " + " " + userName + " " + "and your password is " + passWord)

        # hitting the facebook login button
        try:
            driver.find_element_by_xpath(
                "//span[contains(@class,'Pos(r) Z(1)') and contains(text(), 'Log in with Facebook')]").click()
        except Exception:
            traceback.print_exc()

        # seeing what the parent is
        parent = driver.current_window_handle

        x = driver.window_handles

        for i in x:
            if i != parent:
                driver.switch_to.window(i)
                print(i)

        try:
            driver.find_element_by_id("email").send_keys(userName)
            driver.find_element_by_id("pass").send_keys(passWord)
            driver.find_element_by_id("loginbutton").click()
        except Exception:
            traceback.print_exc()

        driver.switch_to.window(parent)

        try:
            driver.find_element_by_xpath(
                "//span[contains(@class,'Pos(r) Z(1)') and contains(text(), 'Allow')]").click()
        except Exception:
            traceback.print_exc()

        try:
            driver.find_element_by_xpath(
                "//span[contains(@class,'Pos(r) Z(1)') and contains(text(), 'Not interested')]").click()
        except Exception:
            traceback.print_exc()

        # implicitly wait 20 seconds
        driver.implicitly_wait(20)








        while(True):
            pass













