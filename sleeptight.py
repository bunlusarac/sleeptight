###################################################################
# sleeptight - worst fear of YTU guys who wear socks with sandals #
# by brsthegck                                                    #
###################################################################

import time
import os
import psutil
from urllib.request import urlopen
from selenium import webdriver

print(
r"""
      ,,                     ,           ,,      ,  
      ||                    ||   '   _   ||     ||  
 _-_, ||  _-_   _-_  -_-_  =||= \\  / \\ ||/\\ =||= 
||_.  || || \\ || \\ || \\  ||  || || || || ||  ||  
 ~ || || ||/   ||/   || ||  ||  || || || || ||  ||  
,-_-  \\ \\,/  \\,/  ||-'   \\, \\ \\_-| \\ |/  \\, 
                     |/             /  \   _/       
                     '             '----`           
don't let the bed bugs bite - brsthegck v1.0.0-alpha
----------------------------------------------
""")

SITE_URL = 'https://online.yildiz.edu.tr/'
CONFIG_PATH = './stconfig'
ZOOM_EXECUTABLES = ['zoom.exe', 
                    'zoom_launcher.exe', 
                    'zUpdater.exe', 
                    'zCrashReport.exe',
                    'CptControl.exe',
                    'CptHost.exe', 
                    'CptInstall.exe', 
                    'CptService.exe',
                    'zTscoder.exe',
                    'ZoomOutlookIMPlugin.exe',
                    'ZoomDocConverter.exe']

#Check connectivity
try:
    urlopen(SITE_URL)
    print("Internet connection found/site is accessible. Proceeding...")
except urllib2.URLError as err:
    print("Internet connection not found or site is currently not accessible.")
    quit()

#Read/write config
if(os.path.exists(CONFIG_PATH)):
    print("Config file found. Using login creds from the config file...")
    
    config_file = open(CONFIG_PATH, "r")
    std_mail = config_file.readline()
    std_pass = config_file.readline()
    config_file.close()
else:
    print("Config file does not exist. Prompting login creds for new config file.")
    std_mail = input("Enter the student mail address:")
    std_pass = input("Enter the student password:")
    
    config_file = open(CONFIG_PATH, "w")
    config_file.writelines(std_mail + '\n')
    config_file.writelines(std_pass)
    config_file.close()
    
#Get user input
course_id = input("Enter the course ID:")    
n_hours = int(input("How long is the course (hours):"))
    
driver = webdriver.Chrome('./chromedriver')
driver.get(SITE_URL)

#Login process
print("Logging in...")
mail_field = driver.find_element_by_id("Data_Mail")
pwd_field = driver.find_element_by_id("Data_Password")
login_btn = driver.find_element_by_class_name("btn-primary")

mail_field.send_keys(std_mail)
pwd_field.send_keys(std_pass)
login_btn.click()

time.sleep(5)

#Waiting loop
for i in range(1, (n_hours+1)):
    print("Slaughtering all Zoom processes...")
    for proc in psutil.process_iter():
        if proc.name() in ZOOM_EXECUTABLES:
            proc.kill()
    
    print(f"-----Starting and waiting for next hour... [{i}/{n_hours}]-----")
    driver.get(f"https://online.yildiz.edu.tr/?transaction=LMS.EDU.LessonProgram.ViewOnlineLessonProgramForStudent/{course_id}")
    time.sleep(3)
    join_btn = driver.find_element_by_class_name("btn-secondary")
    join_btn.click()
    time.sleep(5)
    
    #Wait 50 minutes
    time.sleep(60 * 50)
    
 
driver.close()
