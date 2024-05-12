from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
# 데이터 다운로드, 팝업창 제어를 함수로 만들 경우 알 수 없는 오류 발생...
# 2020년 ~ 2023년 데이터 다운로드 -> 기간의 마지막 일자를 선택하는 방식
def select_ym(driver):
    driver.find_element(By.ID, 'monthEnd').click() # 종료일 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[1]/table/tbody/tr/td[2]').click() # 년도 클릭
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[2]/td[3]/a').click() # 다음 년도 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[4]/td[3]/a').click() # 12월 선택
    driver.find_element(By.XPATH, '//*[@id="searchWrap"]/div[1]/input').click() # 조회 버튼 클릭
    time.sleep(0.5)

# 다운로드 -> 팝업창 제어가 필요
def download(driver):
    driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/a').click()
    driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/ul/li[3]/p[2]/a').click()
    time.sleep(1)

    tmp = driver.find_element(By.ID, 'modal_data_util_exmn')
    tmp.find_element(By.ID, 'rdoDataUtilExmn5').click()
    tmp.find_element(By.ID, 'submit').click()
'''

# 웹 페이지 생성
url = 'https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(0.5)

driver.find_element(By.CLASS_NAME, 'member').click()
time.sleep(0.5)

# 로그인
driver.find_element(By.ID, 'mbrId').click()
driver.find_element(By.ID, 'mbrId').send_keys('ID')
driver.find_element(By.ID, 'mbrPw').click()
driver.find_element(By.ID, 'mbrPw').send_keys('PW')
driver.find_element(By.CLASS_NAME, 'table-btn').click()
time.sleep(0.5)

# 원하는 데이터 페이지로 이동
driver.get('https://datalab.visitkorea.or.kr/datalab/portal/loc/getLocalDataForm.do')
time.sleep(1)

# 처음에 2019년으로 들어가는 부분
driver.find_element(By.ID, 'monthStart').click()
driver.find_element(By.CLASS_NAME, 'month-picker-title').click()
driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="searchWrap"]/div[1]/input').click()
time.sleep(1)

#download(driver=driver) # 2019 데이터 다운로드

# 2019년 데이터 다운로드
driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/a').click() # ... 클릭
driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/ul/li[3]/p[2]/a').click() # 데이터 다운로드 클릭
time.sleep(1)

# 팝업창 제어
tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창을 찾는다.
tmp.find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
tmp.find_element(By.ID, 'submit').click() # 제출 클릭
time.sleep(3)

# 2020 ~ 2023 데이터 다운로드
for _ in range(4):
    driver.find_element(By.ID, 'monthEnd').click() # 종료일 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[1]/table/tbody/tr/td[2]').click() # 년도 클릭
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[2]/td[3]/a').click() # 다음 년도 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[4]/td[3]/a').click() # 12월 선택
    driver.find_element(By.XPATH, '//*[@id="searchWrap"]/div[1]/input').click() # 조회 버튼 클릭
    time.sleep(0.5)
    
    # 데이터 다운로드
    driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/a').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1106"]/div[1]/div[2]/ul/li[3]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(1)

    # 팝업창 제어
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창을 찾는다.
    tmp.find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
    tmp.find_element(By.ID, 'submit').click() # 제출 클릭
    time.sleep(3)