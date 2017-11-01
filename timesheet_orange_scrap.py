import sys,time,os
from selenium import webdriver
#import smtplib
import Tkinter as tk # Python 2 import
import tkMessageBox
from functools import partial

###########################################################################
#                          Validate GUI inputs                            #
###########################################################################
list1 = []
def validate_input(mailid_val,username_val,password_val):
    global list1
    if not mailid_val.get():
        tkMessageBox.showerror("Error", "Please enter mail-id")
        root.destroy()
    else:
        list1.append(mailid_val.get())
    if not username_val.get():
        tkMessageBox.showerror("Error", "Please enter cu-id")
        root.destroy()
    else:
        list1.append(username_val.get())
    if not password_val.get():
        tkMessageBox.showerror("Error", "Please enter Password")
        root.destroy()
    else:
        list1.append(password_val.get())
    root.destroy()
    #root.withdraw()


###########################################################################
#                          Creating GUI                                   #
###########################################################################
root = tk.Tk()

mailid = tk.Label(root, text="Enter email-id").grid(row=0, column=0)
mailid_val = tk.Entry(root)
mailid_val.grid(row = 0, column = 1)
    
username = tk.Label(root, text="Enter cu-id").grid(row = 1, column = 0)
username_val = tk.Entry(root)
username_val.grid(row = 1, column = 1)
    
password = tk.Label(root, text="Enter password").grid(row = 2, column = 0)
password_val = tk.Entry(root, show="*")
password_val.grid(row = 2, column = 1)    

action_with_args=partial(validate_input,mailid_val,username_val,password_val)
Submit = tk.Button(root, text="Submit", command=action_with_args).grid(row=4, column=0)
Cancel = tk.Button(root, text="Cancel", command=root.destroy).grid(row=4, column=1)

root.mainloop()


#print list1
if len(list1) < 3:
    print "Exiting -- Not Found required parameters"
    sys.exit()

    
#root.deiconify()    
###########################################################################
#                          Selenium Variables                             #
###########################################################################
#url_to_find = "http://portal-kod.sso.infra.ftgroup/activite/index"


#url = 'http://portal-kod.sso.infra.ftgroup/login/login'
url = 'https://self.sso.infra.ftgroup/AuthForm/redirect.jsp?RETURN=http%3A//portal-kod.sso.infra.ftgroup/login/login'

Phantojs_Path = 'C:\\geckodriver-v0.11.1-win64\\phantomjs.exe'
#IE_Driver_Path = 'C:\\IEDriverServer_x64_3.0.0\\IEDriverServer.exe'
#curDir = os.getcwd()
#IE_Driver_Path = curDir + "\\IEDriverServer.exe"




###########################################################################
#                          Setting up the driver                          #
###########################################################################

#driver = webdriver.Ie(IE_Driver_Path)
driver = webdriver.PhantomJS(Phantojs_Path)
driver.delete_all_cookies()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get(url)
user = driver.find_element_by_xpath("//input[@id='user']")
user_name = user.get_attribute('value')
passwd = driver.find_element_by_xpath("//input[@id='password']")
pass_word = passwd.get_attribute('value')


if user_name == list1[1] and pass_word == list1[2]:
    driver.find_element_by_xpath("//span[text()='sign in']").click()
else:
    user.send_keys(list1[1])
    passwd.send_keys(list1[2])
    driver.find_element_by_xpath("//span[text()='sign in']").click()
    
time.sleep(20)

if not driver.title == "SI Labs :: Home":
    tkMessageBox.showerror("Error", "Error in login")
    sys.exit()

driver.find_element_by_xpath("//a[text()='timesheets']").click()
table =  driver.find_element_by_xpath("//div[@class='innerCalendrier']")



###########################################################################
#                          Get data of unfilled timesheet                 #
###########################################################################

def get_unfilled_weeks():
    '''this method will return the list of weeks for which timesheets are not filled
    exit the program if timesheet is all filled'''
    unfilled_list = []
    for row in table.find_elements_by_xpath('.//li/a'):
        if 'Status: no entry' in row.get_attribute('title'):
            unfilled_list.append(row.get_attribute('title'))
	
    if not unfilled_list:
        print "Timesheet is already filled for weeks mentioned in Si Labs"
        tkMessageBox.showinfo("INFO", "Timesheet is already filled for weeks mentioned in Si Labs")
        sys.exit()
    else:
        #print "Timesheet is pending for below weeks\n {}".format(unfilled_list)
        return [i.split(',')[0] for i in unfilled_list]
		
	
		

weeks = get_unfilled_weeks()
print "Timesheet is pending for below weeks:\n {}".format(weeks)
driver.quit()
tkMessageBox.showinfo("Timesheet is pending for::", weeks)



###########################################################################
#                       email variables                                   #
###########################################################################
From = 'test_user@orange.com'
To = list1[0]
Subject = 'Timesheet data'
Text = weeks
Server = 'meplus-smtp.si.francetelecom.fr'



###########################################################################
#                          Send email                                     #
###########################################################################

def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    """This method will send email report based on timesheet data"""
    message = """\
	Subject: %s

	%s
""" % (SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()	
	
#sendMail(From,To,Subject,Text,Server)
