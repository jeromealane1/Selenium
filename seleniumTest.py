from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import smtplib
import time

# The web driver must be added to the UNIX PATH in order for this to work
# I added the web driver to the PATH variable from the directory selenium/test1 in this manner: 
# export PATH=$PATH:/home/jerome/Documents/Code/python/selenium/test1
#os.environ['PATH'] = "/home/jerome/Documents/Code/python/selenium/test1"
#
#os.system('export PATH=$PATH:/home/jerome/Documents/Code/python/selenium/test1')
#os.system('ls')
browser = webdriver.Firefox('/home/jerome/Documents/Code/python/selenium/test1')
#browser.get('http://seleniumhq.org/')
#browser.get('https://www.google.com/imghp?hl=en&tab=wi0&ogbl')
browser.get('https://www.packworld.com/newsletter-registration')

#browser.find_element_by_name("q").send_keys("cars") #google search 
#browser.find_element_by_name("q").send_keys(Keys.ENTER) #google search click
browser.find_element_by_name('submitted[email]').send_keys("fab@yiffst.com")
browser.find_element_by_id('edit-submitted-first-name').send_keys("bob")
browser.find_element_by_id('edit-submitted-last-name').send_keys("vila")
browser.find_element_by_id('edit-submitted-job-title').send_keys("content manager")
browser.find_element_by_id('edit-submitted-company-name').send_keys("Pelcore")
browser.find_element_by_id('edit-submitted-phone').send_keys("333-333-3333")

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 587)#set up emailing
smtpObj.connect()
smtpObj.ehlo()

smtpObj.login('ln.jrm.1988@gmail.com','')
smtpObj.sendmail('ln.jrm.1988@gmail.com','Subject: test')#send the mail with a subject
smtpObj.quit()
print(type(smtpObj))
print("test")

