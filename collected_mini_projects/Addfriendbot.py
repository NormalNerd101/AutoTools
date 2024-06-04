#!/usr/bin/env python
import os
import time

from selenium import webdriver  # selenium setup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.system("")
PROCESSOR = '\033[95m'  # Light pink
BLUE = '\033[94m'  # Blue
GREEN = '\033[92m'  # Green
YELLOW = '\033[93m'  # Yellow
FAIL = '\033[91m'  # Red
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

driver = webdriver.Firefox()


def help():  # help function: instruction.
    print(BLUE + "start : Start the script." + ENDC)
    print(BLUE + "version : Version." + ENDC)
    print(BLUE + "exit : Exit." + ENDC)
    print(BLUE + "info : Info." + ENDC)
    print(BLUE + "clear : Clear console." + ENDC)
    print(BLUE + "help : This help message." + ENDC)


tool = "Add_friends@py: "
cycle = True  # login cycle
times = 0
# the script
while True:
    print("--Commands : start - version - exit - info - clear - help.")
    c = input(PROCESSOR + tool + ENDC)
    if c == "start":
        x = int(input(BOLD + "Number of friends to add: " + ENDC))
        added = x
        # log-in cycle.
        while cycle:
            # open facebook.com
            driver.get("https://www.facebook.com")
            # Enter account and password
            nme = input(YELLOW + "Your facebook username/email: " + ENDC)
            pssword = input(YELLOW + "Your facebook password: " + ENDC)
            email = driver.find_element(By.NAME, "email")
            email.send_keys(nme)
            password = driver.find_element(By.NAME, "pass")
            password.send_keys(pssword)
            password.send_keys(Keys.RETURN)
            times += 1
            time.sleep(8)
            # Test for log-in success.
            # breakpoint()
            if times == 5:
                print(FAIL + "OVERLOADING ERR : TERMINATING . . . " + ENDC)
                exit(1)
            try:
                # WebDriverWait(driver, 12).until(
                #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Block')]"))
                # ).click()
                driver.refresh()
                time.sleep(4)
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Home"]').click()
                cycle = False
                break
            except:
                print(
                    FAIL + "Your username and/or password appear to be incorrect. Or Errors occured while logging-in. "
                           "Try again !" + ENDC)
                cycle = True

        print(PROCESSOR + "Successfully Logged in. continuing !" + ENDC)

        # friend-adding process.
        for friend_index in range(1, x + 1):
            if friend_index == 1:
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Friends"]').click()
                time.sleep(3)
            # try to click Add Friend-button
            try:
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Add friend"]').click()
                # driver.get("https://www.facebook.com")    # reloads : facebook will not think that the script is a
                # bot + time delay (new friends may appear)
                print(UNDERLINE + "Friend number " + GREEN + str(
                    friend_index) + ENDC + UNDERLINE + " has been added." + ENDC)
                time.sleep(2)
            except NoSuchElementException:
                time.sleep(3)  # wait (in hope that new Add Friend-buttons will appear)
                print(FAIL + "Error, friend couldn't been added" + ENDC)
                added = added - 1
                # driver.get("https://www.facebook.com")    # reloads
        # report final result.
        print(YELLOW + "You have succesfully added " + str(added) + " friends in total!. \n" + ENDC)
        print(PROCESSOR + "Terminating . . . " + ENDC)
        driver.close()
        quit()

    # COMMAND-LINEs
    elif c == "exit":
        print(FAIL + "Exiting...")
        driver.close()
        quit()
    elif c == "version":
        print('Version 1.5 \n')
    elif c == "info":
        print(BLUE + "A Facebook friend-request sender script for your entertainment. Have fun ! " + ENDC)
    elif c == "clear":
        print('\n' * 64)
    elif c == "help":
        help()
    else:
        print(FAIL + "Command not recognized. Please try again !" + ENDC)
