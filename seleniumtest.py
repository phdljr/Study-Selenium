from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen

# 크롬 드라이버 위치를 찾아서 selenium 객체를 받아온다. 그거를 dirver 변수에 저장한다.
driver = webdriver.Chrome("C:/Users/Ted/Desktop/chromedriver_win32/chromedriver.exe")
# 창이 잘 열리기 위해서 1초 대기
driver.implicitly_wait(10) 

# nun이 1부터 27까지 반복
for num in range(1, 28):
    # 사진의 url 패턴을 보면 num이 하나씩 증가하는 모습을 볼 수 있음
    url = f"https://tr.hangame.com/guide/characterinfo.asp?num={num}&ctype=0"
    # 해당 url의 html 정보를 다 저장
    driver.get(url)

    # 저장한 html 정보를 하나하나 찾아가는 과정이 밑의 세 줄
    myDynamicElement = driver.find_element(By.CLASS_NAME, 'character-img') # 클래스 이름을 기준으로 태그를 탐색
    myDynamicElement = myDynamicElement.find_element(By.TAG_NAME, 'span') # 위에서 찾은 div 태그 안에서 span 태그를 탐색
    src = myDynamicElement.get_attribute('style') # 위에서 찾은 span 태그 안에서 style 속성 데이터 가져옴

    myDynamicElement = driver.find_element(By.CLASS_NAME, f'li{num}') # 클래스 이름을 기준으로 태그를 탐색
    myDynamicElement = myDynamicElement.find_element(By.TAG_NAME, 'span')
    character = myDynamicElement.text

    # style 속성의 문자열을 어느정도 가공하여 딱 url만 가져올 수 있도록 문자열 처리
    src = src[23:src.find(".png")+4]
    # # 파일 이름을 캐릭터 이름으로 저장하기 위해서 캐릭터 이름을 문자열 처리로 가져옴
    # character = src[src.find("images/character/") + 17 : src.find("/img_")]

    # 이미지 url에 접근해서 데이터를 저장하는 코드
    with urlopen(src) as f:
        with open('./images/' + character + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

driver.close()