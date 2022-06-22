# -------------------------------------------------------------------------------
# Imports
import csv
import requests
from selenium import webdriver
import time
# -------------------------------------------------------------------------------
# Setup

def start(data,exe_path):
    with open(data, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # -------------------------------------------------------------------------------
        # Web Automation

        driver = webdriver.Chrome(executable_path=exe_path)
        #add this line
        driver.implicitly_wait(10)

        driver.get('https://www.google.si/')
        
        ids = "TITLE FIRSTNAME LASTNAME PHONE EMAIL DEPOSIT".split()
        for line in csv_reader:
            time.sleep(0.2)
            for i,id in enumerate(ids):
                driver.find_element_by_xpath(f'//*[@id="{id}"]').send_keys(line[i])

            #submit
            driver.find_element_by_xpath('//*[@id="sib-form"]/div[9]/div/button').click()
            # wait for notifcation --> driver.implicitly_wait(10) sets up the driver so it will wait for 10 seconds
            try:
                if "Bidder added successfully" == driver.find_element_by_class_name('sib-form-message-panel__inner-text').text:
                    # close the notifcation or just continue
                    pass
                else:
                    #bidder wasn't added succesfully
                    pass
            except:
                print("driver didn't find the element with 10 seconds wait period")
        driver.quit()