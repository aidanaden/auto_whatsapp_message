from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
from datetime import datetime
import sched, time
import sys


def check_if_roll_call():


    # obtain & format current date & time 
    # to (date, month, hour)
    now = datetime.now()
    day_str = now.strftime("%d %B")


    # only grab the hours value and
    # manually add "00" to the back xd
    time_str = now.strftime("%H00")

    
    # check if it's 0800 or 1400
    # (time for roll call)
    if (time_str == "0800" or time_str == "1400"):


        # if true, return current date & hour
        return (True, day_str, time_str)

    else:


        # return false if not roll call time
        return (False, None, None)        






def create_roll_call_message(day_str, time_str, current_location):
    

    # starting message of roll call
    msg_1 = f"*Roll Call on {day_str} @ {time_str}hrs*"
    msg_2 = "1. Name: CPL RYAN"
    msg_3 = "2. Temperature: 36.3"
    msg_4 = "3. Medical Status: not sick"
    msg_5 = f"4. Location: {current_location}"

    big_msg = [msg_1, msg_2, msg_3, msg_4, msg_5]
    #big_msg_cat = '\n'.join(big_msg)
    #big_msg_cat = big_msg_cat.replace('\n', Keys.SHIFT+Keys.RETURN)

    return big_msg






def send_roll_call_msg(driver, roll_call_msg):


    # set the name of your target (group/user)
    test_target = "'baby slut '"
    target = '"2nd SCDF *PROVOST*"'


    # find the convo/chat with target via css selector
    driver.find_element_by_css_selector(f"span[title={target}]").click()


    # find the message box & enter the message in 
    # TEST: driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(roll_call_msg)
    for msg in roll_call_msg:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT + Keys.RETURN)
    

    # click on the send button
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()


    # close driver
    # driver.close()






def roll_call(s,driver):


    # check if it's roll call 
    is_rollcall, day_str, time_str = check_if_roll_call() 
        
     
    if is_rollcall == True:

        # if it's roll call time, 
        # create current location & 
        # roll call message and send it
        current_location = "home"
        roll_call_msg = create_roll_call_message(day_str, time_str, current_location)
        send_roll_call_msg(driver, roll_call_msg)


    else:

        # if not true, create new schedule 
        print('Not time for roll call, checking again in 1 hour...')
    

    # start next schedule check
    s.enter(3600, 1, roll_call, (s,driver))






def setup():
    
    
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
    s.enter(0, 1, roll_call, (s,driver))
    
    
    # start scheduler
    s.run()





setup()