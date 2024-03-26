#!/usr/bin/env python
import time

from selenium import webdriver  # selenium setup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

PROCESSOR = '\033[95m'         # Light pink
BLUE = '\033[94m'              # Blue
GREEN = '\033[92m'             # Green
YELLOW = '\033[93m'            # Yellow
FAIL = '\033[91m'              # Red
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

while (True):  # the script
    c = input(PROCESSOR + tool + ENDC)  # command-line-like interface
    if (c == "start"):                # start script
        x = int(input(BOLD + "Number of friends to add:\t" + ENDC))  # number of friends to add
        added = x                                                    # number of soon-will-be-added accounts. save up for modifying

        while cycle:  # cycle while the script cannot login

            nme = input(YELLOW + "Your facebook username/email: " + ENDC)  # facebook email / username
            pssword = input(YELLOW + "Your facebook password: " + ENDC)    # facebook password

            driver.get("https://www.facebook.com")  # open to facebook.com

            email = driver.find_element(By.NAME, "email")  # search email textbox
            email.send_keys(nme)                           # enter email / username = nme

            # email.send_keys(Keys.TAB)  # probably useless, since the next step covers the intent already.

            password = driver.find_element(By.NAME, "pass")  # search password textbox

            password.send_keys(pssword)      # enter password
            password.send_keys(Keys.RETURN)  # --press login button.

            breakpoint()    # ain't no idea but we gotta wait for a while till the process is set.

            try:                                                                               # try finding home-button and click, test for login success.
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Home"]').click()  # find Home-button and click it
                cycle = False;                                                                 # if succeded, not cycle
                break;                                                                         # break out of the cycle
            except NoSuchElementException:                                                     # if password and/or username are incorrect
                print(FAIL + "Your username and/or password appear to be incorrect. Try again !" + ENDC)    # report error
                cycle = True

        time.sleep(5)  # wait for process loading ( redundant ?)
        print(PROCESSOR + "Successfully Logged in. continuing !" + ENDC)

        for friend_index in range(1, x + 1):                                            # friend-adding cycle
            if friend_index == 1 :
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Friends"]').click()         # click the Friends button
                time.sleep(3)                                                                  # wait to load
            try:     # try to click Add Friend-button
                driver.find_element(By.CSS_SELECTOR, '[aria-label="Add friend"]').click()    # -- testing --> success. Still in checking.
                # driver.get("https://www.facebook.com")                                     # reloads : facebook will not think that the script is a bot + time delay (new friends may appear) --prbly won't be of use.

                print(UNDERLINE + "Friend number " + GREEN + str(friend_index) + ENDC + UNDERLINE + " has been added." + ENDC)  # reports
                time.sleep(2)       # wait for loading process

            except NoSuchElementException:                                # if button not found
                time.sleep(3)                                             # wait (in hope that new Add Friend-buttons will appear)
                print(FAIL + "Error, friend couldn't been added" + ENDC)  # report
                added = added - 1                                         # loses one friend
                # driver.get('https://www.facebook.com')                    # reload to check if new friends appeared (a bit redundant. prbly won't be of use).

        print(YELLOW + "You have succesfully added " + str(added) + " friends in total!. \n" + ENDC)    # reports how many friends were succesfully added
        print(PROCESSOR + "Terminating . . . ")
        driver.close()                                         # clothes firefox window
        quit()

    # COMMAND-LINE for interaction
    elif (c == "exit"):             # if user wants to exit
        print(FAIL + "Exiting...")  # report
        driver.close()              # close firefox window
        quit()                      # exit this script

    elif (c == "version"):          # if user want to know the version number
        print('Version 1.1 \n')     # version

    elif (c == "info"):             # if user want info
        print(
            """This script is a simple facebook friend-request sender, it is still in development. If you wish to help or give an advice or an idea, you are welcome at """ + BLUE + UNDERLINE + """https://gist.github.com/RRobotek/6619b5ca6948f1f49ae3\n""" + ENDC + """Cheers, RRobotek \n""")

    elif (c == "clear"):  # clear
        print('\n' * 64)  # 64 new lines

    elif (c == "help"):   # help
        help()            # function above is used

    else:                 # if command not recognized
        print(FAIL + "Command not recognized. Please try again !" + ENDC)
