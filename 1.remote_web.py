from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import uiautomation as auto
import time
import os
import sys

# Selenium WebDriver 설정
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
# options.add_argument("--start-fullscreen")  # 브라우저를 전체 화면으로 엽니다.
options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

# 크롬 드라이버 경로
CHROME_DRIVER_PATH = (
    "C:\PV_REMOTE_v2.9\chromedriver.exe")
service = Service(CHROME_DRIVER_PATH)

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(service=service, options=options)

try:
    # private 주소
    private_url = 'https://192.168.0.9:8886/home'
    
    # public 주소로 이동
    driver.get(private_url)
    
    # 3초 타임 슬립 : DOM 트리 로딩이 생각보다 느려서 타임슬립 걸어야 됨
    time.sleep(3)
    
    # 비공개 페이지에서 고급 버튼 존재 확인
    try:
        if driver.find_element(By.XPATH, "//body[@class='ssl']/div[@class='interstitial-wrapper']/div[@class='nav-wrapper']/button[@id='details-button' and @class='secondary-button small-link' and contains(text(), '고급')]").is_displayed():
            print("고급 버튼이 존재합니다.")
        else:
            print("고급 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("고급 버튼을 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 비공개 페이지에서 고급 버튼 존재 확인
    try:
        if driver.find_element(By.XPATH, "//body[@class='ssl']/div[@class='interstitial-wrapper']/div[@class='nav-wrapper']/button[@id='details-button' and @class='secondary-button small-link' and contains(text(), '고급')]").is_displayed():
            print("고급 버튼이 존재합니다.")
        else:
            print("고급 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("고급 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 비공개 페이지에서 고급 버튼 클릭
    try:
        secondarybtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//body[@class='ssl']/div[@class='interstitial-wrapper']/div[@class='nav-wrapper']/button[@id='details-button' and @class='secondary-button small-link' and contains(text(), '고급')]")))
        actions = ActionChains(driver)\
            .move_to_element(secondarybtn)\
            .click(secondarybtn)\
            .perform()
        print("고급 버튼을 클릭했습니다.")
    except NoSuchElementException:
            print("고급 버튼을 클릭하지 못했습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인
    try:
        if driver.find_element(By.XPATH, "//div[@id='details']/p[@id='final-paragraph']/a[@id='proceed-link' and @class='small-link']").is_displayed():
            print("안전하지 않음 링크가 존재합니다.")
        else:
            print("안전하지 않음 링크가 존재하지 않습니다.")
    except NoSuchElementException:
            print("안전하지 않음 링크를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 비공개 페이지에서 (안전하지 않음) 링크 클릭
    try:
        small_linkbtn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='details']/p[@id='final-paragraph']/a[@id='proceed-link' and @class='small-link']")))
        actions = ActionChains(driver)\
            .move_to_element(small_linkbtn)\
            .click(small_linkbtn)\
            .perform()
        print("안전하지 링크를 클릭했습니다.")
    except NoSuchElementException:
        print("Remote v2.9 화면으로 이동했습니다.")
        
    # 3초 타임 슬립 : DOM 트리 로딩이 생각보다 느려서 타임슬립 걸어야 됨
    time.sleep(3)
    
    # 아이디 입력 필드 존재 확인
    try:
        id_input_field = driver.find_element(
            By.XPATH, "//div[@class='email-input el-input el-input--suffix']/input[@type='text' and @autocomplete='off' and @name='email']")
        if id_input_field.is_displayed():
            print("아이디 입력 필드가 존재합니다.")
        else:
            print("아이디 입력 필드가 존해하지 않습니다.")
    except NoSuchElementException:
        print("로그인 입력 필드를 찾을 수 없습니다. ")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 패스워드 입력 필드 존재 확인
    try:
        password_field = driver.find_element(
                By.XPATH, "//div[@class='password-input el-input el-input--suffix']/input[@type='password' and @autocomplete='off' and @name='password']")
        if password_field.is_displayed():
            print("패스워드 입력 필드가 존재합니다.")
        else:
            print("패스워드 입력 필드가 존재하지 않습니다.")
    except NoSuchElementException:
        print("패스워드 입력 필드를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로그인 버튼이 존재하는지 확인
    try:
        login_btn = driver.find_element(
            By.XPATH, "//div[@class='el-col el-col-24']/button[@disabled='disabled' and @type='button' and @class='el-button next-btn block-btn el-button--info is-disabled']/span[text()='로그인']")
        if login_btn.is_displayed():
            print("로그인 버튼이 존재합니다.")
        else:
            print("로그인 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("로그인 버튼을 찾을 수 없습니다.")
        
    # 3초안동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입력되는 아이디와 패스워드를 변수 값에 넣기
    Login_id = 'user1'
    Password = 'Admin1324'
    
    # 아이디 입력
    try:
        user_id = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='email-input el-input el-input--suffix']/input[@type='text' and @autocomplete='off' and @name='email']")))
        actions = ActionChains(driver)\
            .send_keys_to_element(user_id, Login_id)\
            .perform()
        print("아이디를 입력했습니다.")
    except NoSuchElementException:
            print("아이디를 입력하지 못했습니다.")
            
    # 아이디와 입력된 값 비교
    if user_id.get_attribute("value") == Login_id:
        print("아이디가 일치합니다.")
    else:
        print("아이디가 일치하지 않습니다.")
        
    # 3초안동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 패스워드 입력
    try:
        user_pwd = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
            (By.XPATH, "//div[@class='password-input el-input el-input--suffix']/input[@type='password' and @autocomplete='off' and @name='password']")))
        actions = ActionChains(driver)\
            .send_keys_to_element(user_pwd, Password)\
            .perform()
        print("패스워드를 입력했습니다.")
    except NoSuchElementException:
            print("패스워드를 입력하지 못했습니다.")
            
    # 패스워드와 입력된 값 비교
    if user_pwd.get_attribute("value") == Password:
        print("패스워드가 일치합니다.")
    else:
        print("패스워드가 일치하지 않습니다.")
        
    # 3초안동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로그인 버튼 클릭
    logbtn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='el-button next-btn block-btn el-button--info']")))
    actions = ActionChains(driver)\
            .move_to_element(logbtn)\
            .click(logbtn)\
            .perform()
    print("로그인 버튼을 클릭하였습니다.")
    
    # 로그인 결과 확인
    try:
        if driver.find_element(By.XPATH, "//section[@class='remote-layout']"):
            print("로그인 성공!")
        else:
            print("로그인에 실패했습니다.")
    except NoSuchElementException:
        print("로그인 화면을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 중복 로그인에 대한 예외 처리
    try:
        try:
            duplicate_login = driver.find_element(
                    By.XPATH, "//div[@class='swal2-content']/div[@id='swal2-content' and @class='swal2-html-container' and @style='display: block;']")
            if duplicate_login.is_displayed():
                print("다른 장치에서 이미 로그인 중입니다. 계속 하시려면 상대방의 접속을 종료시켜주세요.")
                swal2_actions = driver.find_element(
                    By.XPATH, "//div[@class='swal2-actions']/button[@class='swal2-confirm swal2-styled' and contains(text(), '원격종료')]")
                actions = ActionChains(driver)\
                    .move_to_element(swal2_actions)\
                    .click(swal2_actions)\
                    .perform()
                print("원격종료 버튼을 클릭했습니다.")
            else:
                print("중복 로그인 알림창이 출력되지 않았습니다.")
        except NoSuchElementException:
            print("중복 로그인 알림창을 찾을 수 없습니다.")
    except NoSuchElementException:
        print("Remote 화면으로 이동합니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 워크스페이스 메뉴 존재 확인
    try:
        work_space = driver.find_element(By.XPATH, "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']")
        if work_space.is_displayed():
            print("워크스페이스가 메뉴가 존재합니다.")
        else:
            print("워크스페이스 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("워크스페이스 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 워크스페이스 메뉴 클릭하기
    work_space_option = [
        {
            "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector']",
            "message": "워크스페이스 메뉴를 클릭했습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector selected']",
            "message": "워크스페이스 메뉴를 닫았습니다.",
            "timeout": 5
            }
        ]
    for work_space_xpath in work_space_option:
        work_space_btn = WebDriverWait(driver, work_space_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, work_space_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(work_space_btn)\
            .click(work_space_btn)\
            .perform()
        print(work_space_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 영상 메뉴 존재 확인
    try:
        display_menu = driver.find_element(By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[1][@class='tooltip']")
        if display_menu.is_displayed():
            print("영상 on/off 메뉴가 존재합니다.")
        else:
            print("영상 on/off 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("영상 on/off 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 영상 off > on 동작하기
    video_display_option = [
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button active toggle-header stream']",
            "message": "영상을 off 하였습니다.",
            "timeout": 5
            },
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button toggle-header stream']",
            "message": "영상을 on 하였습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button active toggle-header stream']",
            "message": "영상을 off 하였습니다.",
            "timeout": 5
            },
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[1][@class='tooltip']/button[@class='toggle-button toggle-header stream']",
            "message": "영상을 on 하였습니다.",
            "timeout": 5
            }
        ]
    for video_display_xpath in video_display_option:
        video_display_btn = WebDriverWait(driver, video_display_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, video_display_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(video_display_btn)\
            .click(video_display_btn)\
            .perform()
        print(video_display_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 마이크 메뉴 존재 확인
    try:
        mic_menu = driver.find_element(By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[2][@class='tooltip']")
        if mic_menu.is_displayed():
            print("마이크 on/off 메뉴가 존재합니다.")
        else:
            print("마이크 on/off 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("마이크 on/off 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 마이크 on > off 동작하기
    mic_option_1 = [
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button toggle-header mic']",
            "message": "마이크를 on 하였습니다.",
            "timeout": 5
            },
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button active toggle-header mic']",
            "message": "마이크를 off 하였습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button toggle-header mic']",
            "message": "마이크를 on 하였습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//ul[@class='header-workspace-tools']/div[2][@class='tooltip']/button[@class='toggle-button active toggle-header mic']",
            "message": "마이크를 off 하였습니다.",
            "timeout": 5
            }
        ]
    for mic_xpath_1 in mic_option_1:
        mic_btn_1 = WebDriverWait(driver, mic_xpath_1["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, mic_xpath_1["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(mic_btn_1)\
            .click(mic_btn_1)\
            .perform()
        print(mic_xpath_1["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 스피커 메뉴 존재 확인
    try:
        speaker_menu = driver.find_element(By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']")
        if speaker_menu.is_displayed():
            print("스피커 on/off 메뉴가 존재합니다.")
        else:
            print("영상 on/off 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("스피커 on/off 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 스피커 off > on 동작하기
    speaker_option = [
        {
            "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button active toggle-header speaker']",
            "message": "스피커를 off 하였습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button toggle-header speaker']",
            "message": "스피커를 on 하였습니다.",
            "timeout": 5
            },
        {
            "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button active toggle-header speaker']",
            "message": "스피커를 off 하였습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[3][@class='tooltip']/button[@class='toggle-button toggle-header speaker']",
            "message": "스피커를 on 하였습니다.",
            "timeout": 5
            }
        ]
    for speaker_xpath_1 in speaker_option:
        speaker_btn = WebDriverWait(driver, speaker_xpath_1["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, speaker_xpath_1["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(speaker_btn)\
            .click(speaker_btn)\
            .perform()
        print(speaker_xpath_1["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴 존재 확인
    try:
        noti_menu = driver.find_element(By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[1][@class='popover--wrapper']")
        if noti_menu.is_displayed():
            print("알림 메뉴가 존재합니다.")
        else:
            print("알림 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("알림 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 알림 메뉴 클릭
    noti_menu_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[1][@class='popover--wrapper']/button[@class='toggle-button header-tools__notice toggle-header ']")))
    actions = ActionChains(driver)\
        .move_to_element(noti_menu_btn)\
        .click(noti_menu_btn)\
        .perform()
    print("알림 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 알림 리스트 옵션 박스 메뉴 존재 확인
    try:
        noti_list_opt = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__body']/div[@class='popover-notice__empty']")
        if noti_list_opt.is_displayed():
            print("알림 리스트 옵션 박스가 존재합니다.")
        else:
            print("알림 리스트 옵션 박스가 존재하지 않습니다.")
    except NoSuchElementException:
        print("알림 리스트 옵션 박스를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 알림 Push off > on > 알림 메뉴 닫기
    noti_menu_option = [
        {
            "xpath": "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__header']/span[text()='알림']/following-sibling::div[@class='switcher']/div[@class='switcher-toggle toggle']",
            "message": "Push를 off 했습니다.",
            "timeout": 5
            },
        {
            "xpath": "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-notice']/div[@class='popover--body']/div/div[@class='popover-notice__header']/span[text()='알림']/following-sibling::div[@class='switcher']/div[@class='switcher-toggle']",
            "message": "Push를 on 했습니다.",
            "timeout": 5
            },
        
        {
            "xpath": "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[1][@class='popover--wrapper']/button[@class='toggle-button header-tools__notice toggle-header visible']",
            "message": "알림 메뉴를 닫았습니다.",
            "timeout": 5
            }
        ]
    for noti_menu_xpath in noti_menu_option:
        noti_btn = WebDriverWait(driver, noti_menu_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, noti_menu_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(noti_btn)\
            .click(noti_btn)\
            .perform()
        print(noti_menu_xpath["message"])
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴 존재 확인
    try:
        my_profile_menu = driver.find_element(
            By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']")
        if my_profile_menu.is_displayed():
            print("나의 프로필 메뉴가 존재합니다.")
        else:
            print("나의 프로필 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("나의 프로필 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴 클릭
    my_profile = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']/figure[@class='profile']/div[@class='profile--thumb']")))
    actions = ActionChains(driver)\
        .move_to_element(my_profile)\
        .click(my_profile)\
        .perform()
    print("나의 프로필 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 리스트 존재 확인
    try: 
        my_profile_list = driver.find_element(By.XPATH,
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']")
        if my_profile_list.is_displayed():
            print("나의 프로필 옵션 박스 메뉴가 존재합니다.")
        else:
            print("나의 프로필 옵션 박스 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("나의 프로필 옵션 박스 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 > 워크스테이션 메뉴 존재 확인
    try:
        work_station_menu = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '워크스테이션')]")
        if work_station_menu.is_displayed():
            print("워크스테이션 매뉴가 존재합니다.")
        else:
            print("워크스테이션 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("워크스테이션 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 > 대시보드 매뉴 존재 확인
    try:
        dash_board_menu = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '대시보드')]")
        if dash_board_menu.is_displayed():
            print("대시보드 메뉴가 존재합니다.")
        else:
            print("대시보드 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("대시보드 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 > 로컬 파일 메뉴 존재 확인
    try:
        local_file_menu = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로컬 녹화 파일')]")
        if local_file_menu.is_displayed():
            print("로컬 녹화 파일 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 파일 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 파일 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 > 로그아웃 메뉴 존재 확인
    try:
        logout_menu = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로그아웃')]")
        if logout_menu.is_displayed():
            print("로그아웃 메뉴가 존재합니다.")
        else:
            print("로그아웃 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로그아웃 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴 클릭
    my_profile = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']/figure[@class='profile visible']/div[@class='profile--thumb']")))
    actions = ActionChains(driver)\
        .move_to_element(my_profile)\
        .click(my_profile)\
        .perform()
    print("나의 프로필 메뉴를 닫았습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성 버튼 존재 확인
    try:
        remote_collaboration_btn = driver.find_element(By.XPATH, "//button[@class='btn' and contains(text(), '원격 협업 생성')]")
        if remote_collaboration_btn.is_displayed():
            print("원격 협업 생성 버튼이 존재합니다.")
        else:
            print("원격 협업 생성 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("원격 협업 생성 버튼을 찾을 수 없습니다.")
        
    # 오픈 룸 생성 버튼 존재 확인
    try:
        remote_open_room = driver.find_element(By.XPATH, "//button[@class='btn workspace-welcome__open' and contains(text(), '오픈 룸 생성')]")
        if remote_open_room.is_displayed():
            print("오픈 룸 생성 버튼이 존재합니다.")
        else:
            print("오픈 룸 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("오픈 룸 생성 버튼을 찾을 수 없습니다.")
        
    # 원격 협업 탭 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        remote_collaboration_tab = driver.find_element(By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][1]/button[@class='active' and contains(text(), '원격 협업')]")
        if remote_collaboration_btn.is_displayed():
            print("원격 협업 탭이 존재합니다.")
        else:
            print("원격 협업 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("원격 협업 탭을 찾을 수 없습니다.")
        
    # 원격 협업 탭 > 협업 이름 검색창 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        collaboration_name = driver.find_element(By.XPATH, "//div[@class='search tab-view__search']/input[@type='text' and @placeholder='협업 이름 검색' and @class='search__input']")
        if collaboration_name.is_displayed():
            print("협업 이름 검색창이 존재합니다.")
        else:
            print("협업 이름 검색창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("협업 검색창을 찾을 수 없습니다.")
        
    # 원격 협업 탭 > 새로고침 버튼 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        collaboration_refresh = driver.find_element(By.XPATH, "//div[@class='search tab-view__search']/button[@class='search__input-icon disabled']")
        if collaboration_refresh.is_displayed():
            print("새로고침 버튼이 존재합니다.")
        else:
            print("새로고침 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("새로고침 버튼을 찾을 수 없습니다.")
        
    # 원격 협업 탭 선택
    btnactive1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][1]/button[@class='active' and contains(text(), '원격 협업')]")))
    actions = ActionChains(driver)\
        .move_to_element(btnactive1)\
        .click(btnactive1)\
        .perform()
    print("원격 협업 탭을 선택했습니다.")
    
    # 3초 타임 슬립 : 협업 이름 검색창 클릭을 시각으로 확인 할 수 있어야 해서 타입 슬립 대기
    time.sleep(3)
    
    # 원격 협업 탭 > 협업 검색창 클릭
    serch1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='search tab-view__search']/input[@type='text' and @placeholder='협업 이름 검색' and @class='search__input']")))
    actions = ActionChains(driver)\
        .move_to_element(serch1)\
        .click(serch1)\
        .perform()
    print("협업 이름 검색창을 클릭했습니다.")
    
    # 3초 타임 슬립 : 새로고침 동작을 시각으로 확인 할 수 있어야 해서 타임 슬립 대기
    time.sleep(3)
    
    # 원격 협업 탭 > 새로고침 버튼 선택
    refresh1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='tab-view__tools']/button[@class='icon-button refresh']")))
    actions = ActionChains(driver)\
        .move_to_element(refresh1)\
        .click(refresh1)\
        .perform()
    print("새로고침 버튼을 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 목록 확인
    try:
        remote_collaboration_list = driver.find_element(By.XPATH, "//div[@class='tab-view__body offsetwidth']/div[@class='show-empty']")
        if remote_collaboration_list.is_displayed():
            print("원격 협업 목록이 없습니다.")
        else:
            print("원격 협업 목록이 있습니다.")
    except NoSuchElementException:
        print("원격 협업 목록을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 최근 기록 탭 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        recent_record_tab = driver.find_element(By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][2]/button[1]")
        if recent_record_tab.is_displayed():
            print("최근 기록 탭이 존재합니다.")
        else:
            print("최근 기록 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("최근 기록 탭을 찾을 수 없습니다.")
        
    # 3초 타임 슬립 : 최근 기록 탭 클릭하는 것 시각으로 확인해야 함
    time.sleep(3)
    
    # 최근 기록 탭 선택
    btnactive2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][2]/button[1]")))
    actions = ActionChains(driver)\
        .move_to_element(btnactive2)\
        .click(btnactive2)\
        .perform()
    print("최근 기록 탭을 선택했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 최근 기록 탭 > 협업 이름 검색창 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        collaboration_name_serch = driver.find_element(
            By.XPATH, "//section[@class='tab-view history']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/div[@class='search tab-view__search']")
        if collaboration_name_serch.is_displayed():
            print("협업 검색창이 존재합니다.")
        else:
            print("협업 검색창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("협업 검색창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 최근 기록 탭 > 전체 삭제 버튼 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        all_delete_btn = driver.find_element(
            By.XPATH, "//section[@class='tab-view history']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button delete']")
        if all_delete_btn.is_displayed():
            print("전체 삭제 버튼이 존재합니다.")
        else:
            print("전체 삭제 버튼이 존해하지 않습니다.")
    except NoSuchElementException:
        print("전체 삭제 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 최근 기록 탭 > 새로고침 버튼 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        recent_record_refresh = driver.find_element(
            By.XPATH, "//section[@class='tab-view history']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button refresh']")
        if recent_record_refresh.is_displayed():
            print("새로고침 버튼이 존재합니다.")
        else:
            print("새로고침 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("새로고침 버튼을 찾을 수 없습니다.")
        
    # 3초 타임 슬립 : 최근 기록 탭 클릭하는 것 시각으로 확인해야 함
    time.sleep(3)
    
    # 최근 기록 탭 > 협업 검색창 클릭
    serch2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view history']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/div[@class='search tab-view__search']")))
    actions = ActionChains(driver)\
        .move_to_element(serch2)\
        .click(serch2)\
        .perform()
    print("협업 검색창을 클릭했습니다.")
    
    # 3초 타임 슬립 : 최근 기록 탭 클릭하는 것 시각으로 확인해야 함
    time.sleep(3)
    
    refresh2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view history']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button refresh']")))
    actions = ActionChains(driver)\
        .move_to_element(refresh2)\
        .click(refresh2)\
        .perform()
    print("새로고침 버튼을 클릭했습니다.")
    
    # 멤버 탭 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        member_tab = driver.find_element(
            By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][3]/button[1]")
        if member_tab.is_displayed():
            print("멤버 탭이 존재합니다.")
        else:
            print("멤버 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("멤버 탭이 존재하지 않습니다.")
        
    # 멤버 탭 선택
    btnactive3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][3]/button[1]")))
    actions = ActionChains(driver)\
        .move_to_element(btnactive3)\
        .click(btnactive3)\
        .perform()
    print("멤버 탭을 선택했습니다.")
    
    # 3초 타임 슬립 : 멤버 탭 클릭하는 것은 시각으로 확인해야 함
    time.sleep(3)
    
    # 멤버 탭 > 멤버 검색창 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        member_serch = driver.find_element(
            By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/div[@class='search tab-view__search']")
        if member_serch.is_displayed():
            print("멤버 검색창이 존재합니다.")
        else:
            print("멤버 검색창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("멤버 검색창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 멤버 탭 > 새로고침 버튼 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        member_refresh = driver.find_element(By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button refresh']")
        if member_refresh.is_displayed():
            print("새로고침 버튼이 존재합니다.")
        else:
            print("새로고침 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("새로고침 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 멤버 탭 > 즐겨찾기 버튼 존재 확인 : 해당 UI 요소가 없을 경우 NoSuchElementException 예외 처리함
    try:
        member_favorite_btn = driver.find_element(
                By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button favourite']")
        if member_favorite_btn.is_displayed():
            print("즐겨찾기 버튼이 존재합니다.")
        else:
            print("즐겨찾기 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("즐겨찾기 버튼을 찾을 수 없습니다.")
        
    # 3초 타임 슬립 : 협업 검색창을 클릭하는 것은 시각으로 확인해야 함
    time.sleep(3)
    
    # 멤버 탭 > 멤버 검색창 클릭
    serch3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/div[@class='search tab-view__search']/input[@type='text' and @placeholder='멤버 검색' and @class='search__input']")))
    actions = ActionChains(driver)\
        .move_to_element(serch3)\
        .click(serch3)\
        .perform()
    print("협업 검색창을 클릭했습니다.")
    
    # 3초 타임 슬립 : 협업 검색창을 클릭하는 것은 시각으로 확인해야 함
    time.sleep(3)
    
    # 멤버 탭 > 새로고침 버튼 클릭
    refresh3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button refresh']")))
    actions = ActionChains(driver)\
        .move_to_element(refresh3)\
        .click(refresh3)\
        .perform()
    print("새고침 버튼을 클릭했습니다.")
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 멤버 탭 > 즐겨찾기 버튼 클릭
    favourite = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button favourite']")))
    actions = ActionChains(driver)\
        .move_to_element(favourite)\
        .click(favourite)\
        .perform()
    print("즐겨찾기 버튼을 클릭했습니다.")
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 버튼 선택 > 즐겨찾기 생성 상태 확인
    try:
        create_favorite_btn = driver.find_element(By.XPATH, "//div[@class='show-empty']/div[@class='show-empty__inner']")
        if create_favorite_btn.is_displayed():
            print("생성한 즐겨찾기가 없습니다.")
        else:
            print("생성한 즐겨찾기가 있습니다.")
    except NoSuchElementException:
        print("생성한 즐겨찾기를 찾을 수 없습니다.")
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 멤버 버튼 존재 확인
    try:
        member_btn = driver.find_element(By.XPATH, "//button[@class='icon-button member']")
        if member_btn.is_displayed():
            print("멤버 버튼이 존재합니다.")
        else:
            print("멤버 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("멤버 버튼을 찾을 수 없습니다.")
        
    # 멤버 버튼 클릭
    iconbtnmem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='icon-button member']")))
    actions = ActionChains(driver)\
        .move_to_element(iconbtnmem)\
        .click(iconbtnmem)\
        .perform()
    print("멤버 버튼을 클릭했습니다.")
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 버튼 클릭
    favourite = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='tab-view__header offsetwidth']/div[@class='tab-view__tools']/button[@class='icon-button favourite']")))
    actions = ActionChains(driver)\
        .move_to_element(favourite)\
        .click(favourite)\
        .perform()
    print("즐겨찾기 버튼을 클릭했습니다.")
    
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가 버튼 존재 확인
    try:
        favorite_add_btn = driver.find_element(By.XPATH, "//button[@class='icon-button add-group']")
        if favorite_add_btn.is_displayed():
            print("즐겨찾기 추가 버튼이 존재합니다.")
        else:
            print("즐겨찾기 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("즐겨찾기 버튼을 찾을 수 없습니다.")
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가 버튼 클릭
    addfavourite = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='icon-button add-group']")))
    actions = ActionChains(driver)\
        .move_to_element(addfavourite)\
        .click(addfavourite)\
        .perform()
    print("즐겨찾기 추가 버튼을 클릭했습니다.")
    
    # 3초 타임 슬립 : 즐겨찾기 추가 버튼 클릭하면 모달창 출력되는 동시에 순간 다음 스크립트 수행되어 타임 슬립 진행
    time.sleep(3)
    
    # 즐겨찾기 추가/수정 모달창 출력 여부 확인
    try:
        favorite_modal_open = driver.find_element(By.XPATH, "//div[@class='modal--body']")
        if favorite_modal_open.is_displayed():
            print("즐겨찾기 추가/수정 모달창이 출력 되었습니다.")
        else:
            print("즐겨찾기 추가/수정 모달창이 출력되지 않았습니다.")
    except NoSuchElementException:
        print("즐겨찾기 추가/수정 모달창을 찾을 수 없습니다.")
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 그룹 리스트가 decorated 상태 일 때 예외 처리
    try:
        collapsible_button = driver.find_element(
            By.XPATH, "//button[@class='collapsible__button decorated']")
        if 'opend' not in collapsible_button.get_attribute('class'):
            collapsible_button.click()
    except NoSuchElementException:
        print("그룹 리스트가 출력되었습니다.")
        
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 닫기 버튼 존재 확인
    try:
        favorite_modal_close = driver.find_element(By.XPATH, "//div[@class='modal--header']/button[@class='modal--close']")
        if favorite_modal_close.is_displayed():
            print("즐겨찾기 모달창 닫기 버튼이 존재합니다.")
        else:
            print("즐겨찾기 모달창 닫기 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("즐겨찾기 모달창 닫기 버튼을 찾을 수 없습니다.")
        
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 > 즐겨찾기 이름 입력 필드 존재 확인
    try:
        favorite_name_field = driver.find_element(
            By.XPATH, "//div[@class='member-group']/figure[@class='inputrow']/input[@type='text' and @placeholder='즐겨찾기 이름' and @class='inputrow-input input']")
        if favorite_name_field.is_displayed():
            print("즐겨찾기 이름 입력 필드가 존재합니다.")
        else:
            print("즐겨찾기 이름 입력 필드가 존재하지 않습니다.")
    except NoSuchElementException:
        print("즐겨찾기 이름 입력 필드를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 > 새로고침 버튼 존재 확인
    try:
        favorite_fresh_btn = driver.find_element(By.XPATH, "//button[@class='icon-button refresh']")
        if favorite_fresh_btn.is_displayed():
            print("새로고침 버튼이 존재합니다.")
        else:
            print("새로고침 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("새로고침 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 > collapsible button 존재 확인
    try:
        favorite_collapsible_btn = driver.find_element(By.XPATH, 
            "//div[@class='collapsible member-collapsible opend decorated']/button[@type='button' and @class='collapsible__button opend decorated']")
        if favorite_collapsible_btn.is_displayed():
            print("collapsible button이 존재합니다.")
        else:
            print("collapsible button 존재하지 않습니다.")
    except NoSuchElementException:
        print("collapsible button을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # widecard 리스트 출력 확인
    try:
        widecard_list = driver.find_element(
                By.XPATH, "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']")
        if widecard_list.is_displayed():
            print("widecard 리스트가 출력되었습니다.")
        else:
            print("widecard 리스트가 출력되지 않았습니다.")
    except NoSuchElementException:
        print("widecard 리스트을 찾을 수 없습니다.")
        
    # 5초 타임 슬립 모드
    time.sleep(5)
    
    # collapsible button > 스크롤 동작 > # 아래로 스크롤
    vue_scrollbar = driver.find_element(
        By.XPATH, "//div[@class='createroom-user__body']/div[@class='vue-scrollbar__wrapper']")
    
    # 스크롤 아래로 이동
    driver.execute_script(
        "arguments[1].scrollTop += arguments[1].offsetHeight;", vue_scrollbar, vue_scrollbar)
    
    # 5초 타임 슬립 모드
    time.sleep(5)
    
    # 스크롤 위로 이동
    driver.execute_script(
        "arguments[0].scrollTop -= arguments[1].offsetHeight;", vue_scrollbar, vue_scrollbar)
    
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 확인 버튼 존재 확인
    try:
        save_confirmation_btn = driver.find_element(
                By.XPATH, "//div[@class='member-group']/button[@disabled='disabled' and @class='btn save-group' and contains(text(), '확인 0/5')]")
        if save_confirmation_btn.is_displayed():
            print("SAVE 확인 버튼이 존재합니다.")
        else:
            print("SAVE 확인 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("SAVE 확인 버튼을 찾을 수 없습니다.")
        
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 > 새로고침 버튼 클릭
    refresh4 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='icon-button refresh']")))
    actions = ActionChains(driver)\
        .move_to_element(refresh4)\
        .click(refresh4)\
        .perform()
    print("새로고침 버튼을 클릭했습니다.")
    
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨 찾기 그룹 추가하기 > 즐겨찾기 이름 입력
    favourite_group_add = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='text' and @placeholder='즐겨찾기 이름' and @maxlength='20' and @class='inputrow-input input']")))
    actions = ActionChains(driver)\
        .send_keys_to_element(favourite_group_add, '즐겨찾기 1')\
        .perform()
    print("즐겨찾기 이름 입력 필드를 클릭하였습니다.")
    
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # widecard list > Admin/master 계정 선택
    widecard_choice1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='collapsible__content opend']/div[1][@class='widecard choice']")))
    actions = ActionChains(driver)\
        .move_to_element(widecard_choice1)\
        .click(widecard_choice1)\
        .perform()
    print("어드민 멤버를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # widecard list > Admin/master 계정 다시 선택
    widecard_choice1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='collapsible__content opend']/div[1][@class='widecard choice selected']")))
    actions = ActionChains(driver)\
        .move_to_element(widecard_choice1)\
        .click(widecard_choice1)\
        .perform()
    print("어드민 멤버를 재선택 하여  해제했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 버튼 상태 변경을 확인할 함수
    button_xpath = "//div[@class='member-group']/button[@disabled='disabled' and @class='btn save-group' and contains(text(), '확인 0/5')]"
    def check_button_status():
        savebtn = driver.find_element(
            By.XPATH, "//div[@class='member-group']/button[@disabled='disabled' and @class='btn save-group' and contains(text(), '확인 0/5')]")
        return savebtn.is_displayed()
    
    # 버튼 상태 변경 확인
    is_status_changed = check_button_status()
    if is_status_changed:
        print("'확인 0/5'으로 상태가 변경되었습니다." + str(is_status_changed))
    else:
        print("리스트 해제했지만 상태가 변경되지 않았습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 즐겨찾기 추가/수정 모달창 닫기
    modalclose = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='modal--header']/button[@class='modal--close']")))
    actions = ActionChains(driver)\
        .move_to_element(modalclose)\
        .click(modalclose)\
        .perform()
    print("즐겨찾기 추가/수정 모달창을 닫았습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 탭 존재 확인
    try:
        setting_btn = driver.find_element(By.XPATH, 
            "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][4]/button[1]")
        if setting_btn.is_displayed():
            print("환경 설정 탭이 존재합니다.")
        else:
            print("환경 설정 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("환경 설정 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 탭 클릭
    enviro_set = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='workspace-tab']/nav[@class='workspace-tab__nav']/ul[@class='flex offsetwidth']/li[@class='workspace-tab__button'][4]/button[1]")))
    actions = ActionChains(driver)\
        .move_to_element(enviro_set)\
        .click(enviro_set)\
        .perform()
    print("환경 설정 탭을 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 탭 > 메인 메뉴 출력 확인
    try:
        setting_main_menu = driver.find_element(By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']")
        if setting_main_menu.is_displayed():
            print("환경 설정 메인 메뉴가 출력되었습니다.")
        else:
            print("환경 설정 메인 메뉴가 출력되지 않았습니다.")
    except NoSuchElementException:
        print("환경 설정 메인 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 메인 메뉴 > 영상 설정 메뉴 클릭
    video_settings = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[2][@class='setting-nav__menu active' and contains(text(), '영상 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(video_settings)\
        .click(video_settings)\
        .perform()
    print("영상 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경설정 > 영상 설정 > 카메라 메뉴 존재 확인
    try:
        display_camera_menu = driver.find_element(By.XPATH, "//figure[1][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']")
        if display_camera_menu.is_displayed():
            print("영상 설정 : 카메라 메뉴가 존재합니다.")
        else:
            print("영상 설정 : 카메라 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("영상 설정 : 카메라 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 영상 설정 > 카메라 메뉴 클릭
    camera_btn_option = [
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '카메라')]/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "영상 설정 : 카메라 메뉴를 클릭했습니다.",
            "camera_start" : True
            },
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '카메라')]/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "영상 설정 : 카메라 메뉴를 닫았습니다.",
            "camera_end" : False
            }
        ]
    for camera_btn_xpath in camera_btn_option:
        camera_btn_click = WebDriverWait(driver, camera_btn_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, camera_btn_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(camera_btn_click)\
            .click(camera_btn_click)\
            .perform()
        print(camera_btn_xpath["message"])
        time.sleep(3)
        
        if "camera_start" in camera_btn_xpath:
            time.sleep(3)
            
            # 환경설정 > 영상 설정 > 카메라 메뉴 > 카메라 옵션 박스 메뉴 존재 확인
            try:
                camera_option_box = driver.find_element(
                    By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if camera_option_box.value_of_css_property('display') != 'none':
                    print("영상 설정 : 카메라 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("영상 설정 : 카메라 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("영상 설정 : 카메라 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "camera_end" in camera_btn_xpath:
            pass
    
    # 3초 동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입력 해상도 메뉴 존재 확인
    try:
        input_resolution_menu = driver.find_element(By.XPATH, "//figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']")
        if input_resolution_menu.is_displayed():
            print("영상 설정 : 입력 해상도 메뉴가 존재합니다.")
        else:
            print("영상 설정 : 입력 해상도 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("영상 설정 : 입력 해상도 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입력 해상도 > Default : 720p 확인
    try:
        input_resolution_default = driver.find_element(By.XPATH, 
            "//figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']/span[text()='720p(HD)']")
        if input_resolution_default.is_displayed():
            print("입력 해상도 Default는 720p입니다.")
        else:
            print("입력 해상도 Default 값이 720p가 아닙니다.")
    except NoSuchElementException:
        print("입력 해상도 Default 값을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 영상 설정 > 입력 해상도 버튼 클릭
    input_resolution_option = [
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/p[@class='setting__label' and contains(text(), '입력 해상도')]/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "입력 해상도 메뉴를 클릭했습니다.",
            "input_start" : True
            },
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/p[@class='setting__label' and contains(text(), '입력 해상도')]/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "입력 해상도 메뉴를 닫았습니다.",
            "input_end" : True
            }
        ]
    for input_resolution_xpath in input_resolution_option:
        resolution_box = WebDriverWait(driver, input_resolution_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, input_resolution_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(resolution_box)\
            .click(resolution_box)\
            .perform()
        print(input_resolution_xpath["message"])
        time.sleep(3)
        
        if "input_start" in input_resolution_xpath:
            time.sleep(3)
            
            # 입력 해상도 버튼 클릭 > 입력 해상도 옵션 박스 출력
            try:
                input_resolutions_option_box = driver.find_element(
                    By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if input_resolutions_option_box.value_of_css_property('display') != 'none':
                    print("입력 해상도 선택 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("입력 해상도 선택 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("입력 해상도 선택 옵션 박스를 찾을 수 없습니다.")
        
        elif "input_end" in input_resolution_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입력 해상도 버튼 클릭 > 480p 클릭
    input_option = [
        ('480p(VGA)', '480p(VGA)를 선택했습니다.'),
        ('360p', '360p를 선택했습니다.'),
        ('720p(HD)', '720p(HD)를 선택했습니다.')
        ]
    for resolution, resolution_message in input_option:
        input_resolution_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(input_resolution_btn)\
            .click(input_resolution_btn)\
            .perform()
        print("입력 해상도 버튼을 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        input_resolution = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, f"//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{resolution}')]")))
        actions = ActionChains(driver)\
            .move_to_element(input_resolution)\
            .click(input_resolution)\
            .perform()
        print(resolution_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 카메라 화면 존재 확인
    try:
        camera_display = driver.find_element(By.XPATH, "//figure[@class='setting__figure video']/div[@class='setting-video']")
        if camera_display.is_displayed():
            print("영상 미리보기 화면이 존재합니다.")
        else:
            print("영상 미리보기 화면이 존재하지 않습니다.")
    except NoSuchElementException:
        print("영상 미리보기 화면을 찾을 수 없습니다.")
        
    #3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # ActionChains 객체 생성
    # progress bar 영역에 롱 클릭 액션 추가
    # 마우스를 왼쪽으로 이동하는 액션 추가
    # 액션 실행
    # Default 30FPS(왼쪽) > 25FPS(오른쪽)로 이동
    FPS_progress_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[3][@class='setting-section__body horizon']/figure[2][@class='setting__figure slidecontainer']/div[@class='range-slider']/input[@type='range' and @min='1' and @max='30' and @step='1']")))
    actions = ActionChains(driver)\
        .click_and_hold(FPS_progress_bar)\
        .move_by_offset(119, 0)\
        .perform()
    # @value 속성 값 가져오기
    value = FPS_progress_bar.get_attribute("value")
    
    # FPS 값 출력 확인
    print(value +  "FPS 값이 적용되었습니다.")
    
    # 5초 타임 슬립
    time.sleep(3)
    
    # Default 25FPS(왼쪽) > 1FPS(오른쪽)로 이동
    FPS_progress_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[3][@class='setting-section__body horizon']/figure[2][@class='setting__figure slidecontainer']/div[@class='range-slider']/input[@type='range' and @min='1' and @max='30' and @step='1']")))
    actions = ActionChains(driver)\
        .click_and_hold(FPS_progress_bar)\
        .move_by_offset(-200, 119)\
        .perform()
    # @value 속성 값 가져오기
    value = FPS_progress_bar.get_attribute("value")
    
    # FPS 값 출력 확인
    print(value + "FPS 값이 적용되었습니다.")
    
    # default 30FPS 상태임
    # 30 FPS x=0, 8FPS x=-100,
    # 15FPS x=-10(-10, 0), 22FPS x=90(90, 0), 24FPS x=110(110, 0) 25FPS x=119(119, 0)
    # 4FPS x=-115(-115, 119), 15FPS x=0(0, -200), 1FPS x=-200(-200, 119), 30FPS x=200(200, -200)
    
    # 5초 타임 슬립
    time.sleep(3)
    
    # Default 1FPS(왼쪽) > 30FPS(오른쪽)로 이동
    FPS_progress_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[3][@class='setting-section__body horizon']/figure[2][@class='setting__figure slidecontainer']/div[@class='range-slider']/input[@type='range' and @min='1' and @max='30' and @step='1']")))
    actions = ActionChains(driver)\
        .click_and_hold(FPS_progress_bar)\
        .move_by_offset(200, -210)\
        .perform()
    # @value 속성 값 가져오기
    value = FPS_progress_bar.get_attribute("value")
    
    # FPS 값 출력 확인
    print(value + "FPS 값이 적용되었습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 메인 메뉴 > 오디오 설정 메뉴 클릭
    audio_settings = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[3][@class='setting-nav__menu' and contains(text(), '오디오 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(audio_settings)\
        .click(audio_settings)\
        .perform()
    print("오디오 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입력 장치 버튼 존재 확인
    try:
        input_device_btn = driver.find_element(By.XPATH, 
            "//div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']")
        if input_device_btn.is_displayed():
            print("입력 장치 옵션 메뉴가 존재합니다.")
        else:
            print("입력 장치 옵션 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("입력 장치 옵션 메뉴를 찾을 수 업습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입출력 장치 > 입력 장치 버튼 클릭
    input_device_option = [
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "입력 장치 메뉴를 클릭했습니다.",
            "device_start" : True
            },
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "입력 장치 메뉴를 닫았습니다.",
            "device_end" : False
            }
        ]
    for input_device_xpath in input_device_option:
        input_device_btn = WebDriverWait(driver, input_device_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, input_device_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(input_device_btn)\
            .click(input_device_btn)\
            .perform()
        print(input_device_xpath["message"])
        
        if "device_start" in input_device_xpath:
            time.sleep(3)
            
            # 입력 장치 옵션 박스 버튼 존재 확인
            try:
                input_device_option_box = driver.find_element(
                    By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if input_device_option_box.value_of_css_property('display') != 'none':
                    print("입력 장치 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("입력 장치 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("입력 장치 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "device_end" in input_device_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 출력 장치 버튼 존재 확인
    try:
        output_device_btn = driver.find_element(By.XPATH, 
            "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")
        if output_device_btn.is_displayed():
            print("출력 장치 버튼이 존재합니다.")
        else:
            print("출력 장치 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("출력 장치 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 입출력 장치 > 출력 장치 버튼 클릭
    output_device_option = [
        {
            "xpath" :  "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "출력장치 버튼을 클릭하였습니다.", 
            "output_start" : True
            },
        {
            "xpath" :  "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "출력장치 버튼을 닫았습니다.",
            "output_end" : False
            }
        ]
    for output_device_xpath in output_device_option:    
        output_device_btn = WebDriverWait(driver, output_device_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, output_device_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(output_device_btn)\
            .click(output_device_btn)\
            .perform()
        print(output_device_xpath["message"])
        
        if "output_start" in output_device_xpath:
            time.sleep(3)
            
            # 출력 장치 옵션 박스 버튼 존재 확인
            try:
                output_device_option_box = driver.find_element(
                    By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if output_device_option_box.value_of_css_property('display') != 'none':
                    print("출력 장치 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("출력 장치 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("출력 장치 옵션 박스 메뉴를 찾을 수 없습니다.")
        
        elif "output_end" in output_device_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 마이크 테스트 버튼 존재 확인
    try:
        mic_test_btn = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body horizon']/div[1][@class='mic-item']/button[@class='btn' and contains(text(), '마이크 테스트')]")
        if mic_test_btn.is_displayed():
            print("마이크 테스트 버튼이 존재합니다.")
        else:
            print("마이크 테스트 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("마이크 테스트 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 마이크 테스트 버튼 클릭 : 마이크 테스트 버튼 클릭
    mic_option_2 = [
        {
            "xpath": "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body mic horizon']/div[1][@class='mic-item']/button[@class='btn' and contains(text(), '마이크 테스트')]",
            "message" : "마이크 테스트 버튼을 클릭했습니다.",
            "timeout" : 5
            },
        {
            "xpath": "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body mic horizon']/div[1][@class='mic-item']/button[@class='btn' and contains(text(), '마이크 테스트')]",
            "message": "마이크 테스트 버튼을 해제했습니다.",
            "timeout": 5
            }
        ]
    for mic_xpath_2 in mic_option_2:
        mic_btn_2 = WebDriverWait(driver, mic_xpath_2["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, mic_xpath_2["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(mic_btn_2)\
            .click(mic_btn_2)\
            .perform()
        print(mic_xpath_2["message"])
        time.sleep(5)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 오디오 설정 > 토글 마이크 존재 확인
    try:
        toggle_mic = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body mic horizon']/div[@class='mic-item__progress']/button[@class='toggle-button mic-radius']")
        if toggle_mic.is_displayed():
            print("오디오 설정 : 토글 마이크 버튼이 존재합니다.")
        else:
            print("오디오 설정 : 토글 마이크 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("오디오 설정 : 토글 마이크 버튼을 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 오디오 설정 > 토글 마이크 클릭
    toggle_mic_option = [
        {
            "xpath" : "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body mic horizon']/div[@class='mic-item__progress']/button[@class='toggle-button mic-radius']",
            "timeout" : 5,
            "message" : "토글 마이크 버튼을 클릭했습니다."
            },
        {
            "xpath" : "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body mic horizon']/div[@class='mic-item__progress']/button[@class='toggle-button mic-radius active']",
            "timeout" : 5,
            "message" : "토글 마이크 버튼을 해제했습니다."
            }
        ]
    for toggle_mic_xpath in toggle_mic_option:
        toggle_mic_click = WebDriverWait(driver, toggle_mic_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, toggle_mic_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(toggle_mic_click)\
            .click(toggle_mic_click)\
            .perform()
        print(toggle_mic_xpath["message"])
        time.sleep(5)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 녹화 설정 메뉴 클릭
    recording_setting = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, 
        "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[4][@class='setting-nav__menu' and contains(text(), '녹화 설정')]")))
    actions = ActionChains(driver, 5)\
        .move_to_element(recording_setting)\
        .click(recording_setting)\
        .perform()
    print("녹화 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 녹화 설정 > 로컬 녹화 설정 > 최대 녹화 시간 메뉴 존재 확인
    try:
        recording_local_set = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']")
        if recording_local_set.is_displayed():
            print("로컬 녹화 시간 : 최대 녹화 시간 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 시간 : 최대 녹화 시간 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 시간 : 최대 녹화 시간 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 녹화 설정 > 로컬 녹화 설정 > 최대 녹화 시간 메뉴 클릭
    recording_time_option = [
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[1][@class='select-label']",
            "timeout" : 5,
            "message" : "로컬 녹화 시간 : 최대 녹화 시간 메뉴를 클릭했습니다.",
            "recording_start" : True
            },
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[1][@class='select-label active']",
            "timeout" : 5,
            "message" : "로컬 녹화 시간 : 최대 녹화 시간 메뉴를 닫았습니다.",
            "recording_end" : False
            }
        ]
    for recording_time_xpath in recording_time_option:
        recording_time_click = WebDriverWait(driver, recording_time_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, recording_time_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(recording_time_click)\
            .click(recording_time_click)\
            .perform()
        print(recording_time_xpath["message"])
        time.sleep(3)
        
        if "recording_start" in recording_time_xpath:
            time.sleep(3)
            
            # 최대 녹화 시간 옵션 박스 존재 확인
            try:
                recording_option_box = driver.find_element(
                        By.XPATH, "//div[@role='tooltip' and @class='popover select-options reverse']/div[@class='popover--body']/div[@class='select-optionbox']")
                if recording_option_box.value_of_css_property('display') != 'none':
                    print("로컬 녹화 설정 : 최대 녹화 시간 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("로컬 녹화 설정 : 최대 녹화 시간 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 설정 : 최대 녹화 시간 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "recording_end" in recording_time_xpath:
            pass
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 최대 녹화 시간 메뉴 순차적으로 클릭 : 1분 > 5분 > 10분 > 15분 > 30분 > 45분 > 60분 > 90분 > 120분 > Default 60분 선택
    recording_option = [
        ('1 분', '로컬 녹화 : 최대 녹화 시간 : 1분을 선택했습니다.'),
        ('5 분', '로컬 녹화 : 최대 녹화 시간 : 5분을 선택했습니다.'),
        ('10 분', '로컬 녹화 : 최대 녹화 시간 : 10분을 선택했습니다.'),
        ('15 분', '로컬 녹화 : 최대 녹화 시간 : 15분을 선택했습니다.'),
        ('30 분', '로컬 녹화 : 최대 녹화 시간 : 30분을 선택했습니다.'),
        ('45 분', '로컬 녹화 : 최대 녹화 시간 : 45분을 선택했습니다.'),
        ('60 분', '로컬 녹화 : 최대 녹화 시간 : 60분을 선택했습니다.'),
        ('90 분', '로컬 녹화 : 최대 녹화 시간 : 90분을 선택했습니다.'),
        ('120 분', '로컬 녹화 : 최대 녹화 시간 : 120분을 선택했습니다.'),
        ('60 분', '로컬 녹화 : 최대 녹화 시간 : 60분을 선택했습니다.')
        ]
    for recording_click, recording_message in recording_option:
        recording_time_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
        "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[1][@class='setting__figure']/span[1][@class='popover--wrapper setting__r-selecter']/button[1][@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(recording_time_btn)\
            .click(recording_time_btn)\
            .perform()
        print("로컬 녹화 시간 :> 최대 녹화 시간 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 최대 녹화 순차적으로 클릭
        recording_max_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[6][@role='tooltip']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{recording_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(recording_max_click)\
            .click(recording_max_click)\
            .perform()
        print(recording_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
        # 녹화 설정 > 로컬 녹화 설정 > 녹화 간격 메뉴 존재 확인
    try:
        recording_duration_menu = driver.find_element(
            By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")
        if recording_duration_menu.is_displayed():
            print("로컬 녹화 : 녹화 간격 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 녹화 간격 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 : 녹화 간격 메뉴를 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 설정 > 녹화 간격 버튼 클릭
    recording_duration_option = [
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 녹화 간격 메뉴를 클릭했습니다",
            "duration_start" : True
            },
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 녹화 간격 메뉴를 클릭했습니다",
            "duration_end" : False
        }
    ]
    for recording_duration_xpath in recording_duration_option:
        recording_duration_click = WebDriverWait(driver, recording_duration_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, recording_duration_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(recording_duration_click)\
            .click(recording_duration_click)\
            .perform()
        print(recording_duration_xpath["message"])
        time.sleep(3)
        
        if "duration_start" in recording_duration_xpath:
            time.sleep(3)
            
            # 녹화 간격 옵션 박스 메뉴 존재 확인
            try:
                recording_duration_option_box = driver.find_element(
                    By.XPATH, "//div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if recording_duration_option_box.value_of_css_property('display') != 'none':
                    print("로컬 녹화 : 녹화 간격 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("로컬 녹화 : 녹화 간격 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 : 녹화 간격 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "duration_end" in recording_duration_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 녹화 간격 클릭 : 1분 > 5분 > 10분 > 20분
    recording_duration_option = [
        ('5 분', '로컬 녹화 : 녹화 간격 5분을 선택했습니다.'),
        ('10 분', '로컬 녹화 : 녹화 간격 10분을 선택했습니다.'),
        ('20 분', '로컬 녹화 : 녹화 간격 20분을 선택했습니다.'),
        ('1 분', '로컬 녹화 : 녹화 간격 1분을 선택했습니다.')
        ]
    for recording_duration_click, recording_duration_message in recording_duration_option:
        recording_duration_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(recording_duration_btn)\
            .click(recording_duration_btn)\
            .perform()
        print(recording_duration_message)
        time.sleep(3)
        
        # 3초 동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 녹화 간격 클릭 : 1분 > 5분 > 10분 > 20분 연속으로 클릭
        recording_duration_time = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[7][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{recording_duration_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(recording_duration_time)\
            .click(recording_duration_time)\
            .perform()
        print("로컬 녹화 :> 녹화 간격 메뉴를 클릭했습니다.")
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 녹화 설정 > 로컬 녹화 설정 > 녹화 영상 해상도 메뉴 존재 확인
    try:
        setting_recording_resolution = driver.find_element(
            By.XPATH, "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']")
        if setting_recording_resolution.is_displayed():
            print("로컬 녹화 : 녹화 영상 해상도 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 녹화 영상 해상도 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 : 녹화 영상 해상도 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 녹화 설정 > 녹화 영상 해상도 메뉴 클릭
    resolution_option = [
        {
            "xpath" : "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5, 
            "message" : "로컬 녹화 : 녹화 영상 해상도 메뉴를 클릭했습니다.",
            "resolution_start" : True
            },
        {
            "xpath" : "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5, 
            "message" : "로컬 녹화 : 녹화 영상 해상도 메뉴를 닫았습니다.",
            "resolution_end" : False
            }
        ]
    for resolution_option_xpath in resolution_option:
        recording_video_resolution = WebDriverWait(driver, resolution_option_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, resolution_option_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(recording_video_resolution)\
            .click(recording_video_resolution)\
            .perform()
        print(resolution_option_xpath["message"])
        time.sleep(3)
        
        if "resolution_start" in resolution_option_xpath:
            time.sleep(3)
            
            # 환경 설정 > 녹화 설정 > 녹화 영상 해상도 옵션 박스 메뉴 존재 확인
            try:    
                video_resolution_option_box = driver.find_element(
                    By.XPATH, "//div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if video_resolution_option_box.value_of_css_property('display') != 'none':
                    print("로컬 녹화 : 녹화 영상 해상도 옵션 메뉴가 존재합니다.")
                else:
                    print("로컬 녹화 : 녹화 영상 해상도 옵션 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 : 녹화 영상 해상도 옵션 메뉴를 찾을 수 없습니다.")
        
        elif "resolution_end" in resolution_option_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 녹화 설정 > 녹화 영상 해상도 클릭 : 360p > 480p > 720p > Default 480p
    video_resolution_option = [
        
        ('360p', '로컬 녹화 : 녹화 영상 해상도 360p를 클릭했습니다.'),
        ('480p', '로컬 녹화 : 녹화 영상 해상도 480p를 클릭했습니다.'),
        ('720p', '로컬 녹화 : 녹화 영상 해상도 720p를 클릭했습니다.'),
        ('480p', '로컬 녹화 : 녹화 영상 해상도 480p를 클릭했습니다.')
        ]
    for video_resolution_click,  video_resolution_message in video_resolution_option:
        recording_video_resolution = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '로컬 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
        .move_to_element(recording_video_resolution)\
        .click(recording_video_resolution)\
        .perform()
        print("로컬 녹화 :> 녹화 영상 해상도 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        recording_resolution_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[8][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{video_resolution_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(recording_resolution_btn)\
            .click(recording_resolution_btn)\
            .perform()
        print(video_resolution_message)
        time.sleep(3)
        
    # 5초동안 암묵적 대기
    time.sleep(5)
    
    # 마우스 이용하여 화면을 상,하 컨트롤 > 화면을 아래로 스크롤 이동
    # progress bar 엘리먼트 찾기
    scroll_bar = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='remote-layout']/div[@class='vue-scrollbar__wrapper remote-wrapper workspace']")))
    
    # 스크롤 아래로 이동
    driver.execute_script(
        "arguments[1].scrollTop += arguments[1].offsetHeight;", scroll_bar, scroll_bar)
    
    # 5초 타임 슬립 모드
    time.sleep(5)
    
    # 스크롤 위로 이동
    driver.execute_script(
        "arguments[0].scrollTop -= arguments[1].offsetHeight;", scroll_bar, scroll_bar)
    
    # 5초 타임 슬립 모드
    time.sleep(5)
    
    # 스크롤 아래로 이동
    driver.execute_script(
        "arguments[1].scrollTop += arguments[1].offsetHeight;", scroll_bar, scroll_bar)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 > 최대 녹화 시간 메뉴 존재 확인
    try:
        setting_server_recording = driver.find_element(By.XPATH, 
        "//div[@class='setting-section__title']/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '최대 녹화 시간')]/following-sibling::span[@class='popover--wrapper setting__r-selecter']")
        if setting_server_recording.is_displayed():
            print("서버 녹화 : 최대 녹화 시간 메뉴가 존재합니다.")
        else:
            print("서버 녹화 : 최대 녹화 시간 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("서버 녹화 : 최대 녹화 시간 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 시간 > 최대 녹화 시간 메뉴 클릭
    maximum_time_option = [
        {
            "xpath" : "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "서버 녹화 : 최대 녹화 시간 메뉴를 클릭했습니다.",
            "maximum_start" : True
            },
        {
            "xpath" : "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "서버 녹화 : 최대 녹화 시간 메뉴를 닫았습니다.",
            "maximum_end" : False
            }
        ]
    for maximum_time_xpath in maximum_time_option:
        maximum_recording_time = WebDriverWait(driver, maximum_time_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, maximum_time_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_time)\
            .click(maximum_recording_time)\
            .perform()
        print(maximum_time_xpath["message"])
        
        if "maximum_start" in maximum_time_xpath:
            time.sleep(3)
            
            # 서버 녹화 > 최대 녹화 시간 메뉴 옵션 박스 메뉴 존재 확인
            try:
                maximum_recording_option_box = driver.find_element(By.XPATH, 
                    "//div[@role='tooltip' and @class='popover select-options reverse']/div[@class='popover--body']/div[@class='select-optionbox']")
                if maximum_recording_option_box.value_of_css_property('display') != 'none':
                    print("서버 녹화 : 최대 녹화 시간 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("서버 녹화 : 최대 녹화 시간 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("서버 녹화 : 최대 녹화 시간 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "maximum_end" in maximum_time_xpath:
            pass
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 설정 > 최대 녹화 시간 클릭 : 5분 > 15분 > 30분 > 60분
    maximum_recording_option = [
        ('5 분', '서버 녹화 : 최대 시간 5분을 클릭했습니다.'),
        ('15 분', '서버 녹화 : 최대 시간 15분을 클릭했습니다.'),
        ('30 분', '서버 녹화 : 최대 시간 30분을 클릭했습니다.'),
        ('60 분', '서버 녹화 : 최대 시간 60분을 클릭했습니다.'),
        ('30 분', '서버 녹화 : 최대 시간 30분을 클릭했습니다.')
        ]
    for maximum_recording_click, maximum_recording_message in maximum_recording_option:
        maximum_recording_time = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_time)\
            .click(maximum_recording_time)\
            .perform()
        print("서버 녹화 :> 최대 녹화 시간 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        maximum_recording_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[9][@role='tooltip']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{maximum_recording_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_btn)\
            .click(maximum_recording_btn)\
            .perform()
        print(maximum_recording_message)
        time.sleep(3)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 녹화 설정 > 서버 녹화 설정 > 녹화 영상 해상도 메뉴 클릭
    video_resolution_btn_option = [
        {
            "xpath" : "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/div[@class='setting__figure--wrapper']/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "서버 녹화 : 녹화 영상 해상도 메뉴를 클릭했습니다.",
            "video_start" : True
            },
        {
            "xpath" : "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/div[@class='setting__figure--wrapper']/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "서버 녹화 : 녹화 영상 해상도 메뉴를 닫았습니다.",
            "video_end" : False
            }
        ]
    for resolution_btn_xpath in video_resolution_btn_option:
        video_resolution_btn = WebDriverWait(driver, resolution_btn_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, resolution_btn_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(video_resolution_btn)\
            .click(video_resolution_btn)\
            .perform()
        print(resolution_btn_xpath["message"])
        time.sleep(3)
        
        if "video_start" in resolution_btn_xpath:
            time.sleep(3)
            
            # 녹화 영상 해상도 옵션 박스 메뉴 존재 확인
            try:
                video_resolution_option_box = driver.find_element(
                    By.XPATH, "//div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if video_resolution_option_box.value_of_css_property('display') != 'none':
                    print("서버 녹화 : 녹화 영상 해상도 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("서버 녹화 : 녹화 영상 해상도 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("서버 녹화 : 녹화 영상 해상도 옵션 박스 메뉴를 찾을 수 없습니다.")
                
        elif "video_end" in resolution_btn_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 > 녹화 영상 해상도 클릭 : 480p > 720p > 1080p
    video_resolution_option = [
        ('480p', '서버 녹화 : 녹화 영상 해상도 480p를 클릭했습니다.'),
        ('720p', '서버 녹화 : 녹화 영상 해상도 720p를 클릭했습니다.'),
        ('1080p', '서버 녹화 : 녹화 영상 해상도 1080p를 클릭했습니다.'),
        ('720p', '서버 녹화 : 녹화 영상 해상도 720p를 클릭했습니다.')
        ]
    for resolution_click, resolution_click_message in video_resolution_option:
        video_resolution_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/div[@class='setting__figure--wrapper']/following-sibling::span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(video_resolution_btn)\
            .click(video_resolution_btn)\
            .perform()
        print("서버 녹화 :> 녹화 영상 해상도 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        redording_resolution_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[10][@role='tooltip']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{resolution_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(redording_resolution_btn)\
            .click(redording_resolution_btn)\
            .perform()
        print(resolution_click_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 > 자동 서버 녹화 > 자동 서버 사용 존재 확인
    try:
        setting_server_auto = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[2][@class='setting-section']/div[@class='setting-section__body']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '자동 서버 녹화')]/following-sibling::div[@class='check']")
        if setting_server_auto.is_displayed():
            print("서버 녹화 : 자동 녹화 사용 메뉴가 존재합니다.")
        else:
            print("서버 녹화 : 자동 녹화 사용  메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("서버 녹화 : 자동 녹화 사용 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 환경 설정 > 서버 녹화 설정 > 자동 서버 녹화 메뉴 클릭 및 해제
    auto_server_option = [
        {
            "xpath": "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '자동 서버 녹화')]/following-sibling::div[@class='check']",
            "message": "서버 녹화 : 자동화 서버 녹화 사용 메뉴를 체크했습니다.",
            "timeout" : 5
            },
        {
            "xpath": "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '자동 서버 녹화')]/following-sibling::div[@class='check toggle']",
            "message": "서버 녹화 : 자동화 서버 녹화 사용 메뉴를 해제했습니다.",
            "timeout": 5
            },
        {
            "xpath": "//div[@class='setting-section__title' and contains(text(), '서버 녹화 설정')]/following-sibling::div[@class='setting-section__body']/figure[@class='setting__figure']/p[@class='setting__label' and contains(text(), '자동 서버 녹화')]/following-sibling::div[@class='check']",
            "message": "서버 녹화 : 자동화 서버 녹화 사용 메뉴를 다시 체크했습니다.",
            "timeout": 5
            }
        ]
    for auto_server_xpath in auto_server_option:
        auto_server_check = WebDriverWait(driver, auto_server_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, auto_server_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(auto_server_check)\
            .click(auto_server_check)\
            .perform()
        print(auto_server_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 언어 설정 메뉴 클릭
    language_set = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[5][@class='setting-nav__menu' and contains(text(), '언어 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(language_set)\
        .click(language_set)\
        .perform()
    print("언어 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 언어 설정 > 언어 선택 메뉴 존재 확인
    try:
        setting_language_select = driver.find_element(By.XPATH, 
            "//section[@class='setting-section language']/div[@class='setting-section__title main' and contains(text(), '언어 선택')]/following-sibling::div[@class='radio-custom']/div[@class='radio-group']")
        if setting_language_select.is_displayed():
            print("언어 설정 : 언어 선택 메뉴가 존재합니다.")
        else:
            print("언어 설정 : 언어 선택 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("언어 설정 : 언어 선택 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 언어 설정 > 언어 선택 > 영어 > 일본어 > 중국어(간체) > 중국어(본체) > 에스파니아 > 한국어 순서대로 클릭
    language_select = [
        ('en', '언어 설정 : 영어를 선택했습니다.'),
        ('ja', '언어 설정 : 일본어를 선택했습니다.'),
        ('zh-cn', '언어 설정 : 중국어(간체)를 선택했습니다.'),
        ('zh-tw', '언어 설정 : 중국어(본체)를 선택했습니다.'),
        ('es', '언어 설정 : 에스파니아어를 선택했습니다.'),
        ('ko', '언어 설정 : 한국어를 선택했습니다.')
        ]
    for select, select_message in language_select:
        language_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='setting-section language']/div[@class='setting-section__title main']/following-sibling::div[@class='radio-custom']/div[@class='radio-group']/label[@class='radio-option']/span[@class='radio-option__input']/input[@type='radio' and @value='{select}']")))
        actions = ActionChains(driver)\
            .move_to_element(language_btn)\
            .click(language_btn)\
            .perform()
        print(select_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 메뉴 클릭
    translation_set = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[6][@class='setting-nav__menu' and contains(text(), '번역 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(translation_set)\
        .click(translation_set)\
        .perform()
    print("번역 설정 메뉴를 선택했습니다.")
    
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 환경 설정 > 번역 설정 > 번역 사용 > 번역 사용 허용 메뉴 존재 확인
    try:
        setting_translation_check = driver.find_element(By.XPATH, 
            "//div[@class='setting-view__body']/div/section[@class='setting-section list']/div[@class='setting-section__title main' and contains(text(), '번역 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label']/following-sibling::div[@class='check']")
        if setting_translation_check.is_displayed():
            print("번역 설정 : 번역 사용 허용 메뉴가 존재합니다.")
        else:
            print("번역 설정 : 번역 사용 허용 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("번역 설정 : 번역 사용 허용 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 번역 사용 > 번역 사용 허용 체크
    translation_option = [
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section list']/div[@class='setting-section__title main' and contains(text(), '번역 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label']/following-sibling::div[@class='check']/span[@class='check-toggle']",
            "message": "번역 설정 : 번역 사용 허용 체크하였습니다.",
            "timeout" : 5
            },
        {
            "xpath" : "//div[@class='setting-view__body']/div/section[@class='setting-section list']/div[@class='setting-section__title main' and contains(text(), '번역 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label']/following-sibling::div[@class='check toggle']/span[@class='check-toggle toggle']",
            "message": "번역 설정 : 번역 사용 허용 체크 해제했습니다.",
            "timeout" : 5
            },
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section list']/div[@class='setting-section__title main' and contains(text(), '번역 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/p[@class='setting__label']/following-sibling::div[@class='check']/span[@class='check-toggle']",
            "message": "번역 설정 : 번역 사용 허용 다시 체크하였습니다.",
            "timeout": 5
            }
        ]
    for translation_xpath in translation_option:
        translation_check = WebDriverWait(driver, translation_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, translation_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(translation_check)\
            .click(translation_check)\
            .perform()
        print(translation_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 번역 언어 설정 메뉴 클릭
    language_select_option = [
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "번역 설정 : 번역 언어 설정 메뉴를 클릭했습니다.",
            "language_start" : True
            },
        {
            "xpath" : "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "번역 설정 : 번역 언어 설정 메뉴를 닫았습니다.",
            "language_end" : False
            }
        ]
    for language_select_xpath in language_select_option:
        language_select_box = WebDriverWait(driver, language_select_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, language_select_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(language_select_box)\
            .click(language_select_box)\
            .perform()
        print(language_select_xpath["message"])
        time.sleep(3)
        
        if "language_start" in language_select_xpath:
            time.sleep(3)
            
            # 환경 설정 > 번역 설정 > 번역 언어 설정 옵션 박스 메뉴 존재 확인
            try:
                setting_translation_language = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options scroll']/div[@class='popover--body']/div[@class='ps']/div[@class='select-optionbox']")
                if setting_translation_language.is_displayed():
                    print("번역 설정 : 번역 언어 설정 옵션 박스 메뉴가 존재합니다.")
                else:
                    print("번역 설정 : 번역 언어 설정 옵션 박스 메뉴가 존재하지 않습니다.")
            except NoSuchElementException:
                print("번역 설정 : 번역 언어 설정 옵션 박스 메뉴를 찾을 수 없습니다.")
        
        elif "language_end" in language_select_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 번역 언어 설정
    translation_language = [
        ('English', '번역 설정 : 영어를 선택했습니다.'),
        ('日本語', '번역 설정 : 일본어를 선택했습니다.'),
        ('中文', '번역 설정 : 중국어를 선택했습니다.'),
        ('française', '번역 설정 : 프랑스어를 선택했습니다.'),
        ('Español', '번역 설정 : 에스파니아어를 선택했습니다.'),
        ('русский', '번역 설정 : 러시아어를 선택했습니다.'),
        # ('Український', '우크라이나어를 선택했습니다.'),
        # ('Polski', '폴란드어를 선택했습니다.'),
        # ('ไทย', '태국어를 선택했습니다.'),
        ('한국어', '번역 설정 : 한국어를 선택했습니다.')
        ]
    for language, language_message in translation_language:
        language_select_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//div[@class='setting-section__body horizon']/figure[2][@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(language_select_box)\
            .click(language_select_box)\
            .perform()
        print("번역 설정 :> 번역 언어 설정 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        language_select_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//section[@class='remote-layout']/div[6][@role='tooltip']/div[@class='popover--body']/div[@class='ps']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{language}')]")))
        actions = ActionChains(driver)\
            .move_to_element(language_select_btn)\
            .click(language_select_btn)\
            .perform()
        print(language_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 원본/번역 출력 방식 메뉴 존재 확인
    try:
        original_translation_output = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/div/section[2][@class='setting-section list']/div[@class='setting-section__title' and contains(text(), '번역/원본 출력 방식')]/following-sibling::div[@class='slider']")
        if original_translation_output.is_displayed():
            print("번역 설정 : 번역/원본 출력 방식 메뉴가 존재합니다.")
        else:
            print("번역 설정 : 번역/원본 출력 방식 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("번역 설정 : 번역/원본 출력 방식 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 번역/원본 출력 방식 : 선택 출력 클릭 > 동시 출력 클릭
    translation_original = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='setting-view__body']/div/section[2][@class='setting-section list']/div[@class='setting-section__title' and contains(text(), '번역/원본 출력 방식')]/following-sibling::div[@class='slider']")))
    for i in range(2):
        actions = ActionChains(driver)\
            .move_to_element(translation_original)\
            .click(translation_original)\
            .perform()
        print("번역/원본 출력 방식 슬라이드 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # "active" 상태 문구 출력 할 수 있는 xpath
        active_path_1 = "//div[@class='setting-view__body']/div/section[2][@class='setting-section list']/div[@class='setting-section__title' and contains(text(), '번역/원본 출력 방식')]/following-sibling::div[@class='slider']/span[contains(@class, 'slider-option') and contains(@class, 'active')]"
        
        # XPath 요소 찾기
        active_element_1 = driver.find_element(By.XPATH, active_path_1)
        
        # 번역/원본 출력 방식 텍스트 가져오기
        active_text_1 = active_element_1.text
        print(active_text_1 + "으로 선택되었습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 음성 인식 방식(STT) 메뉴 존재 확인
    try:
        translation_voice = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/div/section[3][@class='setting-section list horizon translate']/figure[@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 인식 방식')]/following-sibling::div[@class='slider']")
        if translation_voice.is_displayed():
            print("번역 설정 : 음성 인식 방식(STT) 메뉴가 존재합니다.")
        else:
            print("번역 설정 : 음성 인식 방식(STT) 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("번역 설정 : 음성 인식 방식(STT) 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 환경 설정 > 번역 설정 > 음성 인식 방식(STT) 클릭
    voice_recognition_stt = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='setting-view__body']/div/section[3][@class='setting-section list horizon translate']/figure[@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 인식 방식')]/following-sibling::div[@class='slider']")))
    for i in range(2):
        actions = ActionChains(driver)\
            .move_to_element(voice_recognition_stt)\
            .click(voice_recognition_stt)\
            .perform()
        print("번역 설정 : 음성 인식 방식(STT) 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # "active" 상태 문구 출력 할 수 있는 xpath
        active_xpath_2 = "//div[@class='setting-view__body']/div/section[3][@class='setting-section list horizon translate']/figure[@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 인식 방식')]/following-sibling::div[@class='slider']/span[contains(@class, 'slider-option') and contains(@class, 'active')]"
        
        # xpath 요소 찾기
        active_element_2 = driver.find_element(By.XPATH, active_xpath_2)
        
        # 음성 인식 방식(STT) 텍스트 가져 오기
        active_text_2 = active_element_2.text
        print(active_text_2 + "으로 선택되었습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 번역 설정 > 음성 변환 설정(TTS) 메뉴 존재 확인
    try:
        setting_translation_voice = driver.find_element(By.XPATH, 
            "//div[@class='setting-view__body']/div/section[@class='setting-section list horizon translate']/figure[2][@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 변환 설정(TTS)')]/following-sibling::div[@class='check']")
        if setting_translation_voice.is_displayed():
            print("번역 설정 : 음성 변환 설정(TTS) 메뉴가 존재합니다.")
        else:
            print("번역 설정 : 음성 변환 설정(TTS) 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("번역 설정 : 음성 변환 설정(TTS) 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 환경 설정 > 번역 설정 > 음성 변환 설정(TTS) > 음성 변환 사용 허용 체크 클릭
    voice_trans_option = [
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section list horizon translate']/figure[2][@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 변환 설정(TTS)')]/following-sibling::div[@class='check']/span[@class='check-toggle']",
            "message": "번역 설정 : 음성 변환 사용 허용 체크 메뉴를 클릭했습니다.",
            "timeout": 5
            },
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section list horizon translate']/figure[2][@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 변환 설정(TTS)')]/following-sibling::div[@class='check toggle']/span[@class='check-toggle toggle']",
            "message": "번역 설정 : 음성 변환 사용 허용 체크 메뉴를 해제 했습니다.",
            "timeout": 5
            },
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section list horizon translate']/figure[2][@class='setting-section__translate']/div[@class='setting-section__title' and contains(text(), '음성 변환 설정(TTS)')]/following-sibling::div[@class='check']/span[@class='check-toggle']",
            "message": "번역 설정 : 음성 변환 사용 허용 체크 메뉴를 클릭했습니다.",
            "timeout": 5
            }
        ]
    for voice_trans_xpath in voice_trans_option:
        voice_trans_check = WebDriverWait(driver, voice_trans_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, voice_trans_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(voice_trans_check)\
            .click(voice_trans_check)\
            .perform()
        print(voice_trans_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 클릭
    function_setting = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[7][@class='setting-nav__menu' and contains(text(), '기능 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(function_setting)\
        .click(function_setting)\
        .perform()
    print("기능 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 > 영상 공유 제어 > 영상 제한 모드 사용 > 영상 제한 모드 사용 메뉴 존재 확인
    try:
        video_restriction_mode = driver.find_element(By.XPATH, 
            "//div[@class='setting-view__body']/div/section[@class='setting-section feature']/div[@class='setting-section__title' and contains(text(), '영상 공유 제어')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/div[@class='check']")
        if video_restriction_mode.is_displayed():
            print("기능 설정 : 영상 제한 모드 사용 메뉴가 존재합니다.")
        else:
            print("기능 설정 : 영상 제한 모드 사용 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("기능 설정 : 영상 제한 모드 사용 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 > 영상 공유 제어 > 영상 제한 모드 사용 > 영상 제한 모드 사용 체크
    video_limit_option = [
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section feature']/div[@class='setting-section__title' and contains(text(), '영상 공유 제어')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/div[@class='check']/span[@class='check-toggle']",
            "message" : "기능 설정 : 영상 제한 모드 사용을 체크하였습니다.",
            "timeout" : 5,
            "limit_check" : True
            },
        {
            "xpath": "//div[@class='setting-view__body']/div/section[@class='setting-section feature']/div[@class='setting-section__title' and contains(text(), '영상 공유 제어')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/div[@class='check toggle']/span[@class='check-toggle toggle']",
            "message": "기능 설정 : 영상 제한 모드 사용을 해제하였습니다.",
            "timeout": 5,
            "limit_check" : False
            }
        ]
    video_limit_count = range(1, 2)
    for i in video_limit_count:
        for video_limit_xpath in video_limit_option:
            video_limit_check = WebDriverWait(driver, video_limit_xpath["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, video_limit_xpath["xpath"])))
            actions = ActionChains(driver)\
                .move_to_element(video_limit_check)\
                .click(video_limit_check)\
                .perform()
            print(video_limit_xpath["message"])
            
            # 영상 제한 on 일 때
            if video_limit_xpath["limit_check"]:
                time.sleep(3)
            #영상 제한 off 일 때
            elif not video_limit_xpath["limit_check"]:
                pass
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 > 협업 지속 시간 설정 메뉴 존재 확인
    try: 
        collaboration_duration = driver.find_element(
            By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '협업 지속 시간 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']")
        if collaboration_duration.is_displayed():
            print("기능 설정 : 협업 지속 시간 메뉴가 존재합니다.")
        else:
            print("기능 설정 : 협업 지속 시간 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("기능 설정 : 협업 지속 시간 메뉴를 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 > 협업 지속 시간 메뉴 클릭
    collaboration_duration_option = [
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '협업 지속 시간 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "기능 설정 : 협업 지속 시간 메뉴를 클릭했습니다.",
            "collaboration_start" : True
            },
        {
            "xpath" : "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '협업 지속 시간 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "기능 설정 : 협업 지속 시간 메뉴를 닫았습니다.",
            "collaboration_end" : False
            }
        ]
    for collaboration_duration_xpath in collaboration_duration_option:
        collaboration_duration_click = WebDriverWait(driver, collaboration_duration_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, collaboration_duration_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(collaboration_duration_click)\
            .click(collaboration_duration_click)\
            .perform()
        print(collaboration_duration_xpath["message"])
        
        if "collaboration_start" in collaboration_duration_xpath:
            time.sleep(3)
            
            # 환경 설정 > 기능 설정 > 협업 지속 시간 옵션 박스 메뉴 존재 확인
            try:
                collaboration_duration_box = driver.find_element(
                    By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options reverse scroll']/div[@class='popover--body']")
                if collaboration_duration_box.is_displayed():
                    print("기능 설정 : 협업 지속 시간 옵션 박스가 존재합니다.")
                else:
                    print("기능 설정 : 협업 지속 시간 옵션 박스가 존재하지 않습니다.")
            except NoSuchElementException:
                print("기능 설정 : 협업 지속 시간 옵션 박스를 찾을 수 없습니다.")
                
        elif "collaboration_end" in collaboration_duration_xpath:
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 기능 설정 > 협업 지속 시간 메뉴 클릭 > 1시간 > 2시간 > 3시간 > 4시간 > 5시간 > 제한 없음 순서대로 클릭
    collaboration_duration_time = [
        ('1시간', '1시간을 선택했습니다.'),
        ('2시간', '2시간을 선택했습니다.'),
        ('3시간', '3시간을 선택했습니다.'),
        ('4시간', '4시간을 선택했습니다.'),
        ('5시간', '5시간을 선택했습니다.'),
        ('6시간', '6시간을 선택했습니다.'),
        ('7시간', '7시간을 선택했습니다.'),
        ('8시간', '8시간을 선택했습니다.'),
        ('9시간', '9시간을 선택했습니다.'),
        ('10시간', '10시간을 선택했습니다.'),
        ('11시간', '11시간을 선택했습니다.'),
        ('12시간', '12시간을 선택했습니다.'),
        ('13시간', '13시간을 선택했습니다.'),
        ('14시간', '14시간을 선택했습니다.'),
        ('15시간', '15시간을 선택했습니다.'),
        ('16시간', '16시간을 선택했습니다.'),
        ('17시간', '17시간을 선택했습니다.'),
        ('18시간', '18시간을 선택했습니다.'),
        ('19시간', '19시간을 선택했습니다.'),
        ('20시간', '20시간을 선택했습니다.'),
        ('21시간', '21시간을 선택했습니다.'),
        ('22시간', '22시간을 선택했습니다.'),
        ('23시간', '24시간을 선택했습니다.'),
        ('24시간', '24시간을 선택했습니다.'),
        ('제한 없음', '제한 없음을 선택했습니다.')
        ]
    for duration_time, duration_message in collaboration_duration_time:
        collaboration_duration_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section']/div[@class='setting-section__title' and contains(text(), '협업 지속 시간 설정')]/following-sibling::div[@class='setting-section__body horizon']/figure[@class='setting__figure']/span[@class='popover--wrapper setting__r-selecter']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(collaboration_duration_click)\
            .click(collaboration_duration_click)\
            .perform()
        print("기능 설정 : 협업 지속 시간 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        collaboration_duration_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, f"//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options reverse scroll']/div[@class='popover--body']/div[@class='ps']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{duration_time}')]")))
        actions = ActionChains(driver)\
            .move_to_element(collaboration_duration_btn)\
            .click(collaboration_duration_btn)\
            .perform()
        print(duration_message)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
        # 환경 설정 > 대화명 설정 클릭
    communi_setting = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//section[@class='tab-view']/div[@class='setting-wrapper offsetwidth']/div[@class='setting-nav']/div[8][@class='setting-nav__menu' and contains(text(), '대화명 설정')]")))
    actions = ActionChains(driver)\
        .move_to_element(communi_setting)\
        .click(communi_setting)\
        .perform()
    print("대화명 설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 메뉴 존재 확인
    try:
        communication_name = driver.find_element(
            By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__title' and contains(text(), '대화명 설정')]")
        if communication_name.is_displayed():
            print("대화명 설정 : 대화명 설정 메뉴가 존재합니다.")
        else:
            print("대화명 설정 : 대화명 설정 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 대화명 설정 메뉴를 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > Defalult 대화명 지우기
    try:
        commnuni_name_clear = driver.find_element(
            By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/input[@class='input']")
        commnuni_name_clear.clear()
    except NoSuchElementException:
        print("대화명 설정 : Default 원격 협업 대화명을 지우지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > 대화명 변경 입력: "test1"으로 입력 > 변경 버튼 클릭
    try:
        communication_name_change = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/input[@class='input']")
        actions = ActionChains(driver)\
            .send_keys_to_element(communication_name_change, 'test1')\
            .perform()
        print("대화명 설정 : 원격 협업 대화명을 test1으로 입력했습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 원격 협업 대화명을 test1으로 입력하지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > 대화명 변경 입력 > 변경 버튼 존재 확인
    try:
        change_button = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/button[@class='input-button']")
        if change_button.is_displayed():
            print("대화명 설정 : 변경 버튼이 존재합니다.")
        else:
            print("대화명 설정 : 변경 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 변경 버튼을 찾을 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > 대화명 변경 > 변경 버튼 클릭
    try:
        change_button_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/button[@class='input-button']")))
        actions = ActionChains(driver)\
            .move_to_element(change_button_click)\
            .click(change_button_click)\
            .perform()
        print("대화명 설정 : 변경 버튼을 클릭하였습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 변경 버튼을 클릭하지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > test1 대화명 지우기
    try:
        commnuni_name_clear = driver.find_element(
            By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/input[@class='input']")
        commnuni_name_clear.clear()
    except NoSuchElementException:
        print("대화명 설정 : Default 원격 협업 대화명을 지우지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 다시 Default 대화명으로 변경 : "user1-Member"
    try:
        communication_name_change = driver.find_element(By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/input[@class='input']")
        actions = ActionChains(driver)\
            .send_keys_to_element(communication_name_change, 'user1-Member')\
            .perform()
        print("대화명 설정 : 원격 협업 대화명을 user1-Member으로 입력했습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 원격 협업 대화명을 user1-Member으로 입력하지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 대화명 설정 > 원격 협업 대화명 > Default 대화명으로 다시 변경 > 변경 버튼 클릭
    try:
        change_button_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='setting-view__body']/section[@class='setting-section nickname']/div[@class='setting-section__body']/figure[@class='setting__figure']/div[@class='input-button-container']/button[@class='input-button']")))
        actions = ActionChains(driver)\
            .move_to_element(change_button_click)\
            .click(change_button_click)\
            .perform()
        print("대화명 설정 : 변경 버튼을 클릭하였습니다.")
    except NoSuchElementException:
        print("대화명 설정 : 변경 버튼을 클릭하지 못했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 메뉴 클릭
    my_profile = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/span[2][@class='popover--wrapper']/figure[@class='profile']/div[@class='profile--thumb']")))
    actions = ActionChains(driver)\
        .move_to_element(my_profile)\
        .click(my_profile)\
        .perform()
    print("나의 프로필 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 리스트 존재 확인
    try: 
        my_profile_list = driver.find_element(By.XPATH,
            "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']")
        if my_profile_list.is_displayed():
            print("나의 프로필 옵션 박스 메뉴가 존재합니다.")
        else:
            print("나의 프로필 옵션 박스 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("나의 프로필 옵션 박스 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 나의 프로필 > 로그아웃 메뉴 존재 확인
    try:
        logout_menu = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로그아웃')]")
        if logout_menu.is_displayed():
            print("로그아웃 메뉴가 존재합니다.")
        else:
            print("로그아웃 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로그아웃 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    logout_menu_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover popover-profile']/div[@class='popover--body']/div/div[@class='popover-profile__linklist']/div[@class='popover-profile__link']/button[contains(text(), '로그아웃')]")))
    actions = ActionChains(driver)\
        .move_to_element(logout_menu_btn)\
        .click(logout_menu_btn)\
        .perform()
    print("로그아웃 버튼을 클릭했습니다.")
    
finally:
    # 브라우저 세션 종료
    driver.quit()
    print("브라우저창을 닫습니다.")