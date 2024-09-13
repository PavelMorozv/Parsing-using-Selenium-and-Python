import csv
import os
import random
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data)

    print(f"Data saved to {filename}")

url = 'https://www.nseindia.com/'

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

wd = webdriver.Chrome(options=options)
wd.maximize_window()
wd.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wd.delete_all_cookies()
wd.get(url)

time.sleep(random.uniform(0.5, 2))


elem = wd.find_element(by=By.XPATH, value="//header//a[@class='nav-link dd-link' and @id='link_2']")
WebDriverWait(wd, 10).until(lambda d: elem.is_displayed() and elem.is_enabled())
ActionChains(wd).move_to_element(elem).perform()

time.sleep(random.uniform(0.5, 2))

punkt = wd.find_element(by=By.XPATH, value="//header//a[@class='nav-link' and @href='/market-data/pre-open-market-cm-and-emerge-market']")
if WebDriverWait(wd, 10).until(lambda d: punkt.is_displayed() and punkt.is_enabled()):
    ActionChains(wd).move_to_element(punkt).click().perform()
else:
    print("Not found punct")
    os.close(1)


time.sleep(random.uniform(0.5, 2))

headers = wd.find_elements(by=By.XPATH, value="//table[@id='livePreTable']/thead/tr/th")
rows = wd.find_elements(by=By.XPATH, value="//table[@id='livePreTable']/tbody/tr")


time.sleep(random.uniform(0.5, 2))

if WebDriverWait(wd, 10).until(lambda d: len(headers) != 0) and \
   WebDriverWait(wd, 10).until(lambda d: len(rows) > 0):
    header_texts = [elem.text.replace("\n", " ") for elem in headers]
    data = [header_texts]

    for row in rows:
        cells = row.find_elements(by=By.XPATH, value=".//td")
        cell_texts = [cell.text.replace("\n", " ") for cell in cells]
        data.append(cell_texts)
        
    save_to_csv(data, 'test.csv')
else:
    print("Not found table head or body")
    os.close(1)

wd.get(url);

time.sleep(random.uniform(0.5, 5))







nefty_bank = wd.find_element(by=By.ID, value="tabList_NIFTYBANK")
if WebDriverWait(wd, 10).until(lambda d: nefty_bank.is_displayed() and nefty_bank.is_enabled()):
    ActionChains(wd).move_to_element(nefty_bank).click().perform()
else:
    print("Not found nefty_bank")
    os.close(1)

time.sleep(random.uniform(0.5, 2))

view_all = wd.find_element(By.XPATH, "//div[@class='tab-pane fade active show']//a[@href='/market-data/live-equity-market?symbol=NIFTY BANK']")
wd.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", view_all)
time.sleep(random.uniform(1, 2))
ActionChains(wd).move_to_element(view_all).click().perform()

time.sleep(random.uniform(0.5, 2))

select = wd.find_element(by=By.ID, value="equitieStockSelect")
ActionChains(wd).move_to_element(select).click().perform()

time.sleep(random.uniform(0.5, 2))

item = select.find_element(by=By.XPATH, value="//option[@value='NIFTY ALPHA 50']")
item.click()
wd.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", item)
time.sleep(random.uniform(1, 2))
ActionChains(wd).move_to_element(select).click().perform()
   
time.sleep(random.uniform(0.5, 5))
    
wd.quit()

os.startfile('test.csv')
os.close(0)

input('asdasdasd')