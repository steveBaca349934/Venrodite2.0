from selenium import webdriver
import traceback
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from builtins import input
import time
import urllib.request
from selenium.webdriver.common.keys import Keys

from CNN import *


class OpenTinder(object):

    def __init__(self):
        print("initialized")

    @staticmethod
    def tinderOpen(string):
        x = set()

        # opening up chrome using selenium
        driver = webdriver.Chrome()
        driver.get(string)

        # implicitly wait 5 seconds
        driver.implicitly_wait(20)

        # hitting the login button
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





        # implicitly wait 5 seconds
        driver.implicitly_wait(10)

        # hitting the facebook login button
        try:
            element = driver.find_element_by_xpath(
                "//span[contains(@class,'Pos(r) Z(1) D(ib)') and contains(text(), 'Log in with Facebook')]")
            driver.execute_script("arguments[0].click();", element)

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
        #initialize and load Conv Net
        CNN.loadImagesTrainModel()

        counter = 0
        while True:
            if counter ==0:

                counter += 1


            element = driver.find_element_by_xpath("//div[@class = 'Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox']")
            string = element.get_attribute("style")
            imageUrl = string.split("\"")
            urllib.request.urlretrieve(imageUrl[1],"/Users/stevebaca/Desktop/saved folder images tinderbot/image.jpg")

            # going every other person so you dont get shat on by the algorithm
            driver.find_element_by_id("Tinder").send_keys(Keys.ARROW_LEFT)



            #TODO I need to have this loop check for popups that tinder sometimes comes up with


            print(imageUrl[1])

            number = CNN.applyModel("/Users/stevebaca/Desktop/saved folder images tinderbot/image.jpg")
            print("The number is " + " " + str(number))
            if number == 0:
                driver.find_element_by_id("Tinder").send_keys(Keys.ARROW_LEFT)
            else:
                driver.find_element_by_id("Tinder").send_keys(Keys.ARROW_RIGHT)

            try:
                driver.find_element_by_xpath(
                    "//span[contains(@class,'Pos(r) Z(1)') and contains(text(), 'Not interested')]").click()
            except Exception:
                print("did not show up luckily lol")
                continue





        while True:
            pass
