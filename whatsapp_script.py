from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
from datetime import datetime
import sched, time
import sys
import argparse


def check_if_roll_call():


    # obtain current day, date & time 
    # & format to (date, month, hour)
    now = datetime.now()
    date_str = now.strftime("%d %B")
    day_str = now.strftime("%a")


    # only grab the hours value and
    # minute values xd
    time_str = now.strftime("%H00")

    
    # check if it's 0800 or 1400 (time for roll call)
    # and it's a weekday and not a weekend.
    if (time_str == "0800" or time_str == "1400") and (day_str not in ["Sat", "Sun"]):


        # if true, return current date & hour
        return (True, date_str, time_str)

    else:


        # return false if not roll call time
        return (False, None, None)        






def create_roll_call_message(date_str, time_str, roll_call_info):
    

    # unwrap roll call info
    status, temp, location = roll_call_info


    # sets date and month in format eg 7 July @ 1400hrs
    msg_1 = f"*Roll Call on {date_str} @ {time_str}hrs*"

    # set rank and name
    msg_2 = "1. Name: CPL RYAN"

    # set temperature
    msg_3 = f"2. Temperature: {temp}"

    # set medical status
    msg_4 = f"3. Medical Status: {status}"

    # set location
    msg_5 = f"4. Location: {location}"

    big_msg = [msg_1, msg_2, msg_3, msg_4, msg_5]

    return big_msg






def send_roll_call_msg(driver, roll_call_msg):


    # set the name of your target (group/user)
    test_target = "'baby slut '"
    target = '"2nd SCDF *PROVOST*"'


    # find the convo/chat with target via css selector
    driver.find_element_by_css_selector(f"span[title={target}]").click()


    # find the message box & enter the message in 
    for msg in roll_call_msg:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT + Keys.RETURN)
    

    # click on the send button
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()


    # close driver
    # driver.close()






def roll_call(s,driver,roll_call_info):


    # check if it's roll call 
    is_rollcall, date_str, time_str = check_if_roll_call() 
        
     
    if is_rollcall == True:

        # if it's roll call time, 
        # create roll call message and send it
        roll_call_msg = create_roll_call_message(date_str, time_str, roll_call_info)
        send_roll_call_msg(driver, roll_call_msg)
        print('Time for roll call, sent roll call message!!')


        # start next schedule check in 1 hr (3600 seconds)
        s.enter(3600, 1, roll_call, (s,driver,roll_call_info))


    else:

        # if not true, create new schedule 
        print('Not time for roll call, checking again in 10 mins...')
    

        # start next schedule check in 10 mins (600 seconds)
        s.enter(600, 1, roll_call, (s,driver,roll_call_info))
    






def setup(args):
    
    # get status, temp and location from user
    roll_call_info = (args.status, args.temperature, args.location)
    
    # access chromedriver (use FULL PATH)
    # and make sure it's updated to be compatible
    # with the version of chrome u using 
    driver = webdriver.Chrome('C:\\Users\\Aidan\\Downloads\\chromedriver_win32\\chromedriver.exe')
    
    
    # tells chromedriver to wait for at least 'x'
    # amount of seconds before throwing an error
    driver.implicitly_wait(15)
    
    
    # start new whatsapp instance (get ur phone rdy)
    driver.get("https://web.whatsapp.com/")
    
    
    # setup scheduler
    s = sched.scheduler(time.time, time.sleep)
    
    
    # start first schedule
    s.enter(0, 1, roll_call, (s,driver,roll_call_info))
    
    
    # start scheduler
    s.run()



parser = argparse.ArgumentParser()
parser.add_argument('temperature',help='Enter your temperature for the day in degrees C.')
parser.add_argument('status', help='Enter your medical status (sick or not sick) for the day.')
parser.add_argument('location', help='Enter your location for the day (div or home) and reason.')

args = parser.parse_args()

setup(args)