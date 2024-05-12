from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
# 함수로 할 경우 알 수 없는 오류 발생
# 다운로드 -> 팝업창 제어가 필요 
def download(driver):
    # 방문자수 추이
    driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/a').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn')
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click()
    tmp.find_element(By.ID, 'submit').click()
    time.sleep(10)

    # 방문자 거주지 분포
    place_container = driver.find_element(By.ID, '1202')
    place_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1202"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn')
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click()
    tmp.find_element(By.ID, 'submit').click()
    time.sleep(10)

    # 방문자 성/연령 분포
    sex_container = driver.find_element(By.ID, '1267')
    sex_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1267"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn')
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click()
    tmp.find_element(By.ID, 'submit').click()
    time.sleep(10)
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
driver.find_element(By.ID, 'mbrId').send_keys('id 입력')
driver.find_element(By.ID, 'mbrPw').click()
driver.find_element(By.ID, 'mbrPw').send_keys('pw 입력')
driver.find_element(By.CLASS_NAME, 'table-btn').click()
time.sleep(0.5)


# 원하는 데이터 페이지로 이동
driver.get('https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaDataForm.do#')
time.sleep(0.5)

# 방문자 선택
driver.find_element(By.ID, 'tab2on').click()
time.sleep(5)

for i in range(1, 18): # 서울 ~ 제주: 실제로는 18으로 바꿔줘야됨
    driver.find_element(By.ID, 'area-select').click() # 도시 선택 버튼 클릭
    driver.find_element(By.XPATH, f'//*[@id="srchNatCdList1"]/a[{i}]').click() # 지역 선택
    driver.find_element(By.XPATH, '//*[@id="popup1"]/div[3]/div/a[2]').click() # 확인 버튼 클릭
    time.sleep(3)

    # 처음에 2019년 다운로드 -> 검색 단위가 18개월이라 애매 -> 끝나는 date을 설정해준다.
    driver.find_element(By.ID, 'monthStart').click()
    driver.find_element(By.CLASS_NAME, 'month-picker-title').click() # 년도 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[1]/a').click() # 2019 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[1]/a').click() # 1월 선택
    driver.find_element(By.XPATH, '//*[@id="searchWrap"]/div[1]/input').click()
    time.sleep(1)

    driver.find_element(By.ID, 'monthEnd').click() # 종료일 선택
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[1]/table/tbody/tr/td[1]/a').click() # 2020년에서 2019년으로 이동
    driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[4]/td[3]/a').click() # 12월 선택
    driver.find_element(By.XPATH, '//*[@id="lookup-wrap"]/input').click() # 조회 버튼 클릭
    time.sleep(3)

    # 방문자수 추이
    driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/a').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    # 팝업창 제어
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
    tmp.find_element(By.ID, 'submit').click() # 제출 클릭
    time.sleep(3)

    # 방문자 거주지 분포
    place_container = driver.find_element(By.ID, '1202')
    place_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1202"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    # 팝업창 제어
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
    tmp.find_element(By.ID, 'submit').click() # 제출 클릭
    time.sleep(3)

    # 방문자 성/연령 분포
    sex_container = driver.find_element(By.ID, '1267')
    sex_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
    driver.find_element(By.XPATH, '//*[@id="1267"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
    time.sleep(0.5)
    # 팝업창 제어
    tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
    tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
    tmp.find_element(By.ID, 'submit').click() # 제출 클릭
    time.sleep(3)
 
    for _ in range(4):
        # 시작 date 설정
        driver.find_element(By.ID, 'monthStart').click()
        driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[1]/table/tbody/tr/td[3]/a').click() # 다음 년도로 이동
        driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[1]/a').click() # 1월 선택
        time.sleep(0.5)
        # 끝나는 date 설정
        driver.find_element(By.ID, 'monthEnd').click()
        driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[1]/table/tbody/tr/td[3]/a').click() # 다음 년도로 이동
        driver.find_element(By.XPATH, '//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[4]/td[3]/a').click() # 12월 선택
        driver.find_element(By.XPATH, '//*[@id="lookup-wrap"]/input').click() # 조회 버튼 클릭
        time.sleep(3)

        # 방문자수 추이
        driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/a').click() # ... 클릭
        driver.find_element(By.XPATH, '//*[@id="1264"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
        time.sleep(0.5)
        # 팝업창 제어
        tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
        tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
        tmp.find_element(By.ID, 'submit').click() # 제출 클릭
        time.sleep(3)

        # 방문자 거주지 분포
        place_container = driver.find_element(By.ID, '1202')
        place_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
        driver.find_element(By.XPATH, '//*[@id="1202"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
        time.sleep(0.5)
        # 팝업창 제어
        tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
        tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
        tmp.find_element(By.ID, 'submit').click() # 제출 클릭
        time.sleep(3)
        
        # 방문자 성/연령 분포
        sex_container = driver.find_element(By.ID, '1267')
        sex_container.find_element(By.CLASS_NAME, 'menu-more-wrap').click() # ... 클릭
        driver.find_element(By.XPATH, '//*[@id="1267"]/div[1]/div[2]/ul/li[2]/p[2]/a').click() # 데이터 다운로드 클릭
        time.sleep(0.5)
        # 팝업창 제어
        tmp = driver.find_element(By.ID, 'modal_data_util_exmn') # 팝업창 찾기
        tmp.find_element(By.CLASS_NAME, 'data_qna').find_element(By.ID, 'rdoDataUtilExmn5').click() # 학술연구 및 과제수행 선택
        tmp.find_element(By.ID, 'submit').click() # 제출 클릭
        time.sleep(3)
