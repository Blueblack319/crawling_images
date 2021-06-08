from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# import urllib.request
import requests

# 강아지상: 워너원 강다니엘, 박보검, 엑소 백현, 임시완, 아스트로 차은우, 박보영
# 고양이상: 한예슬, 유인영, 이나영, 하윤하, 오연서, 경리
# 공룡상: 김우빈, 공유, 류준열, 홍종현, 탑(최승현), 동해
# 토끼상: 방탄소년단 전정국, 워너원 박지훈, 트와이스 나연, 아이유

# 프로세스를 차지하지 않게 비워줘야 함.
# ps -aux

# kill -9 $(pidof chromedriver)
# kill -9 $(pidof google-chrome)


SCROLL_PAUSE_TIME = 1
PAGE_LOADING_TIME = 2

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--single-process")

name = '차은우'
animal_type = 'rabbit'


driver = webdriver.Chrome('./chromedriver',
                          options=options)
driver.get('https://google.com')
search_bar = driver.find_element_by_name('q')
search_bar.send_keys(name)
search_bar.send_keys(Keys.RETURN)

time.sleep(PAGE_LOADING_TIME)

driver.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()
# /html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/a
# /html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a

time.sleep(PAGE_LOADING_TIME)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    cur_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == cur_height:
        break
    last_height = cur_height

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
i = 0
for image in images:
    i = i + 1
    time.sleep(1)
    driver.execute_script("arguments[0].click();", image)
    time.sleep(2)
    image_url = image.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute('src')
    try:
        res = requests.get(image_url)
    except:
        i = i - 1
        continue
    with open(f"{name}/{name}_{i}.jpg", 'wb') as outfile:
        outfile.write(res.content)
    if i == 50:
        break
    print(i)

driver.close()

driver.quit()

#/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img