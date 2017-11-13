########################################
# In progress Not completed            #
########################################

from selenium import webdriver
import re,json,sys
import time


list1= []
url = "https://www.amazon.in/"



def get_num(value):
    ''' This method is used to remove extra special character from number
        e.g  input : 25GB  and  output : 25   '''
    pattern = re.compile(r'(^\d*)')
    reg = pattern.search(value)
    return reg.group(1)
    

def driver_setup():
    '''This method is used to setup driver'''
    driver = webdriver.Firefox()
    return driver


def fetch_discounts(driver,url):
    ''' This method is used to get all the discounted items list'''
    driver.get(url)
    discount_list= driver.find_elements_by_xpath("//span[@class='red-sticker']")
    if len(discount_list) == 0:
        print "No items for this much discount"
        sys.exit()
    return discount_list


def dump_data_in_json(list1):
    '''This method is used to put data in to a json file'''
    f=open('data.json','w')
    json.dump(list1,f,indent=4)

def parse_discounts(driver,discount_list,num):
    '''This method is used to get list of items with details (product name & ASIN)whose discounts is more than provided arguments'''
    window_before = driver.window_handles[0]
    for item in discount_list:
        item_text = item.text
        item_value = get_num(item_text)
        if item_value > num:
            print item_value
            item.click()
            time.sleep(4)
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            while True:
                page_state = driver.execute_script('return document.readyState;')
                if page_state == 'complete':
                    break
            product= driver.find_element_by_xpath("//span[@id='productTitle']")
            product_name= product.text
            print product_name
            #number= driver.find_element_by_xpath("//li[contains(.,'ASIN: ')]")
            #ASIN = number.text.split(':')[1].strip()
            data = { "name" : product_name}
            list1.append(data)
            driver.close()
            driver.switch_to_window(window_before)
    return list1




def main(argv):
    '''Main method to define flow of program'''
    
    driver = driver_setup()
    list2 = fetch_discounts(driver,url)
    list3 = parse_discounts(driver,list2,argv)
    dump_data_in_json(list3)
    driver.quit()
    print list3



if __name__ == "__main__":
    if len(sys.argv) >= 3 or len(sys.argv) < 2:
        print "Wrong number of arguments\nUsage only provide single arguments"
        sys.exit()
    main(sys.argv[1])
