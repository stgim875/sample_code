from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pywinauto.application import Application
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 색상 선택
from class_file.color_pallet import ColorPallet

import uiautomation as auto
import time

# Selenium WebDriver 설정
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

# 크롬 드라이버 경로
CHROME_DRIVER_PATH = (
    "C:\PV_REMOTE_v2.9\chromedriver.exe")
service = Service(CHROME_DRIVER_PATH)

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(service=service, options=options)

try: 
    # WebRTC_Internal 페이지로 이동
    driver.get('chrome://webrtc-internals/')
    print("webRTC_Internal 페이지로 이동합니다.")
    
    # 페이지 로딩 시간 측정 시작
    start_time = time.time()
    
    # JavaScript 함수 실행
    driver.execute_script("console.log();")
    
    # 페이지 로딩 시간 측정 종료
    end_time = time.time()
    
    # 페이지 로딩 시간 측정 종료
    print("페이지 로딩 시간 : ", end_time - start_time)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # Read stats From에서 Legacy Non-Standard (callback-based) getStats() API 선택
    Legacy = driver.find_element(
        By.XPATH, "//select[@id='statsSelectElement']/option[@value = 'Legacy Non-Standard (callback-based) getStats() API']")
    Legacy.click()
    print("Legacy Non-Standard (callback-based) getStats() API 선택했습니다.")
    
    # 현재 활성화 된 탭 확인
    print(driver.window_handles)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 새창 열기 및 새창으로 전환
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    
    # 현재 활성화 된 탭 확인
    print(driver.window_handles)
    print("새창 열기 및 새창으로 전환하였습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
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
    
    # 원격 협업 생성 버튼 존재 확인 > 원격 협업 생성 버튼 클릭
    try:
        remote_collaborator = driver.find_element(By.XPATH, "//button[@class='btn' and contains(text(), '원격 협업 생성')]")
        if remote_collaborator.is_displayed():
            print("원격 협업 생성 버튼이 존재합니다.")
        else:
            print("원격 협업 생성 버튼이 존재하지 않습니다.")
            
            # 원격 협업 생성 버튼 클릭
        remote_collaborator_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn' and contains(text(), '원격 협업 생성')]")))
        actions = ActionChains(driver)\
            .move_to_element(remote_collaborator_btn)\
            .click(remote_collaborator_btn)\
            .perform()
        print("원격 협업 생성 버튼을 클릭했습니다.")
    except NoSuchElementException:
        print("원격 협업 생성 버튼을 찾을 수 없습니다.")
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 출력 확인
    try:
        remote_collaborator_modal = driver.find_element(By.XPATH, 
            "//div[@class='modal createroom-modal']/div[@class='modal--inner']/div[@class='modal--header']/following-sibling::div[@class='modal--body']")
        if remote_collaborator_modal.is_displayed():
            print("원격 협업 모달창이 출력되었습니다.")
        else:
            print("원격 협업 생성 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("원격 협업 생성 버튼을 찾을 수 없습니다.")
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > 협업 프로필 이미지 등록 버튼 클릭
    profilebtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/button[@class='btn normal createroom-info_regist-image']")))
    actions = ActionChains(driver)\
        .move_to_element(profilebtn)\
        .click(profilebtn)\
        .perform()
    print("협업 프로필 등록 버튼을 클릭했습니다.")
    
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 열기창에서 등록할 프로필 이미지 업로드
    uploader = auto.WindowControl(searchDepth=2, Name='열기')
    time.sleep(2)
    uploader.EditControl(Name="파일 이름(N):").SendKeys('barnacle.jpg')
    uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
    
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 등록한 프로필 이미지가 정상적으로 업로드 되었는지 확인 절차
    # 1. 프로필 이미지 엘리먼트 가져오기
    profile_image = driver.find_element(
        By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/div[@class='profile-image group']/img[@class='profile-image__image']")
    
    # 2. 이미지가 업로드되어 있는지 확인
    if profile_image.get_attribute("src=data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEBLAEsAAD…jypP7v6r/AI1cooAp+VJ/d/Vf8aPKk/u/qv8AjVyigD//2Q==") != "":
        print("프로필 이미지가 업로드되었습니다.")
    else:
        print("프로필 이미지가 업로드되지 않았습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > 협업 이름 입력창 존재 확인
    try:
        remote_collaborator_name = driver.find_element(By.XPATH, 
                "//div[@class='createroom']/section[@class='createroom-info']/figure[1][@class='inputrow']/input[@type='text' and @class='inputrow-input input']")
        if remote_collaborator_name.is_displayed():
            print("협업 이름 입력창이 존재합니다.")
        else:
            print("협업 이름 입력창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("협업 이름 입력창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > default 협업 이름 지우기
    placeholder = driver.find_element(By.XPATH,
            "//div[@class='createroom']/section[@class='createroom-info']/figure[1][@class='inputrow']/input[@type='text' and @class='inputrow-input input']")
    placeholder.clear()
    print("협업 이름을 지웠습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > 협업 이름 새로 입력하기
    collaborator_name = driver.find_element(By.XPATH,
            "//div[@class='createroom']/section[@class='createroom-info']/figure[1][@class='inputrow']/input[@type='text' and @class='inputrow-input input']")
    actions = ActionChains(driver)\
        .send_keys_to_element(collaborator_name, 'XR 건설_3차_E2E 테스트')\
        .perform()
    print("협업 이름 : XR 건설_3차_E2E 테스트 입력되었습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > 협업 이름 새로 입력하기
    collaborator_explained = driver.find_element(By.XPATH, 
            "//div[@class='createroom']/section[@class='createroom-info']/figure[2][@class='inputrow']/textarea[@type='text' and @class='inputrow-input textarea']")
    actions = ActionChains(driver)\
        .send_keys_to_element(collaborator_explained, 'XR 건설_3차_E2E 테스트 원격 협업 룸입니다.')\
        .perform()
    print("협업 설명 : XR 건설_3차_E2E 테스트 원격 협업 룸입니다.")
    
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 원격 협업 생성하기 모달창 > 새로고침 존재 확인 > 새로고침 버튼 클릭
    try:
        remote_collaborator_refresh = driver.find_element(By.XPATH, "//div[@class='createroom-user__header']/button[@class='icon-button refresh']")
        if remote_collaborator_refresh.is_displayed():
            print("새로고침 버튼이 존재합니다.")
            # 새로 고침 버튼 클릭
            refresh_btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='createroom-user__header']/button[@class='icon-button refresh']")))
            actions = ActionChains(driver)\
                .move_to_element(refresh_btn)\
                .click(refresh_btn)\
                .perform()
            print("새로고침 버튼을 클릭했습니다.")
        else:
            print("새로고침 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("새로 고침 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
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
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # collapsible member 리스트 존재 확인
    try:
        collapsible_member = driver.find_element(By.XPATH, "//div[@class='createroom-user__body']/div[@class='vue-scrollbar__wrapper']")
        if collapsible_member.is_displayed():
            print("멤버 리스트가 존재합니다.")
        else:
            print("멤버 리스트가 존재하지 않습니다.")
    except NoSuchElementException:
        print("멤버 리스트를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 선택 가능한 멤버 리스트 > 멤버 클릭 > 멤버 해제 > 다시 멤버 선택
    user_option = [
        {
            "xpath" : "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice']",
            "message" : "user2를 선택했습니다.",
            "timeout" : 3
            },
        {
            "xpath" : "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice selected']",
            "message" : "user2 선택 취소했습니다.",
            "timeout" : 3
            },
        {
            "xpath": "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice']",
            "message": "user2를 다시 선택했습니다.",
            "timeout": 3
            }
        ]
    # 선택 가능한 멤버 리스트에서 user2 멤버 선택하기
    for user_xpath in user_option:
        user_select = WebDriverWait(driver, user_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, user_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(user_select)\
            .click(user_select)\
            .perform()
        print(user_xpath["message"])
    time.sleep(3)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 협업 생성하기 모달창 > 시작하기 버튼 존재 확인
    try:
        collaborator_modal_start = driver.find_element(By.XPATH, 
            "//div[@class='modal--inner']/div[2][@class='modal--body']/div[@class='createroom']/section[@class='createroom-info']/button[@class='btn large createroom-info__button' and contains(text(), '시작하기')]")
        if collaborator_modal_start.is_displayed():
            print("[시작하기] 버튼이 존재합니다.")
            
            # [시작하기] 버튼 클릭
            start_btn = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='modal--inner']/div[2][@class='modal--body']/div[@class='createroom']/section[@class='createroom-info']/button[@class='btn large createroom-info__button' and contains(text(), '시작하기')]")))
            actions = ActionChains(driver)\
                .move_to_element(start_btn)\
                .click(start_btn)\
                .perform()
            print("[시작하기] 버튼을 클릭했습니다.")
        else:
            print("[시작하기] 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("[시작하기] 버튼을 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 원격 협업 화면 존재 확인
    try: 
        remote_collaborator_display = driver.find_element(By.XPATH, "//section[@class='remote-layout']/div[@class='remote-wrapper service-wrapper']/main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='main-video']")
        if remote_collaborator_display.is_displayed():
            print("원격 협업 화면이 존재합니다.")
        else:
            print("원격 협업 화면이 존재하지 않습니다.")
    except NoSuchElementException:
        print("원격 협업 화면을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 존재 확인
    try:
        real_time_share = driver.find_element(By.XPATH, 
            "//nav[@class='header-lnbs service']/ul[@class='flex']/li[1][@class='header-lnb']/button[@class='header-lnb__button active']")
        if real_time_share.is_displayed():
            print("실시간 공유 탭이 존재합니다.")
        else:
            print("실시간 공유 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("실시간 공유 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 협업보드 탭 존재 확인
    try:
        collaborator_tab = driver.find_element(By.XPATH, 
            "//nav[@class='header-lnbs service']/ul[@class='flex']/li[2][@class='header-lnb']/button[@class='header-lnb__button']")
        if collaborator_tab.is_displayed():
            print("협업보드 탭이 존재합니다.")
        else:
            print("협업보드 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("협업보드 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # AR 공유 탭 존재 확인
    try:
        ar_share_tab = driver.find_element(By.XPATH, 
            "//nav[@class='header-lnbs service']/ul[@class='flex']/li[3][@class='header-lnb']/button[@class='header-lnb__button']")
        if ar_share_tab.is_displayed():
            print("AR 공유 탭이 존재합니다.")
        else:
            print("AR 공유 탭이 존재하지 않습니다.")
    except NoSuchElementException:
        print("AR 공유 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 원격 비디오 화면 출력 확인
    try:
        remote_video_display = driver.find_element(By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='main-video']/div[@class='main-video__box']")
        if remote_video_display.is_displayed():
            print("원격 비디오 화면이 존재합니다.")
        else:
            print("원격 비디오 화면이 존재하지 않습니다.")
    except NoSuchElementException:
        print("원격 비디오 화면을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 상단 가운데 stream tool 메뉴 존재 확인
    try:
        stream_tool = driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']")
        if stream_tool.is_displayed():
            print("stream tool 메뉴가 존재합니다.")
        else:
            print("stream tool 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("stream tool 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 버튼 존재 확인
    try:
        pointing_btn = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool disabled']")
        if pointing_btn.is_displayed():
            print("포인팅 버튼이 존재합니다.")
        else:
            print("포인팅 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("포인팅 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 버튼 존재 확인
    try:
        color_btn = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool']")
        if color_btn.is_displayed():
            print("색상 버튼이 존재합니다.")
        else:
            print("색상 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("색상 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 화면 공유 버튼 존재 확인
    try:
        display_share = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[4][@class='tooltip']")
        if display_share.is_displayed():
            print("화면 공유 버튼이 존재합니다.")
        else:
            print("화면 공유 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("화면 공유 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 화면 공유 버튼 > 공유창 : 해당 공유창은 chrome 자체적으로 지원되는 팝업창이라서 Windows Handle 제어가 안됨, 하여 수동 테스트 영역에서 동작 확인 필요함
    print("화면 공유 팝업창은 수동 테스트로 동작 확인 진행 해주세요.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box 존재 확인
    try:
        menu_box = driver.find_element(By.XPATH, 
        "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']")
        if menu_box.is_displayed():
            print("Menu Box가 존재합니다.")
        else:
            print("Menu Box가 존재하지 않습니다.")
    except NoSuchElementException:
        print("Menu box을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box > 화면 캡쳐 메뉴 존재 확인
    try:
        capture_menu = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[1][@class='tooltip tooltip-menu']/button[@class='menu']")
        if capture_menu.is_displayed():
            print("캡쳐 후 공유 메뉴가 존재합니다.")
        else:
            print("화면 캡쳐 후 공유 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("캡쳐 후 공유 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box > 서버 녹화 메뉴 존재 확인
    try:
        server_recording_menu = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[2][@class='tooltip tooltip-menu']/button[@class='menu']")
        if server_recording_menu.is_displayed():
            print("서버 녹화 메뉴가 존재합니다.")
        else:
            print("서버 녹화 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("서버 녹화 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box > 로컬 녹화 메뉴 존재 확인
    try:
        local_recording_menu = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[3][@class='tooltip tooltip-menu']/button[@class='menu']")
        if local_recording_menu.is_displayed():
            print("로컬 녹화 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box > 로컬 녹화 목록 메뉴 존재 확인
    try:
        local_recording_list = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[4][@class='tooltip tooltip-menu']/button[@class='menu']")
        if local_recording_list.is_displayed():
            print("로컬 녹화 목록 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 목록 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 목록 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 화면 상단 가운데 오른쪽 > Menu box > 설정 메뉴 존재 확인
    try:
        setting_menu = driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[5][@class='tooltip tooltip-menu']/button[@class='menu']")
        if setting_menu.is_displayed():
            print("설정 메뉴가 존재합니다.")
        else:
            print("설정 캡쳐 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("설정 메뉴을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 원격 비디오 화면 > Full screen button 존재 확인
    try:
        full_screen_btn = driver.find_element(By.XPATH, 
            "//div[@class='main-video']/div[@class='main-video__box']/div[@class='tooltip fullscreen-button']/button[@class='tool']")
        if full_screen_btn.is_displayed():
            print("Full screen 버튼이 존재합니다.")
        else:
            print("Full screen 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("Full screen 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > Leader 비디오 화면 존재 확인
    try:
        leader_video_display = driver.find_element(By.XPATH, "//div[@class='participants__view']/article[1]/div[@class='participant-video current']/div[@class='participant-video__stream']/video[@autoplay='autoplay']")
        if leader_video_display.is_displayed():
            print("Leader 비디오 화면이 존재합니다.")
        else:
            print("Leader 비디오 화면이 존재하지 않습니다.")
    except NoSuchElementException:
        print("Leader 비디오 화면을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 참가자 비디오 화면 > Leader 텍스트 출력 확인
    try:
        leader_text = driver.find_element(By.XPATH, 
            "//div[@class='participants__view']/article[1]/div[@class='participant-video current']/div[@class='participant-video__status']/span[@class='participant-video__leader' and contains(text(), 'Leader')]")
        if leader_text.is_displayed():
            print("참가자 비디오 화면에 Leader 텍스트가 존재합니다.")
        else:
            print("참가자 비디오 화면에 Leader 텍스트가 존재하지 않습니다.")
    except NoSuchElementException:
        print("참가자 비디오 화면에서 Leader 텍스트를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 참가자 비디오 화면 > 내 계정 출력 존재 확인
    try:
        my_account = driver.find_element(By.XPATH, 
            "//div[@class='participants__view']/article[1]/div[@class='participant-video current']/div[@class='participant-video__name mine']/div[@class='participant-video__name-text']")
        if my_account.is_displayed():
            print("내 계정이 존재합니다.")
        else:
            print("내 계정이 존재하지 않습니다.")
    except NoSuchElementException:
        print("내 계정을 찾을 수 없습니다.")
        
    # 3초동안 타임슬립
    time.sleep(3)
    
    # span 값에서 내 계정이 실제 출력되는지 확인 : 계정은 변수 값이라서 되도록 텍스트 속성으로 가져오는 것이 명확함
    span_element = driver.find_element(By.XPATH, "//div[@class='participants__view']/article[1]/div[@class='participant-video current']/div[@class='participant-video__name mine']/div[@class='participant-video__name-text']/span[contains(text(), '')]")
    
    # 실시간 공유 탭 > 참가자 비디오 화면 > 계정명 출력
    span_text = span_element.text
    print("계정명이" + span_text + "(으)로 출력됩니다.")
    
    # 내 계정에서 Me 출력 확인 여부 > 아래와 같은 이유로 출력 여부 확인 못함
    #  "::after"와 같은 의사요소는 실제 DOM 구조에는 존재하지 않으므로 Selenium을 사용하여 직접 가져올 수 없습니다. "::after"와 같은 의사요소는 브라우저가 CSS 스타일을 적용할 때 생성되는 가상의 요소입니다. 따라서 Selenium으로 이러한 가상 요소에 접근하는 것은 불가능합니다.

    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 참가자 비디오 추가 메뉴 존재 확인
    try:
        add_participant_video = driver.find_element(By.XPATH, 
            "//div[@class='participants__view']/article[2]/div[@class='participant-video append more']/p[contains(text(), '추가 초대하기')]")
        if add_participant_video.is_displayed():
            print("참가자 비디오 추가 메뉴가 존재합니다.")
        else:
            print("참가자 비디오 화면 추가 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("참가자 비디오 화면 추가 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 채팅 메뉴 존재 확인
    try:
        chatting_menu = driver.find_element(By.XPATH, "//div[@class='subview-wrapper']/div[@class='chat']/div[@class='chat-body']")
        if chatting_menu.is_displayed():
            print("채팅창이 존재합니다.")
        else:
            print("채팅창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("채팅창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 채팅 메뉴 > 채팅 탭 존재 확인
    try:
        chatting_tab = driver.find_element(By.XPATH, 
            "//div[@class='subview-wrapper']/div[@class='chat']/div[@class='chat-header']/ul[@class='chat-header__menu']/li[1][@class='chat-header__selector active']")
        if chatting_tab.is_displayed():
            print("채팅 메뉴에 채팅 탭이 존재합니다.")
        else:
            print("채팅 메뉴에서 채팅 탭이 존해하지 않습니다.")
    except NoSuchElementException:
        print("채팅 메뉴에서 채팅 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 채팅 메뉴 > 파일 탭 존재 확인
    try:
        file_tab = driver.find_element(By.XPATH, 
            "//div[@class='subview-wrapper']/div[@class='chat']/div[@class='chat-header']/ul[@class='chat-header__menu']/li[2][@class='chat-header__selector']")
        if file_tab.is_displayed():
            print("채팅 메뉴에 파일 탭이 존재합니다.")
        else:
            print("채팅 메뉴에서 파일 탭이 존해하지 않습니다.")
    except NoSuchElementException:
        print("채팅 메뉴에서 파일 탭을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > 채팅 메뉴 > 텍스트 입력 필드 존재 확인
    try:
        text_input = driver.find_element(By.XPATH, 
            "//div[@class='chat-body']/div[@class='chat-list']/div[2]/div[@class='chat-input']/div[@class='chat-input__form']")
        if text_input.is_displayed():
            print("채팅 메뉴에 텍스트 입력 필드가 존재합니다.")
        else:
            print("채팅 메뉴에 텍스트 입력 필드가 존재하지 않습니다.")
    except NoSuchElementException:
        print("채팅 메뉴에 텍스트 입력 필드를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 협업 탭 > 채팅 메뉴 > 파일 업로드 버튼 존재 확인
    try:
        file_upload = driver.find_element(By.XPATH, 
            "//div[@class='chat-body']/div[@class='chat-list']/div[2]/div[@class='chat-input']/div[@class='chat-input__form']/button[1][@class='chat-input__form-upload' and contains(text(), '파일 업로드')]")
        if file_upload.is_displayed():
            print("채팅 메뉴에 파일 업로드 버튼이 존재합니다.")
        else:
            print("채팅 메뉴에 파일 업로드 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("채팅 메뉴에서 파일 업로드 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 협업 탭 > 채팅 메뉴 > 보내기 버튼 존재 확인
    try:
        push_btn = driver.find_element(By.XPATH, 
            "//div[@class='chat-body']/div[@class='chat-list']/div[2]/div[@class='chat-input']/div[@class='chat-input__form']/button[2][@class='chat-input__form-button' and contains(text(), '보내기')]")
        if push_btn.is_displayed():
            print("채팅 메뉴에 보내기 버튼이 존재합니다.")
        else:
            print("채팅 메뉴에 보내기 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("채팅 메뉴에서 보내기 버튼을 찾을 수 없습니다.")
        
    ########## WebRTC 띄우기 > STG 홈 화면 > 로그인센터 로그인 > 원격협업 생성 > 실시간 공유 기본 메뉴 확인 완료 ##########
    print("Mobile에서 Remote application 구동 확인해주세요.")
    print("Remote Mobile application이 구동되어 원격 협업 참가하기 전까지 130초 대기합니다.")
    
    # 웹에서 원격 협업 요청 후, 수동으로 직접 Remote Mobile에서 로그인하고 원격 협업을 선택 할 수 있는 물리적인 시간이 필요함
    # 사유 1) 해당 time.sleep(175)초 전까지 실행되기 전까지 해당 파일 전 테스트 코드 실행 되기까지 웹 : 40초 ~ 45초 이내 소요됨
    # 사유 2) 모바일 앱은 3.remote_v2.7_app.py 파일의 테스트 코드가 실행되는 case는 2가지인데 먼저 최초 설치서부터 XR 건설_3차_E2E 테스트 원격 협업 참가하기까지는 1분 40초 소요
    # 사유 3) 사유 2번에서 case 두번째는 Remote 최초 설치 후, 다시 3.remote_v2.7_app.py 실행되어서 XR 건설_3차_E2E 테스트 원격 협업 참가하기까지 1분 38초 소요됨
    # 175초 타임 슬립
    time.sleep(130)
    
    # user2 모바일 협업 인원 더블 클릭하여 선택하기
    participantvideo2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class = 'participant-video']/div[@class = 'participant-video__stream']")))
    actions = ActionChains(driver)\
        .move_to_element(participantvideo2)\
        .double_click(participantvideo2)\
        .perform()
    print("user2 사용자를 선택하였습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 실시간 공유 탭 > [영상 보기] 및 [전체 공유] 모달창 존재 확인
    try:
        real_time_modal = driver.find_element(By.XPATH, "//div[@class='modal select-view']/div[@class='modal--inner']/div[@class='modal--body']")
        if real_time_modal.is_displayed():
            print("[영상 보기] 및 [전체 공유] 모달창이 존재합니다.")
            
            # 실시간 공유 탭 > [전체 공유] 탭 클릭
            share_all = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='modal select-view']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='select-view__layout']/div[@class='select-view__body']/figure[2]/button[@class='btn select-view__button share_view' and contains(text(), '전체 공유')]")))
            actions = ActionChains(driver)\
                .move_to_element(share_all)\
                .click(share_all)\
                .perform()
            print("전체 공유 버튼을 클릭했습니다.")
        else:
            print("[영상 보기] 및 [전체 공유] 모달창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("[영상 보기] 및 [전체 공유] 모달창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # user2 화면 출력 확인
    try:
        user2_video = driver.find_element(By.XPATH, "//div[@class='main-video']/div[@class='main-video__box']/video[@id='main-video' and @muted='muted' and @autoplay='autoplay']")
        if user2_video.is_displayed():
            print("user2 협업 참자가 화면이 전체 공유되었습니다.")
        else:
            print("user2 협업 참가자 화면이 전체 공유되지 못했습니다.")
    except NoSuchElementException:
        print("user2 협업 참가자 화면을 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 포인팅 버튼 요소 클릭 전 XPath
    pointing_button_xpath_before = "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool']"
    
    # 포인팅 버튼 클릭 전 상태 확인
    pointing_button_before = driver.find_element(By.XPATH, pointing_button_xpath_before)
    is_active_before = 'active' in pointing_button_before.get_attribute('class')
    
    # 상태 출력
    print("버튼 클릭 전 상태:", is_active_before)
    
    # 포인팅 버튼 클릭 > 포인팅 버튼 활성화
    try:
        pointing_ready = driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool']")
        if pointing_ready.is_displayed():
            print("포인팅 버튼을 클릭 할 수 있는 상태입니다.")
            
            # 포인팅 버튼 클릭
            pointing_btn1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool']")))
            actions = ActionChains(driver)\
                .move_to_element(pointing_btn1)\
                .click(pointing_btn1)\
                .perform()
            print("포인팅 버튼을 클릭했습니다.")
        else:
            print("포인팅 버튼을 클릭 할 수 없는 상태입니다.")
    except NoSuchElementException:
        print("포인팅 버튼을 찾을 수 없습니다.")
        
    # 3초동안 타임 슬립
    time.sleep(3)
    
    # 버튼 요소 클릭 후 XPath
    pointing_button_xpath_after = "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool active']"
    
    # 버튼 클릭 후 상태 확인
    pointing_button_after = driver.find_element(By.XPATH, pointing_button_xpath_after)
    is_active_after = 'active' in pointing_button_after.get_attribute('class')
    
    # 상태 출력
    print("버튼 클릭 후 상태:", is_active_after)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 버튼 클릭 > 색상 버튼 활성화
    try:
        color_ready = driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool']")
        if color_ready.is_displayed():
            print("색상 버튼을 클릭 할 수 있는 상태입니다.")
            
            # 색상 버튼 클릭
            color_btn1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((
                By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool']")))
            actions = ActionChains(driver)\
                .move_to_element(color_btn1)\
                .click(color_btn1)\
                .perform()
            print("색상 버튼을 클릭했습니다.")
        else:
            print("색상 버튼을 클릭 할 수 없는 상태입니다.")
    except NoSuchElementException:
        print("색상 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 버튼 모달창 존재 확인
    try:
        picker_color = driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']")
        if picker_color.is_displayed():
            print("색상 선택 모달창이 존재합니다.")
        else:
            print("색상 선택 모달창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("색상 선택 모달창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 12종 순차적으로 클릭하기
    color_option = [
        ('#ff843e', '주황색(#ff843e)을 선택하였습니다.'),
        ('#fecc42', '밝은 황색(#fecc42)을 선택하였습니다.'),
        ('ffff53', '노란색(#ffff53)을 선택하였습니다.'),
        ('#b8ff54', '연두색(#b8ff54)을 선택하였습니다.'),
        ('#40fc77', '라임색(#40fc77)을 선택하였습니다.'),
        ('#3fe1ff', '하늘색(#3fe1ff)을 선택하였습니다.'),
        ('#2ea4ff', '스카이 블루(#2ea4ff)을 선택하였습니다.'),
        ('#ff6fe7', '분홍색(#ff6fe7)을 선택하였습니다.'),
        ('#d75fff', '밝은 보라색(#d75fff)을 선택하였습니다.'),
        ('#9a5fff', '진한 보라색(#9a5fff)을 선택하였습니다.'),
        ('#fcfcfc', '밝은 회색(#fcfcfc)을 선택하였습니다.'),
        ('#ff4141', '붉은색(#FF4141)을 선택하였습니다.'),
        ]
    for color_click, color_message in color_option:
        color_click_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[@class='picker--item']/button[@data-v-b85caa5a and contains(text(), '{color_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(color_click_btn)\
            .click(color_click_btn)\
            .perform()
        print(color_message)
        time.sleep(3)
        
    # 색상 버튼 클릭 > 색상 파레트 닫기
    color_btn1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, 
        "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(color_btn1)\
        .click(color_btn1)\
        .perform()
    print("색상 파레트를 닫았습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 버튼 > 색상 선택(파레트) > 색상 12가지 선택하여 포인팅 동작으로 동작 코드를 반복문 조합이 복잡하고 구현이 쉽지 않아서 class로 분리하여 구현함
    # 색상 선택하여 색상 순서대로 순차적으로 임의의 좌표 포인팅
    # ColorPallet 인스턴스 생성 : 색상 파레트 선택해서 포인팅 관련
    color_pallet = ColorPallet(driver)
    
    # 색상 선택하여 포인팅하기
    # 주황색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 주황색(#ff843e)을 선택
        color_pallet.click_color_2()
        print("주황색(#ff843e)을 선택했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("주황색 포인팅합니다.")
    except:
        print("주황색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 밝은 황색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 밝은 황색(#fecc42)을 선택
        color_pallet.click_color_3()
        print("밝은 황색(#fecc42)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("밝은 황색 포인팅합니다.")
    except:
        print("밝은 황색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 노란색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 노란색(#ffff53)을 선택
        color_pallet.click_color_4()
        print("노란색(#ffff53)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("노란색 포인팅합니다.")
    except:
        print("노란색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 연두색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 연두색(#b8ff54)을 선택
        color_pallet.click_color_5()
        print("연두색(#b8ff54)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("연두색 포인팅합니다.")
    except:
        print("연두색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 라임색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 라임색(#40fc77)을 선택
        color_pallet.click_color_6()
        print("라임색(#40fc77)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("라임색 포인팅합니다.")
    except:
        print("라임색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)        
        
    # 하늘색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 하늘색(#3fe1ff)을 선택
        color_pallet.click_color_7()
        print("하늘색(#3fe1ff)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("하늘색 포인팅합니다.")
    except:
        print("하늘색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)        
        
    # 스카이 블루색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 스카이 블루(#2ea4ff)을 선택
        color_pallet.click_color_8()
        print("스카이 블루(#2ea4ff)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("스카이 블루색 포인팅합니다.")
    except:
        print("스카이 블루색 포인팅 동작을 할 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)        
        
    # 분홍색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 분홍색(#ff6fe7)을 선택
        color_pallet.click_color_9()
        print("분홍색(#ff6fe7)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("분홍색 포인팅합니다.")
    except:
        print("분홍색 포인팅 동작을 할 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 밝은 보라색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 밝은 보라색(#d75fff)을 선택
        color_pallet.click_color_10()
        print("밝은 보라색(#d75fff)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("밝은 보라색 포인팅합니다.")
    except:
        print("밝은 보라색 포인팅 동작을 할 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 진한 보라색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 진한 보라색(#9a5fff)을 선택
        color_pallet.click_color_11()
        print("진한 보라색(#9a5fff)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("진한 보라색 포인팅합니다.")
    except:
        print("진한 보라색 포인팅 동작을 할 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 밝은 회색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 밝은 회색(#fcfcfc)을 선택
        color_pallet.click_color_12()
        print("밝은 회색(#fcfcfc)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")        
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("밝은 회색 포인팅합니다.")
    except:
        print("밝은 회색 포인팅 동작을 할 수 없습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 붉은색 선택하여 참가자 화면 포인팅
    try:
        # 색상 버튼 클릭
        color_pallet.click_color_button()
        print("색상 버튼을 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 색상 파레트 선택 > 붉은색(#FF4141)을 선택
        color_pallet.click_color_1()
        print("붉은색(#FF4141)을 선택하였습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 색상 버튼 클릭
        color_pallet.click_color_active()
        print("색상 선택 파레트를 닫았습니다.")
        
        # 참가자 화면에 포인팅
        color_pallet.perform_pointing_actions()
        print("붉은색 포인팅합니다.")
    except:
        print("붉은색 포인팅 동작을 할 수 없습니다.")
    
    #3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 버튼 클릭 비활성하기
    pointing_btn1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-tools tools']/div[1][@class='tooltip']/button[@class='tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_btn1)\
        .click(pointing_btn1)\
        .perform()
    print("포인팅 버튼을 비활성화했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 참가자 화면을 확대 / 축소
    participant_screen_move = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='main-video']/div[@class='main-video__box']/div[4][@class='tooltip fullscreen-button']")))
    # 클릭 횟수를 저장하는 변수 초기화
    click_count = 0
    for i in range(2):
        actions = ActionChains(driver)\
            .move_to_element(participant_screen_move)\
            .click(participant_screen_move)\
            .perform()
        time.sleep(3)
        
        # 클릭 횟수에 따라 출력 메시지 결정
        click_count += 1
        if click_count == 1:
            print("참가자 화면을 확대하였습니다.")
        elif click_count == 2:
            print("참가자 화면을 축소하였습니다.")
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
        # 캡처 후 공유 버튼 클릭 > 영상 캡처 화면 확인
    capture_menu_btn = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[1][@class='tooltip tooltip-menu']/button[@class='menu']")
    actions = ActionChains(driver)\
        .move_to_element(capture_menu_btn)\
        .click(capture_menu_btn)\
        .perform()
    print("캡처 후 공유 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    
    # 영상 캡처 화면 존재하는지 확인 > 다시 찍기 선택 > 이미지 저장 선택
    try:
        try: 
            display_capture = driver.find_element(By.XPATH, 
            "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-header']/p[@class='capture-header__title' and contains(text(), '영상이 캡처되었습니다.')]")
            if display_capture.is_displayed():
                print("영상 캡처 화면이 존재합니다.")
            else:
                print("영상 캡처 화면이 존재하지 않습니다.")
        except NoSuchElementException:
            print("영상 캡처 화면을 찾을 수 없습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
            
        # 영상 캡처 화면 닫기 버튼 존재 확인
        try: 
            display_capture_close = driver.find_element(By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-header']/button[@class='capture-header__close']")
            if display_capture_close.is_displayed():
                print("영상 캡처 화면 닫기 버튼이 존재합니다.")
            else:
                print("영상 캡처 화면 닫기 버튼이 존재하지 않습니다.")
        except NoSuchElementException:
            print("영상 캡처 화면 닫기 버튼을 찾을 수 없습니다.")
            
            # 3초동안 암묵적 대기
            driver.implicitly_wait(time_to_wait=3)
            
        # 다시 찍기 버튼 존재 확인
        try:
            capture_retake = driver.find_element(By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-body']/div[@class='capture-tools']/button[1][@class='capture-tools_button']")
            if capture_retake.is_displayed():
                print("다시 찍기 버튼이 존재합니다.")
            else:
                print("다시 찍기 버튼이 존재하지 않습니다.")
        except NoSuchElementException:
            print("다시 찍기 버튼을 찾을 수 없습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 이미지 저장 버튼 존재 확인
        try:
            image_save = driver.find_element(By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-body']/div[@class='capture-tools']/button[2][@class='capture-tools_button']")
            if image_save.is_displayed():
                print("이미지 저장 버튼이 존재합니다.")
            else:
                print("이미지 저장 버튼이 존재하지 않습니다.")
        except NoSuchElementException:
            print("이미지 저장 버튼을 찾을 수 없습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 캡처 이미지 공유 버튼 존재 확인
        try:
            capture_image_share = driver.find_element(By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-body']/button[@class='capture-share']")
            if capture_image_share.is_displayed():
                print("캡처 이미지 공유 버튼이 존재합니다.")
            else:
                print("캡처 이미지 공유 버튼이 존재하지 않습니다.")
        except NoSuchElementException:
            print("캡처 이미지 공유 버튼을 찾을 수 없습니다.")
            
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 다시 찍기 5번 클릭
        capture_retake_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-body']/div[@class='capture-tools']/button[1][@class='capture-tools_button']")))
        for i in range(1, 6):
            actions = ActionChains(driver)\
                .move_to_element(capture_retake_btn)\
                .click(capture_retake_btn)\
                .perform()
            print(f"다시 찍기를 {i}회 실시하였습니다.")
            time.sleep(3)
            
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 이미지 저장 5번 클릭
        image_save_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-body']/div[@class='capture-tools']/button[2][@class='capture-tools_button']")))
        for i in range(1, 6):
            actions = ActionChains(driver)\
                .move_to_element(image_save_btn)\
                .click(image_save_btn)\
                .perform()
            print(f"이미지 저장을 {i}회 실시하였습니다.")
            time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 영상 캡처 화면 닫기
        capture_close_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//main[@class='main-wrapper']/div[@class='capture']/div[@class='capture-header']/button[@class='capture-header__close']")))
        actions = ActionChains(driver)\
            .move_to_element(capture_close_btn)\
            .click(capture_close_btn)\
            .perform()
        print("영상 캡처 화면을 닫았습니다.")
        time.sleep(3)
    except NoSuchElementException:
        print("영상 캡처 동작 시나리오를 정상적으로 실행하지 못했습니다.")
        
    # 영상 캡처 화면 닫기 버튼 동작은 협업 보드 탭 상호 관계가 있는 기능이라서 해당 동작은 협업 보드 탭에서 구현되어 있음
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 서버 녹화 메뉴 클릭 : 60초 서버 녹화 동작이지만 서버 녹화 클릭 후, 서버 녹화 시작 후, 서버 녹화 종료 되기까지 4초 오차 발생되어 4초 보상
    server_recording_option = [
        {
            "xpath": "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[2][@class='tooltip tooltip-menu']/button[@class='menu']",
            "timeout": 5,
            "message": "{server_start}차 서버 녹화를 시작합니다.",
            "start_recording": True
            },
        {
            "xpath": "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[2][@class='tooltip tooltip-menu']/button[@class='menu active']",
            "timeout": 5,
            "message": "{server_start}차 서버 녹화를 종료합니다.",
            "start_recording": False
            }
        ]
    server_repeat_count = range(1, 4) # range() 함수로 서버 녹화 횟수 지정
    for server_start in server_repeat_count:
        for server_xpath in server_recording_option:
            server_recording_btn = WebDriverWait(driver, server_xpath["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, server_xpath["xpath"])))
            actions = ActionChains(driver)\
                .move_to_element(server_recording_btn)\
                .click(server_recording_btn)\
                .perform()
            print(server_xpath["message"].format(server_start=server_start))
            
            # 63초 후 서버 녹화 종료
            if server_xpath["start_recording"]:
                time.sleep(64)
                
                # 녹화 시간 출력 여부
                recording_time_check_1 = driver.find_element(By.XPATH, 
                "//div[@class='main-video']/div[@class='main-video__box']/div[@class='main-video__recording']/div[@class='main-video__recording--time sharing-on']/p[@class='server']")
                if recording_time_check_1.is_displayed():
                    print(f"{server_start}차 서버 녹화 시간이 출력되었습니다.")
                else:
                    print(f"{server_start}차 서버 녹화 시간이 출력되지 않았습니다.")
                    
                # 실제 녹화 시간 체크 
                recording_time_1 = recording_time_check_1.text
                print(f"{server_start}차 녹화 시간 출력 결과:", recording_time_1)
            elif not server_xpath["start_recording"]:
                pass
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 메뉴 클릭 : 60초 로컬 녹화 동작이지만 로컬 녹화 클릭 후, 약 4초 뒤에 로컬 녹화 시작되어 4초 오차 시간 보상
    local_recording_option = [
        {
            "xpath": "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[3][@class='tooltip tooltip-menu']/button[@class='menu']",
            "timeout": 5,
            "message": "{local_start}차 로컬 녹화를 시작합니다.",
            "start_recording": True
            },
        {
            "xpath": "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[3][@class='tooltip tooltip-menu']/button[@class='menu active']",
            "timeout": 5,
            "message": "{local_start}차 로컬 녹화를 종료합니다.",
            "start_recording": False
            }
        ]
    local_repeat_count = range(1, 4) # range() 함수로 로컬 녹화 횟수 지정
    for local_start in local_repeat_count:
        for local_xpath in local_recording_option:
            local_recording_btn = WebDriverWait(driver, local_xpath["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, local_xpath["xpath"])))
            actions = ActionChains(driver)\
                .move_to_element(local_recording_btn)\
                .click(local_recording_btn)\
                .perform()
            print(local_xpath["message"].format(local_start=local_start))  # 플레이스홀더를 실제 값으로 대체
            
            # 63초 후 서버 녹화 종료
            if local_xpath["start_recording"]:
                time.sleep(60)
                
                # 녹화 시간 출력 여부
                recording_time_check_2 = driver.find_element(By.XPATH, 
                "//div[@class='main-video']/div[@class='main-video__box']/div[@class='main-video__recording']/div[@class='main-video__recording--time']/p[@class='local']")
                if recording_time_check_2.is_displayed():
                    print(f"{local_start}차 서버 녹화 시간이 출력되었습니다.")
                else:
                    print(f"{local_start}차서버 녹화 시간이 출력되지 않았습니다.")
                    
                # 실제 녹화 시간 체크
                recording_time_2 = recording_time_check_2.text
                print(f"{local_start}차 녹화 시간 출력 결과:", recording_time_2)
            elif not local_xpath["start_recording"]:
                pass
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 목록 버튼 클릭
    local_recording_menu_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, 
        "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[4][@class='tooltip tooltip-menu']/button[@class='menu']")))
    actions = ActionChains(driver)\
        .move_to_element(local_recording_menu_btn)\
        .click(local_recording_menu_btn)\
        .perform()
    print("로컬 녹화 목록 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 확인
    try:
        local_recording_modal = driver.find_element(By.XPATH, "//div[@class='modal record-list-modal']/div[@class='modal--inner']/div[@class='modal--header']/p[@class='modal--title' and contains(text(), '로컬 녹화 파일')]")
        if local_recording_modal.is_displayed():
            print("로컬 녹화 파일 모달창이 존재합니다.")
        else:
            print("로컬 녹화 파일 모달창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 파일 모달창을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 닫기 버튼 확인
    try:
        local_recording_close = driver.find_element(By.XPATH, "//div[@class='modal record-list-modal']/div[@class='modal--inner']/div[@class='modal--header']/button[@class='modal--close']")
        if local_recording_close.is_displayed():
            print("로컬 녹화 파일 모달창에 닫기 버튼이 존재합니다.")
        else:
            print("로컬 녹화 파일 모달창에 닫기 버튼이 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 파일 모달창에 닫기 버튼을 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 전체 다운로드 라디오 체크 메뉴 확인
    try:
        local_recording_all_check = driver.find_element(By.XPATH, 
            "//div[@class='record-list']/div[@class='record-list__table']/div[@class='table']/div[@class='table__column']/div[@class='table__column--toggle']/button[@class='toggle-button']")
        if local_recording_all_check.is_displayed():
            print("전체 다운로드 라디오 체크 메뉴가 존재합니다.")
        else:
            print("전체 다운로드 라디오 체크 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("전체 다운로드 라디오 체크 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 > 선택 다운로드 메뉴 확인
    try: 
        select_download = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[1][@class='icon-button custom-local-record']/span[contains(text(), '선택 다운로드')]")
        if select_download.is_displayed():
            print("선택 다운로드 메뉴가 존재합니다.")
        else:
            print("선택 다운로드 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("선택 다운로드 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 > 선택 삭제 메뉴 확인
    try: 
        select_download = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[2][@class='icon-button custom-local-record']/span[contains(text(), '선택 삭제')]")
        if select_download.is_displayed():
            print("선택 삭제 메뉴가 존재합니다.")
        else:
            print("선택 삭제 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("선택 삭제 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 출력 확인
    try:
        local_recording_list = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__body']")
        if local_recording_list.is_displayed():
            print("로컬 녹화 파일 리스트가 존재합니다.")
        else:
            print("로컬 녹화 파일 리스트가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 파일 리스트를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 전체 다운로드 라디오 체크 메뉴 확인
    try:
        local_recording_all_check = driver.find_element(By.XPATH, 
            "//div[@class='record-list']/div[@class='record-list__table']/div[@class='table']/div[@class='table__column']/div[@class='table__column--toggle']/button[@class='toggle-button']")
        if local_recording_all_check.is_displayed():
            print("전체 다운로드 라디오 체크 메뉴가 존재합니다.")
        else:
            print("전체 다운로드 라디오 체크 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("전체 다운로드 라디오 체크 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 > 선택 다운로드 메뉴 확인
    try: 
        select_download = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[1][@class='icon-button custom-local-record']")
        if select_download.is_displayed():
            print("선택 다운로드 메뉴가 존재합니다.")
        else:
            print("선택 다운로드 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("선택 다운로드 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 > 선택 삭제 메뉴 확인
    try: 
        select_download = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[2][@class='icon-button custom-local-record']")
        if select_download.is_displayed():
            print("선택 삭제 메뉴가 존재합니다.")
        else:
            print("선택 삭제 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("선택 삭제 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 로컬 녹화 파일 리스트 출력 확인
    try:
        local_recording_list = driver.find_element(By.XPATH, 
            "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__body']")
        if local_recording_list.is_displayed():
            print("로컬 녹화 파일 리스트가 존재합니다.")
        else:
            print("로컬 녹화 파일 리스트가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 파일 리스트를 찾을 수 없습니다.")
        
    # 5초 타임 슬립
    time.sleep(5)
    
    # 로컬 녹화 파일 리스트 스크롤
    local_recording_scroll = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='record-list']/div[@class='record-list__table']/div[@class='table']/div[@class='table__body']/div[@class='vue-scrollbar__wrapper']")))
    
    # 녹화된 로컬 녹화 파일 리스트 아래로 이동하기
    # 스크롤 아래로 이동
    driver.execute_script(
        "arguments[1].scrollTop += arguments[1].offsetHeight;", local_recording_scroll, local_recording_scroll)
    
    # 5초 타임 슬립
    time.sleep(5)
    
    # 녹화된 로컬 녹화 피일 리스트 위로 이동하기
    # 스크롤 위로 이동
    driver.execute_script(
        "arguments[0].scrollTop -= arguments[1].offsetHeight;", local_recording_scroll, local_recording_scroll)
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 전체 다운로드 라디오 체크 메뉴 클릭 > 1분 녹화 파일들 각각 선택 > 선택 다운로드 > 1초 녹화 파일 각각 선택 > 1초 녹화 파일들 선택 다운로드
    recording_modal_option = [
        {
            "xpath" : "//div[@class='record-list']/div[@class='record-list__table']/div[@class='table']/div[@class='table__column']/div[@class='table__column--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "전체 다운로드 라디오 체크 메뉴를 체크했습니다.",
            },
        {
            "xpath" : "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[1][@class='icon-button highlight custom-local-record']",
            "timeout" : 5,
            "message" : "선택 다운로드 메뉴를 클릭했습니다."
            },
        {
            "xpath" : "//div[@class='record-list']/div[@class='record-list__table']/div[@class='table']/div[@class='table__column']/div[@class='table__column--toggle']/button[@class='toggle-button active']",
            "timeout" : 3,
            "message" : "전체 다운로드 라디오 체크 메뉴를 체크 해제했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[2][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "첫번째 1분 녹화 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[4][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "두번째 1분 녹화 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[6][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "세번째 1분 녹화 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[1][@class='icon-button highlight custom-local-record']",
            "timeout" : 5,
            "message" : "1분짜리 녹화 파일 3개를 선택 다운로드했습니다."
            },
        {
            "xpath" : "//div[@class='modal record-list-modal']/div[@class='modal--inner']/div[@class='modal--header']/button[@class='modal--close']",
            "timeout" : 5,
            "message" : "로컬 녹화 파일 모달창을 닫았습니다."
            }
        ]
    for recording_modal_xpath in recording_modal_option:
        local_recording_all_click = WebDriverWait(driver, recording_modal_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, recording_modal_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(local_recording_all_click)\
            .click(local_recording_all_click)\
            .perform()
        print(recording_modal_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 로컬 녹화 파일 모달창 > 1분 녹화 파일들 각각 선택 > 선택 삭제
    menubox_option = [
        {
            "xpath" : "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[4][@class='tooltip tooltip-menu']/button[@class='menu']",
            "timeout" : 5,
            "message" : "로컬 녹화 목록 메뉴를 클릭했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[1][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "첫번째 0초 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[3][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "두번째 0초 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='vue-scrollbar__wrapper']/div[@class='vue-scrollbar__area vue-scrollbar-transition']/div[@class='scroll--inner']/div[5][@class='table__row']/div[@class='table__cell--toggle']/button[@class='toggle-button']",
            "timeout" : 5,
            "message" : "세번째 0초 파일을 선택했습니다."
            },
        {
            "xpath" : "//div[@class='modal--body']/div[@class='record-list']/div[@class='record-list__table']/div[@class='table' and @showtools='true']/div[@class='table__header']/div[@class='table__tools']/button[2][@class='icon-button highlight custom-local-record']",
            "timeout" : 5,
            "message" : "선택 삭제 메뉴를 선택했습니다."
            },
        {
            "xpath" : "//div[@class='modal record-list-modal']/div[@class='modal--inner']/div[@class='modal--header']/button[@class='modal--close']",
            "timeout" : 5,
            "message" : "로컬 녹화 파일 모달창을 닫았습니다."
            }
        ]
    for menubox_xpath in menubox_option:
        menubox_setting = WebDriverWait(driver, menubox_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, menubox_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(menubox_setting)\
            .click(menubox_setting)\
            .perform()
        print(menubox_xpath["message"])
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 설정 메뉴 클릭
    menubox_setting = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='stream-menu menus']/div[@class='menus-box']/div[5][@class='tooltip tooltip-menu']/button[@class='menu']")))
    actions = ActionChains(driver)\
        .move_to_element(menubox_setting)\
        .click(menubox_setting)\
        .perform()
    print("설정 메뉴를 클릭했습니다.")
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # # 설정 메뉴 클릭 > 환경 설정 모달창 출력
    try:
        preferences = driver.find_element(By.XPATH, "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--header']/p[@class='modal--title' and contains(text(), '환경 설정')]")
        if preferences.is_displayed():
            print("환경설정 모달창이 존재합니다.")
        else:
            print("환경설정 모달창이 존재하지 않습니다.")
    except NoSuchElementException:
        print("환경설정 모달창을 찾을 수 없습니다.")
        
    # # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # # 환경 설정 > 포인팅 설정 메뉴 출력
    try:
        pointing_set_menu = driver.find_element(By.XPATH, 
            "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting-nav']/button[@data-text='포인팅 설정' and @class='service-setting-nav__menu active']")
        if pointing_set_menu.is_displayed():
            print("포인팅 설정 메뉴가 존재합니다.")
        else:
            print("포인팅 설정 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("포인팅 설정 메뉴를 찾을 수 없습니다.")
        
    # # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # # 환경 설정 > 포인팅 설정 메뉴 > 참가자 포인팅 메뉴 출력
    try:
        participant_pointing = driver.find_element(By.XPATH, 
            "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting__view']/div[@class='service-setting__row']/p[@class='service-setting__text' and contains(text(), '참가자 포인팅')]")
        if participant_pointing.is_displayed():
            print("참가자 포인팅 메뉴가 존재합니다.")
        else:
            print("참가자 포인팅 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("참가자 포인팅 메뉴를 찾을 수 없습니다.")
        
    # # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # # 환경 설정 > 포인팅 설정 메뉴 > 포인팅 허용 메뉴 확인
    try:
        allow_pointing = driver.find_element(By.XPATH, 
            "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting__view']/div[@class='service-setting__row']/div[@class='checkbox toggle']/span[@class='checkbox-text' and contains(text(), '참가자 포인팅 허용')]")
        if allow_pointing.is_displayed():
            print("참가자 포인팅 허용 메뉴가 존재합니다.")
        else:
            print("참가자 포인팅 허용 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("참가자 포인팅 허용 메뉴를 찾을 수 없습니다.")
        
    # # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 메뉴 > 포인팅 메뉴
    allow_pointing_option = [
        {
            "xpath" : "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting__view']/div[@class='service-setting__row']/div[@class='checkbox toggle']/span[@class='checkbox-toggle toggle' and contains(text(), 'ON')]",
            "timeout" : 5,
            "message": "참가자 포인팅 허용 체크를 해제했습니다.",
            "pointing_check" : True
            },
        {
            "xpath" : "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting__view']/div[@class='service-setting__row']/div[@class='checkbox']/span[@class='checkbox-toggle' and contains(text(), 'OFF')]",
            "timeout" : 5,
            "message": "참가자 포인팅 허용을 다시 체크했습니다.",
            "pointing_check" : False
            }
        ]
    # 환경 설정 > 포인팅 설정 메뉴 > 포인팅 허용 체크 해제 > 다시 포인팅 허용 체크
    allow_pointing_count = range(1, 2)
    for i in allow_pointing_count:
        for allow_pointing_xpath in allow_pointing_option:
            allow_pointing_check = WebDriverWait(driver, allow_pointing_xpath["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, allow_pointing_xpath["xpath"])))
            actions = ActionChains(driver)\
                .move_to_element(allow_pointing_check)\
                .click(allow_pointing_check)\
                .perform()
            print(allow_pointing_xpath["message"])
            
            # pointing ON 일 때
            if allow_pointing_xpath["pointing_check"]:
                time.sleep(3)
            # pointing OFF 일 때
            elif not allow_pointing_xpath["pointing_check"]:
                pass
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 출력
    try:
        local_recording_menu = driver.find_element(By.XPATH, 
            "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting-nav']/button[@data-text='로컬 녹화 설정' and @class='service-setting-nav__menu']")
        if local_recording_menu.is_displayed():
            print("로컬 녹화 설정 메뉴가 존재합니다.")
            
            # 로컬 녹화 설정 메뉴 클릭
            local_recording_set = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, 
                    "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting-nav']/button[@data-text='로컬 녹화 설정' and @class='service-setting-nav__menu']")))
            actions = ActionChains(driver)\
                .move_to_element(local_recording_set)\
                .click(local_recording_set)\
                .perform()
            print("로컬 녹화 설정 메뉴를 클릭했습니다.")
        else:
            print("로컬 녹화 설정 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 설정 메뉴를 찾을 수 업습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)



#######=============================================================

    # 환경 설정 > 로컬 녹화 설정 메뉴 > 녹화 대상 메뉴 존재 확인
    try:
        recording_target_menu = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[1][@class='service-setting__row']/p[@class='service-setting__text' and contains(text(), '녹화대상')]")
        if recording_target_menu.is_displayed():
            print("녹화 대상 메뉴가 존재합니다.")
        else:
            print("녹화 대상 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("녹화 대상 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 녹화 대상 메뉴 > 영상 녹화 or 화면 녹화 선택
    recording_screen_option = [
        {
            "xpath" : "//div[@class='service-setting__selector']/div[@class='radio-group']/label[@class='radio-option']/span[@class='radio-option__input']/input[@type='radio' and @value='SCREEN']",
            "timeout" : 5,
            "message" : "화면 녹화를 선택했습니다."
            },
        {
            "xpath" : "//div[@class='service-setting__selector']/div[@class='radio-group']/label[@class='radio-option']/span[@class='radio-option__input']/input[@type='radio' and @value='WORKER']",
            "timeout" : 5,
            "message" : "영상 녹화를 선택했습니다."
            }
        ]
    recording_target_count = range(1, 2)
    for i in recording_target_count:
        for recording_target_xpath in recording_screen_option:
                recording_target = WebDriverWait(driver, recording_target_xpath["timeout"]).until(
                    EC.presence_of_element_located((By.XPATH, recording_target_xpath["xpath"])))
                actions = ActionChains(driver)\
                    .move_to_element(recording_target)\
                    .click(recording_target)\
                    .perform()
                print(recording_target_xpath["message"])
                time.sleep(3)
                
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 최대 녹화 시간 메뉴 존재 확인
    try:
        maximum_recording_time = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[2][@class='service-setting__row']/p[@class='service-setting__text' and contains(text(), '최대 녹화 시간')]")
        if maximum_recording_time.is_displayed():
            print("로컬 녹화 : 최대 녹화 시간 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 최대 녹화 시간 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("최대 녹화 시간 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 클릭 > 최대 녹화 시간 메뉴 옵션 박스 출력 확인
    maximum_recording_time_option = [
        {
            "xpath" : "//section[@class='service-setting__view']/div[2][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 최대 녹화 시간 메뉴를 클릭했습니다.",
            "maximum_start" : True
            },
        {
            "xpath" : "//section[@class='service-setting__view']/div[2][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 최대 녹화 시간 메뉴를 닫았습니다.",
            "maximum_end" : False
            }
        ]
    for maximum_recording_xpath in maximum_recording_time_option:
        maximum_recording_btn = WebDriverWait(driver, maximum_recording_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, maximum_recording_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_btn)\
            .click(maximum_recording_btn)\
            .perform()
        print(maximum_recording_xpath["message"])
        
        if "maximum_start" in maximum_recording_xpath:
            time.sleep(3)
            
            # 최대 녹화 시간 메뉴 옵션 박스 출력 확인
            try:
                maximum_recording_box = driver.find_element(By.XPATH, 
                    "//div[@class='modal service-setting-modal']/div[3][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if maximum_recording_box.is_displayed():
                    print("로컬 녹화 : 최대 시간 녹화 시간 메뉴 옵션 박스가 존재합니다.")
                else:
                    print("로컬 녹화 : 최대 녹화 시간 메뉴 옵션 박스가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 : 최대 녹화 시간 메뉴 옵션 박스를 찾을 수 없습니다.")
                
        elif "maximum_end" in maximum_recording_xpath:
            # time.sleep(3)
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 최대 녹화 시간 메뉴 클릭 > 최대 녹화 시간 클릭 : 1분 > 5분 > 10분 > 15분 > 30분 > 45분 > 60분 > 90분 > 120분 > Default 60분 순차적 클릭
    maximum_recording_option = [
        ('1 분', '로컬 녹화 : 1분을 선택하였습니다.'),
        ('5 분', '로컬 녹화 : 5분을 선택하였습니다.'),
        ('10 분', '로컬 녹화 : 10분을 선택하였습니다.'),
        ('15 분', '로컬 녹화 : 15분을 선택하였습니다.'),
        ('30 분', '로컬 녹화 : 30분을 선택하였습니다.'),
        ('45 분', '로컬 녹화 : 45분을 선택하였습니다.'),
        ('60 분', '로컬 녹화 : 60분을 선택하였습니다.'),
        ('90 분', '로컬 녹화 : 90분을 선택하였습니다.'),
        ('120 분', '로컬 녹화 : 120분을 선택하였습니다.'),
        ('60 분', '로컬 녹화 : 60분을 선택하였습니다.')
        ]
    for interval_click,  interval_message in maximum_recording_option:
        maximum_recording_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='service-setting__view']/div[2][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_btn)\
            .click(maximum_recording_btn)\
            .perform()
        print("로컬 녹화 : 최대 녹화 시간 메뉴를 클릭했습니다.")
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 로컬 녹화 : 최대 녹화 시간 순차적 클릭
        maximum_recording_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='modal service-setting-modal']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{interval_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(maximum_recording_click)\
            .click(maximum_recording_click)\
            .perform()
        print(interval_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 최대 녹화 간격 메뉴 존재 확인
    try:
        maximum_recording_interval = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[3][@class='service-setting__row']/div[@class='service-setting__text custom']/p[contains(text(), '최대 녹화 간격')]")
        if maximum_recording_interval.is_displayed():
            print("로컬 녹화 : 최대 녹화 간격 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 최대 녹화 간격 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 : 최대 녹화 간격 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 > 최대 녹화 간격 클릭 > 최대 녹화 간격 메뉴 옵션 박스 출력 확인
    recording_interval_time = [
        {
            "xpath" : "//section[@class='service-setting__view']/div[3][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 최대 녹화 간격 메뉴를 선택했습니다.",
            "interval_start" : True
            },
        {
            "xpath" : "//section[@class='service-setting__view']/div[3][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 최대 녹화 간격 메뉴를 닫았습니다.",
            "interval_end" : False
            }
        ]
    for recording_interval_xpath in recording_interval_time:
        recording_interva_btn = WebDriverWait(driver, recording_interval_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, recording_interval_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(recording_interva_btn)\
            .click(recording_interva_btn)\
            .perform()
        print(recording_interval_xpath["message"])
        time.sleep(3)
        
        if "interval_start" in recording_interval_xpath:
            time.sleep(3)
            
            # 로컬 녹화 : 최대 녹화 간격 메뉴 옵션 박스 출력
            try:
                recording_interva_box = driver.find_element(By.XPATH, "//div[@class='modal service-setting-modal']/div[4][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if recording_interva_box.is_displayed():
                    print("로컬 녹화 : 최대 녹화 간격 메뉴 옵션 박스가 존재합니다.")
                else:
                    print("로컬 녹화 : 최대 녹화 간격 메뉴 옵션 박스가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 : 최대 녹화 간격 메뉴 옵션 박스를 찾을 수 없습니다.")
        elif "interval_end" in recording_interval_xpath:
            # time.sleep(3)
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 클릭 > 최대 녹화 간격 시간 : 5분 > 10분 > 20분 > Default 1분 순차적 클릭
    recording_interval_option = [
        ('5 분', '로컬 녹화 : 5분을 선택하였습니다.'),
        ('10 분', '로컬 녹화 : 10분을 선택하였습니다.'),
        ('20 분', '로컬 녹화 : 20분을 선택하였습니다.'),
        ('1 분', '로컬 녹화 : 1분을 선택하였습니다.')
        ]
    for interval_click, interval_message in recording_interval_option:
        recording_interva_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, 
                "//section[@class='service-setting__view']/div[3][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(recording_interva_btn)\
            .click(recording_interva_btn)\
            .perform()
        print("로컬 녹화 : 최대 녹화 간격 메뉴를 클릭하였습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 로컬 녹화 : 최대 녹화 간격 시간 순차적 클릭
        recording_interval_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='modal service-setting-modal']/div[4][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{interval_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(recording_interval_click)\
            .click(recording_interval_click)\
            .perform()
        print(interval_message)
        time.sleep(3)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 녹화 영상 해상도 존재 확인
    try:
        recording_video_resolution = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[4][@class='service-setting__row']/div[@class='service-setting__text custom']/p[contains(text(), '녹화 영상 해상도')]")
        if recording_video_resolution.is_displayed():
            print("로컬 녹화 : 녹화 영상 해상도 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 녹화 영상 해상도 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("로컬 녹화 : 녹화 영상 해상도 메뉴를 찾을 수 없습니다.")
        
    #3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 > 녹화 영상 해상도 메뉴 클릭 > 녹화 영상 해상도 메뉴 옵션 박스 출력 확인
    video_resolution_recording = [
        {
            "xpath" : "//section[@class='service-setting__view']/div[4][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 녹화 영상 해상도 메뉴를 선택했습니다.",
            "resolution_start" : True
            },
        {
            "xpath" : "//section[@class='service-setting__view']/div[4][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label active']",
            "timeout" : 5,
            "message" : "로컬 녹화 : 녹화 영상 해상도 메뉴를 닫았습니다.",
            "resolution_end" : False
            }
        ]
    for video_resolution_xpath in video_resolution_recording:
        video_resolution_btn = WebDriverWait(driver, video_resolution_xpath["timeout"]).until(
            EC.presence_of_element_located((By.XPATH, video_resolution_xpath["xpath"])))
        actions = ActionChains(driver)\
            .move_to_element(video_resolution_btn)\
            .click(video_resolution_btn)\
            .perform()
        print(video_resolution_xpath["message"])
        time.sleep(3)
        
        if "resolution_start" in  video_resolution_xpath:
            time.sleep(3)
            
            # 녹화 영상 해상도 메뉴 옵션 박스 출력 확인
            try:
                video_resolution_box = driver.find_element(By.XPATH, "//div[@class='modal service-setting-modal']/div[5][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
                if video_resolution_box.is_displayed():
                    print("로컬 녹화 : 녹화 영상 해상도 메뉴 옵션 박스가 존재합니다.")
                else:
                    print("로컬 녹화 : 녹화 영상 해상도 메뉴 옵션 박스가 존재하지 않습니다.")
            except NoSuchElementException:
                print("로컬 녹화 : 녹화 영상 해상도 메뉴 옵션 박스를 찾을 수 없습니다.")
                
        elif "resolution_end" in video_resolution_xpath:
            # time.sleep(3)
            pass
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 녹화 영상 해상도 : 360p > 720p > 480p 순차적 클릭
    video_resolution_option = [
        ('360p', '로컬 녹화 : 360p를 선택하였습니다.'),
        ('720p', '로컬 녹화 : 720p를 선택하였습니다.'),
        ('480p', '로컬 녹화 : 480p를 선택하였습니다.')
        ]
    for resolution_click, resolution_message in video_resolution_option:
        video_resolution_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, 
            "//section[@class='service-setting__view']/div[4][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']")))
        actions = ActionChains(driver)\
            .move_to_element(video_resolution_btn)\
            .click(video_resolution_btn)\
            .perform()
        print("로컬 녹화 : 녹화 영상 해상도 메뉴를 클릭했습니다.")
        time.sleep(3)
        
        # 3초동안 암묵적 대기
        driver.implicitly_wait(time_to_wait=3)
        
        # 녹화 영상 해상도 순차적 클릭
        video_resolution_click = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='modal service-setting-modal']/div[5][@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{resolution_click}')]")))
        actions = ActionChains(driver)\
            .move_to_element(video_resolution_click)\
            .click(video_resolution_click)\
            .perform()
        print(resolution_message)
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 메뉴 > 참가자 로컬 녹화 메뉴 존재 확인
    try:
        participant_local_recording = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[5][@class='service-setting__row']/p[@class='service-setting__text' and contains(text(), '참가자 로컬 녹화')]")
        if participant_local_recording.is_displayed():
            print("로컬 녹화 : 참가자 로컬 녹화 메뉴가 존재합니다.")
        else:
            print("로컬 녹화 : 참가자 로컬 녹화 메뉴를 찾을 수 없습니다.")
    except NoSuchElementException:
        print("로컬 녹화 : 녹화 대상 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 로컬 녹화 설정 > 참가자 로컬 녹화 메뉴 > 참가자 로컬 녹화 허용 체크 해제 > 다시 참가자 로컬 녹화 허용 체크
    participant_local_option = [
        {
            "xpath" : "//div[@class='checkbox toggle']/span[@class='checkbox-toggle toggle' and contains(text(), 'ON')]",
            "timeout" : 5,
            "message" : "로컬 녹화 : 참가자 로컬 녹화 허용을 해제하였습니다."
            },
        {
            "xpath" : "//div[@class='checkbox']/span[@class='checkbox-toggle' and contains(text(), 'OFF')]",
            "timeout" : 5,
            "message" : "로컬 녹화 : 참가자 로컬 녹화 허용을 체크하였습니다."
            }
        ]
    participant_local_count = range(1, 2)
    for i in participant_local_count:
        for participant_xpath in participant_local_option:
            participant_local_btn = WebDriverWait(driver, participant_xpath["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, participant_xpath["xpath"])))
            actions = ActionChains(driver)\
                .move_to_element(participant_local_btn)\
                .click(participant_local_btn)\
                .perform()
            print(participant_xpath["message"])
            time.sleep(3)
            
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 메뉴 출력
    try:
        sever_recording_set = driver.find_element(By.XPATH, 
            "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting-nav']/button[@data-text='서버 녹화 설정' and @class='service-setting-nav__menu']")
        if sever_recording_set.is_displayed():
            print("서버 녹화 : 서버 녹화 설정 메뉴가 존재합니다.")
        else:
            print("서버 녹화 : 서버 녹화 설정 메뉴가 존재하지 않습니다.")
        
        # 서버 녹화 설정 메뉴 클릭
        sever_recording_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='modal service-setting-modal']/div[@class='modal--inner']/div[@class='modal--body']/div[@class='service-setting']/section[@class='service-setting-nav']/button[@data-text='서버 녹화 설정' and @class='service-setting-nav__menu']")))
        actions = ActionChains(driver)\
            .move_to_element(sever_recording_btn)\
            .click(sever_recording_btn)\
            .perform()
        print("서버 녹화 : 서버 녹화 설정 메뉴를 클릭했습니다.")
    except NoSuchElementException:
        print("서버 녹화 : 서버 녹화 설정 메뉴를 찾을 수 없습니다.")
        
    # 3초간 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 > 최대 녹화 시간 메뉴 출력
    try:
        maximum_recording_menu = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[@class='service-setting__row']/p[@class='service-setting__text' and contains(text(), '최대 녹화 시간')]")
        if maximum_recording_menu.is_displayed():
            print("서버 녹화 : 최대 녹화 시간 메뉴가 존재합니다.")
        else:
            print("서버 녹화 : 최대 녹화 시간 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("서버 녹화 : 최대 녹화 시간 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    #########  해당 코드는 현재 결함이 있기 때문에 결함 수정 이후에 xpath 다시 확인해 볼것 ########################################
    
    # 환경 설정 > 서버 녹화 설정 > 최대 녹화 시간 메뉴 클릭 > 최대 녹화 시간 옵션 박스 메뉴 출력 확인
    # recording_menu_option = [
    #     {
    #         "xpath" : "//section[@class='service-setting__view']/div[1][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']",
    #         "timeout" : 5,
    #         "message" : "서버 녹화 : 최대 녹화 시간 메뉴를 선택했습니다.",
    #         "maximum_recording_start" : True
    #         },
    #     {
    #         "xpath" : "//section[@class='service-setting__view']/div[2][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label active']",
    #         "timeout" : 5,
    #         "message" : "서버 녹화 : 최대 녹화 시간 메뉴를 선택했습니다.",
    #         "maximum_recording_end" : False
    #         }
    #     ]
    # for recording_menu_xpath in recording_menu_option:
    #     recording_menu_btn = WebDriverWait(driver, recording_menu_xpath["timeout"]).until(
    #         EC.presence_of_element_located((By.XPATH, recording_menu_xpath["xpath"])))
    #     actions = ActionChains(driver)\
    #         .move_to_element(recording_menu_btn)\
    #         .click(recording_menu_btn)\
    #         .perform()
    #     print(recording_menu_xpath["message"])
    #     time.sleep(3)
    
    #     # 3초동안 암묵적 대기
    #     driver.implicitly_wait(time_to_wait=3)
    
    #     if "recording_start" in recording_menu_xpath:
    #         time.sleep(3)
    
    #         # 최대 시간 옵션 박스 메뉴 출력 확인
    #         try:
    #             maximum_time_box = driver.find_element(By.XPATH, "//div[@class='service-setting']/section[@class='service-setting__view']/div[1][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/div[@role='tooltip']/div[@class='popover--body']/div[@class='select-optionbox']")
    #             if maximum_time_box.is_displayed():
    #                 print("서버 녹화 : 최대 시간 옵션 박스 메뉴가 존재합니다.")
    #             else:
    #                 print("서버 녹화 : 최대 시간 옵션 박스 메뉴가 존재하지 않습니다.")
    #         except NoSuchElementException:
    #             print("서버 녹화 : 최대 시간 옵션 박스 메뉴를 찾을 수 없습니다.")
    #     elif "recording_end" in recording_menu_xpath:
    #         # time.sleep(3)
    #         pass
    
    # # 3초동안 암묵적 대기
    # driver.implicitly_wait(time_to_wait=3)
    
    # 환경 설정 > 서버 녹화 설정 > 최대 녹화 시간 메뉴 : 5분 > 15분 > 30분 > 60분 > 30분 순차적 클릭
    # maximum_menu_option = [
    #     ('5 분', '서버 녹화 : 5분을 선택했습니다.'),
    #     ('15 분', '서버 녹화 : 15분을 선택했습니다.'),
    #     ('30 분', '서버 녹화 : 30분을 선택했습니다.'),
    #     ('60 분', '서버 녹화 : 60분을 선택했습니다.'),
    #     ('30 분', '서버 녹화 : 30분을 선택했습니다.')
    #     ]
    # for maximum_time, maximum_message in maximum_menu_option:
    #     recording_menu_btn = WebDriverWait(driver, ).until(
    #         EC.presence_of_element_located((By.XPATH, 
    #             "//section[@class='service-setting__view']/div[1][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/button[@class='select-label']")))
    #     actions = ActionChains(driver)\
    #         .move_to_element(recording_menu_btn)\
    #         .click(recording_menu_btn)\
    #         .perform()
    #     print("서버 녹화 : 최대 녹화 시간 메뉴를 선택했습니다.")
        
    #     # 3초동안 암묵적 대기
    #     driver.implicitly_wait(time_to_wait=3)
        
    #     # 최대 녹화 시간 메뉴 순차적 클릭
    #     recording_menu_click = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, f"//div[@class='service-setting']/section[@class='service-setting__view']/div[1][@class='service-setting__row']/span[@class='popover--wrapper service-setting__selector']/div[@role='tooltip']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{maximum_time}')]")))
    #     actions = ActionChains(driver)\
    #         .move_to_element(recording_menu_click)\
    #         .click(recording_menu_click)\
    #         .perform()
    #     print(maximum_message)
    #     time.sleep(3)
    
    #########  해당 코드는 현재 결함이 있기 때문에 결함 수정 이후에 xpath 다시 확인해 볼것 ########################################
    
    
    
    
    
    
    
    
    
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 환경설정 > 서버 녹화 설정 > 녹화 영상 해상도 메뉴 출력 확인
    try:
        recording_display_resolution = driver.find_element(By.XPATH, 
            "//section[@class='service-setting__view']/div[@class='service-setting__row']/div[@class='service-setting__text custom']/p[contains(text(), '녹화 영상 해상도')]")
        if recording_display_resolution.is_displayed():
            print("서버 녹화 : 녹화 영상 해상도 메뉴가 존재합니다.")
        else:
            print("서버 녹화 : 녹화 영상 해상도 메뉴가 존재하지 않습니다.")
    except NoSuchElementException:
        print("서버 녹화 : 녹화 영상 해상도 메뉴를 찾을 수 없습니다.")
        
    # 3초동안 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)






finally:
    # 브라우저 세션 종료
    # driver.quit()
    print("브라우저창을 닫습니다.")
