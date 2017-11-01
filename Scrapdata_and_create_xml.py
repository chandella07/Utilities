from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xml.etree.cElementTree as ET
import time

url = "http://www.westervoortplaza.nl/page/"

driver = webdriver.Firefox()

title=[]
imge=[]

for i in range(1,179):
    driver.get(url+str(i))
    d= driver.find_elements_by_xpath("//div[@id='vw-page-content']//h3/a")
    c= driver.find_elements_by_xpath("//div[@id='vw-page-content']//a/img")
    if len(d)== len(c):
        for td in d:
            title.append(td.text)
        
        for j in c:
            imge.append(j.get_attribute('src'))
    else:
        print i


#print title
#print imge

root = ET.Element("dates")


for k in range(len(title)):
    doc = ET.SubElement(root, "date")

    ET.SubElement(doc, "Title").text = "<![CDATA["+title[k]+"]]>"
    ET.SubElement(doc, "image").text = "<![CDATA["+imge[k]+"]]>"

tree = ET.ElementTree(root)
tree.write("Data.xml")
