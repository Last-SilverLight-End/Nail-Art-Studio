
#-------------------------
from selenium import webdriver
import time

import pyautogui
import zepetoAuto
#----------------------------

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome('chromedriver.exe', options=options)

with open(r'zepetoText.txt','r') as info:
    text = info.readlines()


def main():
    LogInPage()

    print("로그인 성공")

    #upload()
    uploadImage()
    
    writeInfo()

    info.close()
    driver.quit()

def LogInInfo2(form,id,pwd):
    info=[id,pwd]
    elems=list(map(lambda b,x:b.find_element_by_class_name(f"user_{x}"),form.find_elements_by_class_name("input_box"),["email","password"]))
    for i,elem in enumerate(elems):elem.send_keys(info[i]) 
def LogInPage():
    url="https://studio.zepeto.me/kr/console/items"
    driver.get(url)
    #options.add_argument('headless')
    #driver.close()
    
    signType=driver.find_element_by_class_name("sign_in_type")
    mailLoginBtn=signType.find_elements_by_tag_name("li")[1]
    mailLoginBtn.click()
    driver.implicitly_wait(3)
    driver.get(url)
    form=driver.find_element_by_tag_name("form")
    LogInInfo2(form,text[0],text[1])
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div[1]/article/div/div/div[2]/form/button').click()



def uploadImage():
    
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/nav/div/div[1]/button/div/div/div').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[3]/ul/li[1]/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/article/div/div/section/div[4]/div/div/div[1]/div[2]/div/div/div/div[2]/div/a/span[1]').click()#네일 생성 버튼
    
    time.sleep(5)
    #driver.quit()
    while True:
        try:
            #time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click()
            #driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click().send_keys(r"C:/Users/mvr/Desktop/image/"+zepeto.fileName)
            zepetoAuto.uploadZepetoAutogui()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div/header/div/a').click()
            #driver.find_element_by_class_name('upload_btns').click()
            break
        except:
            print('대기중')
            time.sleep(10)
            # time.sleep(30)
            # print('실행가능')
            # time.sleep(3)
            # driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click()
            # #driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click().send_keys(r"C:/Users/mvr/Desktop/image/"+zepeto.fileName)
            # zepetoAuto.uploadZepetoAutogui()
            # time.sleep(2)
            # driver.find_element_by_class_name('upload_btns').click()
            
        

def writeInfo():
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(text[3])
    print('이름 입력')

    time.sleep(10)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/header/div/button[1]').click()

    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div/div/div/button').click()

  
main()



# def upload(): #try catch로 오류 설정.
#     driver.implicitly_wait(10)
#     driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/nav/div/div[1]/button/div/div/div').click()
#     driver.implicitly_wait(3)
#     driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[3]/ul/li[1]/button').click()
#     driver.implicitly_wait(3)
#     driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/button').click()
    
    
#     time.sleep(3)
#     driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/article/div/div/section/div[4]/div/div/div[1]/div[2]/div/div/div/div[2]/div/a/span[1]').click()#네일 생성 버튼
#     # time.sleep(10)
#     # driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click()
#     # ##driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click().send_keys(r"C:/Users/mvr/Desktop/image/"+zepeto.fileName)
#     # zepetoAuto.uploadZepetoAutogui()
#     # time.sleep(2)
#     # driver.find_element_by_class_name('upload_btns').click()