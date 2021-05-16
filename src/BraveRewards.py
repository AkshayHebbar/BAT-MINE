#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Start a browser instance with custom properties
import os

#Change Directory to Brave Executable
os.chdir("C:\Program Files\BraveSoftware\Brave-Browser\Application")

#Start Brave Browser using custom configuration in a specific location
os.popen('brave.exe --remote-debugging-port=2021 --user-data-dir="D:\Selenium\AutomationProfile"')


# In[2]:


from selenium import webdriver
import time
from datetime import datetime

#Driver and application path
driver_path = "D:/Technical/Softwares/Technical/ChromeDriver/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

#Add Optional Arguements
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_experimental_option("debuggerAddress", "127.0.0.1:2021")         # Connect using the same custom port to access the specific browser
# option.add_argument("--headless") #OPTIONAL
# option.add_argument("--incognito") #OPTIONAL


# In[3]:


#Open a brave browser

browser = webdriver.Chrome(executable_path=driver_path, options=option, keep_alive=True)
# browser = webdriver.Chrome(driver_path, options=option)
# browser = webdriver.Chrome(executable_path=brave_path, options=option, keep_alive=True)


# In[4]:


#Open New Tab
browser.get("chrome://newtab")


# In[5]:


#CLick Start Brave Rewards Button if available
# XPATH: //*[@id="root"]/div/div/section[3]/div[3]/div/div[1]/div/div[1]/div[2]/button/div

try:
    element = browser.find_element_by_xpath('//*[@id="root"]/div/div/section[3]/div[3]/div/div[1]/div/div[1]/div[2]/button/div')
    browser.execute_script('''document.getElementsByClassName("StyledButton-sc-dpixd1 PrimaryButton-sc-1q1i1vt htUlEF erSHic TurnOnAdsButton-sc-ffhgdb hldotA")[0].click()''')
except:
    print('Start Rewards Button not available')


# ###### Method to Click Rewards or Refresh Page
# 
# Based on the availability of the Reward Element, click or refresh the page

# In[6]:


#Method to click reward
def clickRewards():
    
    try:
#         Check for the XPATH of the rewards element
        element = browser.find_element_by_xpath("//*[@id='root']/div/div/footer/div/section[1]/div/div/a")
#         browser.execute_script('''document.getElementsByClassName("Anchor-sc-g85p1z gqphhp")[0].click()''')
        time.sleep(3)
        element.click()        # Click the element
        print("Element Found", datetime.now())
        time.sleep(6)
        browser.execute_script('''window.history.go(-1);''')        # Go Back
        browser.execute_script("window.open('chrome://newtab');")        # Open a new Tab to stop caching
        time.sleep(3)
        window_name = browser.window_handles[1]        # Get name of new window
        browser.close()        # Close previous tab
        time.sleep(3)
        browser.switch_to.window(window_name=window_name)        # Switch to new Tab
        browser.execute_script('''window.location.reload();''')        # Reload the new Tab
#         browser.execute_script('''window.history.go(-1);''')
    except:
        browser.execute_script('''window.location.reload();''')
        time.sleep(3)
    

# browser.execute_script('''window.open('chrome://newtab');''')
# browser.execute_script('''window.open('', 'newwindow','location=1,status=1,scrollbars=1, resizable=1, directories=1, toolbar=1, titlebar=1');''')
# browser.execute_script('''window.open('');''')
# browser.switch_to.window(driver.window_handles[1])


# In[7]:


# element = browser.find_element_by_xpath('//*[@id="root"]/div/div/section[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/span[1]')


# In[ ]:


# Run the process in an infinite loop to keep clicking on ads
while True:
    print("Process Start:", datetime.now())        # Log process start time
    element = browser.find_element_by_xpath('//*[@id="root"]/div/div/section[3]/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/span[1]')
    print("Total accumulated BAT :", element.text)
    for x in range(6):        # For every 4-6 refresh the rewards page will appear
        clickRewards()
    time.sleep(480)        # Run the method every 8 minutes


# In[ ]:


browser.quit()


# In[16]:





# ###### Desired Capabilities
# 
# It gives the desired properties of the running browser instance

# In[4]:


# handles = browser.desired_capabilities
# print(handles)


# In[ ]:


# # Connect to existing session
# executor_url = browser.command_executor._url
# session_id = browser.session_id

# print(session_id)
# print(executor_url)

# browser = webdriver.Remote(command_executor=executor_url,desired_capabilities={})
# browser.close()   # this prevents the dummy browser
# browser.session_id = session_id

