#-------------------------
from selenium import webdriver
import time

import pyautogui
import zepetoAuto
#----------------------------
class AutoProcess:
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)




    def main(self):
        with open(r'zepetoText.txt','r') as info:
            text = info.readlines()
        self.LogInPage()

        print("로그인 성공")

        #upload()
        self.uploadImage()
        print(text)
        self.writeInfo()

        self.info.close()
        time.sleep(1)
        self.driver.quit()

    def LogInInfo2(self,form,id,pwd):
        with open(r'zepetoText.txt','r') as info:
            text = info.readlines()
        info=[id,pwd]
        elems=list(map(lambda b,x:b.find_element_by_class_name(f"user_{x}"),form.find_elements_by_class_name("input_box"),["email","password"]))
        for i,elem in enumerate(elems):elem.send_keys(info[i]) 

    def LogInPage(self):
        url="https://studio.zepeto.me/kr/console/items"
        self.driver.get(url)
        #options.add_argument('headless')
        #driver.close()
        with open(r'zepetoText.txt','r') as info:
            text = info.readlines()
        signType=self.driver.find_element_by_class_name("sign_in_type")
        mailLoginBtn=signType.find_elements_by_tag_name("li")[1]
        mailLoginBtn.click()
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        form=self.driver.find_element_by_tag_name("form")
        self.LogInInfo2(form,text[0],text[1])
        self.driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/article/div/div/div[2]/form/button').click()



    def uploadImage(self):
    
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/nav/div/div[1]/button/div/div/div').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[3]/ul/li[1]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/article/div/div/section/div[4]/div/div/div[1]/div[2]/div/div/div/div[2]/div/a/span[1]').click()#네일 생성 버튼
        time.sleep(5)
        #driver.quit()
        while True:
            try:
                #time.sleep(3)
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click()
                #driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/article/div/div/div/div/div[2]/button').click().send_keys(r"C:/Users/mvr/Desktop/image/"+zepeto.fileName)
                zepetoAuto.uploadZepetoAutogui()
                time.sleep(2)
                self.driver.find_element_by_class_name('upload_btns').click()
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
            
        

    def writeInfo(self):
        # # with open(r'zepetoText.txt','r') as info:
        # #     text = info.readlines()
        # self.driver.implicitly_wait(3)
        # self.driver.find_element_by_xpath('//*[@id="user_name"]').send_keys(text[3])
        # print('이름 입력')

        # time.sleep(10)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/header/div/button[1]').click()

        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/button').click()
        #오류
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/header/div/button[1]').click()
        time.sleep(1)
        print('완료')
  
if __name__ == '__main__':
    autoprocess = AutoProcess()
    
    autoprocess.main()

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