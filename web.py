import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

#table-striped
#filename = input("ชื่อไฟล์ : ")
#Insert file name
#start_page = int(input("ใส่เลขหน้าเริ่มต้น: "))

#Insert result name
#end_page = int(input("ใส่เลขหน้าสุดท้าย: "))
keyword = "พัทยา"

file_name = "input.xlsx"
dfx = pd.read_excel(file_name)


url_lis = [i for i in dfx['Link']]
for d in url_lis: 
    print(d)



print(url_lis)
#Get bot selenium make sure you can access google chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

soup = BeautifulSoup(driver.page_source,'html.parser')


tun_lis = []
value_lis = []
size_lis = []
tsic_lis = []
cat_lis = []
pur_lis = []
bussiness_lis = []
title_lis = []
niti_lis = []
nitinum_lis = []
reg_lis = []
stat_lis = []
catbus_lis = []
year_lis = []
valueplus_lis = []
phone_lis = []

for i in url_lis:
    
    driver.get(i)

    niti = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/thead/tr/td')
    niti_lis.append(niti.text)
    print(niti.text)

    nitinum = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[1]/td')
    nitinum_lis.append(nitinum.text)
    print(nitinum.text)

    reg = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[2]/td')
    reg_lis.append(reg.text)
    print(reg.text)

    stat = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[3]/td/span')
    stat_lis.append(stat.text)
    print(stat.text)


    catbus = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[4]/td')
    catbus_lis.append(catbus.text)
    print(catbus.text)

    year = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[5]/td/a')
    year_lis.append(year.text)
    print(year.text)
    

    try:
        valueplus = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[6]/td/a')
        valueplus_lis.append(valueplus.text)
        print(valueplus.text)
    except StaleElementReferenceException: 
        valueplus_lis.append("ไม่มี")
        print(valueplus.text) 

    
    try:
        phone = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[1]/div/div/table/tbody/tr[7]/td')
        phone_lis.append(phone.text)
        print(phone_lis)
    except NoSuchElementException: 
        phone_lis.append("ไม่มี")
        print("ไม่มี")
   

    title = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/h3')
    title_lis.append(title.text)
    print(title.text) 

    tun = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td') 
    tun_lis.append(tun.text)
    print(tun.text)

    value = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td')
    value_lis.append(value.text)
    print(value.text)

    size = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[3]/td')
    size_lis.append(size.text)
    print(size.text)


    cat = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td')
    cat_lis.append(cat.text)
    print(cat.text)

    tsic = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[5]/td')
    tsic_lis.append(tsic.text)
    print(tsic.text)



    pur = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[6]/td')
    pur_lis.append(pur.text)
    print(pur.text)


    bussiness = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[4]/div/div[2]/div[2]/div/div/table/tbody/tr[7]/td')
    bussiness_lis.append(bussiness.text)
    print(bussiness.text)


df = pd.DataFrame()
df['ชื่อบริษัท'] = title_lis 

df['ชื่อนิติบุคคล'] = niti_lis 
df['เลขทะเบียนนิติบุคคล'] = nitinum_lis
df['วันเดือนปีที่จดทะเบียน'] =reg_lis 
df['สถานภาพกิจการ'] = stat_lis 
df['ประเภทธุรกิจ'] = catbus_lis
df['ปีที่ส่งงบการเงิน'] = year_lis
df['จดทะเบียนภาษีมูลค่าเพิ่ม'] = valueplus_lis
df['โทรศัพท์'] = phone_lis



df['ทุนจดทะเบียนปัจจุบัน (บาท)'] = tun_lis 
df['มูลค่าบริษัท'] = value_lis 
df['ขนาดธุรกิจ '] = size_lis 
df['หมวดธุรกิจ (A-U)'] = cat_lis 
df['TSIC'] = tsic_lis 
df['วัตถุประสงค์'] = pur_lis 
df['บริษัทในกลุ่มธุรกิจเดียวกัน'] = bussiness_lis 


df.to_excel("Testx.xlsx")