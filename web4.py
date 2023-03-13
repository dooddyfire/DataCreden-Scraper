

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


td_all = []
for i in url_lis:
    
    driver.get(i)

    soupx = BeautifulSoup(driver.page_source,'html.parser')
    lis = soupx.find_all('table',{'class':'table-striped'})

    print(lis[0])
    print(lis[1])

    tr_all_left = [ i.find('th').text for i in lis[0].find_all('tr')]
    td_all_left =  [ i.find('td').text.strip() for i in lis[0].find_all('tr')]

    tr_all_right = [ i.find('th').text for i in lis[1].find_all('tr')]
    td_all_right=   [ i.find('td').text.strip() for i in lis[0].find_all('tr')]

    print(tr_all_left,len(tr_all_left))
    print(tr_all_right,len(tr_all_right))
    print(td_all_left,len(td_all_left))
    print(td_all_right,len(td_all_right))

    td_all.append([td_all_left+td_all_right])

tr_all_big = tr_all_left + tr_all_right

df = pd.DataFrame()

print(tr_all_big)
df.columns = [r'ชื่อนิติบุคคล',r'เลขทะเบียนนิติบุคคล',r'วันเดือนปีที่จดทะเบียน',r'สถานภาพกิจการ',r'ประเภทธุรกิจ',r'ปีที่ส่งงบการเงิน',r'จดทะเบียนภาษีมูลค่าเพิ่ม',r'โทรศัพท์',r'ทุนจดทะเบียนปัจจุบัน (บาท)',r'มูลค่าบริษัท',r'ขนาดธุรกิจ',r'หมวดธุรกิจ (A-U)',r'กลุ่มธุรกิจ (TSIC)',r'วัตถุประสงค์',r'บริษัทในกลุ่มธุรกิจเดียวกัน']

for i in tr_all_big: 
    print(len(i))



df.to_excel("Testx.xlsx")