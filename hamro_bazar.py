import sqlite3Add commentMore actions
from selenium.common import exceptions
# create connection
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE Details(Selling_item Text,Ad_id TEXT, Ad_views INTEGER,Ad_post_date TEXT,Ad_expiry_date TEXT,seller_name TEXT, seller_memvbership_date TEXT,seller_phone INTEGER,seller_location TEXT,seller_mobile TEXT,description _details TEXT,property_price TEXT,property_location TEXT)''')
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
unique_path='/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr/td[1]'
offset=0
while(offset<=40):
       driver.get('https://hamrobazaar.com/c112-real-estate?catid=112&order=popularad&offset='+str(offset) +'')
       for i in range (4,30):
            for table in driver.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i) +']/tbody'):
                items= table.find_elements(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table['+ str(i) +']/tbody/tr[1]/td[3]/a[1]')
                for item in items:
                    item.click()
                    driver.switch_to.window(driver.window_handles[-1])
                    selling_item=(driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/span/b/font')).text
                    ad_id=(driver.find_element(By.XPATH,''+ unique_path +'/table[1]/tbody/tr[2]/td[2]')).text
                    ad_views=(driver.find_element(By.XPATH,''+ unique_path +'/table[1]/tbody/tr[3]/td[2]')).text
                    ad_post_date=(driver.find_element(By.XPATH,''+ unique_path +'/table[1]/tbody/tr[4]/td[2]')).text
                    ad_expiry_date=(driver.find_element(By.XPATH,''+ unique_path +'/table[1]/tbody/tr[5]/td[2]/b')).text
                    seller_name=(driver.find_element(By.XPATH,''+ unique_path +'/table[2]/tbody/tr[2]/td[2]')).text
                    seller_membership_date=(driver.find_element(By.XPATH,''+ unique_path +'/table[2]/tbody/tr[3]/td[2]')).text
                    seller_phone=(driver.find_element(By.XPATH,''+ unique_path +'/table[2]/tbody/tr[5]/td[2]')).text
                    seller_address=(driver.find_element(By.XPATH,''+ unique_path +'/table[2]/tbody/tr[6]/td[2]')).text
                    seller_mobile=(driver.find_element(By.XPATH,''+ unique_path +'/table[2]/tbody/tr[7]/td[2]')).text
                    description=(driver.find_element(By.XPATH,''+ unique_path +'/table[3]/tbody/tr/td/table/tbody/tr[2]/td')).text
                    price=(driver.find_element(By.XPATH,''+ unique_path +'/table[4]/tbody/tr[2]/td[2]')).text
                    property_location=(driver.find_element(By.XPATH,''+ unique_path +'/table[5]/tbody/tr[2]/td[2]')).text
                    
                    c.execute('''INSERT INTO Details VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''',(selling_item,ad_id,ad_views,ad_post_date,ad_expiry_date,seller_name,seller_membership_date,seller_phone,seller_address,seller_mobile,description,price,property_location))
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
    
        
       offset=offset+20
    

       
conn.commit()