######################################################################
# This script goes to keepa url and trigger a jquery for mouseover   #
# an web element to show a table and then parse that table and feed  #
# the data in csv tabular format                                     #
######################################################################

import csv,time
from selenium import webdriver

Phantojs_Path = 'C:\\geckodriver-v0.11.1-win64\\phantomjs.exe'

driver = webdriver.PhantomJS(Phantojs_Path)
#driver = webdriver.Firefox()


url = "https://keepa.com/#!product/1-1118324579"
driver.maximize_window()
driver.get(url)
time.sleep(10)
driver.execute_script("$('#statistics').trigger('mouseover')")
time.sleep(2)


def get_table_data(list_objects):
    '''This method take web objects list as input and returns the text
       of those elements as a list'''
    new_list = []
    for i in list_objects:
        new_list.append(i.text)
    return new_list

def write_data(final_head_list,final_data_list):
    '''This method takes two lists as input one for table heading
       and another for table data and write this to table in csv.'''
    with open('name1.csv', 'w') as csvfile:
        csvw = csv.writer(csvfile)
        csvw.writerow([i for i in final_head_list])
        for i in final_data_list:
            csvw.writerow(i)

list1= []

els_head = driver.find_elements_by_xpath("//table[(@id='statsTable')]//tr/th")

for i in range(1,6):
    els_data = driver.find_elements_by_xpath("//table[(@id='statsTable')]//tr/td["+str(i)+"]")
    list2 = get_table_data(els_data)
    list1.append(list2)

final_head_list = get_table_data(els_head)
final_data_list = zip(*list1)

write_data(final_head_list,final_data_list)

driver.quit()


