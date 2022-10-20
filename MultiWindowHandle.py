from selenium import webdriver
from selenium.webdriver.common.by import By

input = input('enter website')
input =input.lower()
driver = webdriver.Chrome()
driver.get('file:///C:/Users/Prem/AppData/Local/Temp/Rar$EXa20236.4594/MultipleWindowsOpening.html')
links = driver.find_elements(By.XPATH,'//a')
d = {}
for link in links:
    link.click()
    text = link.text
    url = driver.current_url
    d[text] = url
print(*d.items(),sep='\n')
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    title= driver.title
    title= title.lower()
    if input not in title:
        driver.close()










