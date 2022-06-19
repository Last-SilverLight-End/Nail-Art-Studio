
#------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import text
import createJson
import time
import pinataAuto
from klaytnMain import KlaytnAutoProcess
#------------------------------------
#gvrlab05
#Graphics405!
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(chrome_driver, options= chrome_options)
class PinataAutoProcess:
    
    def __init__(self) -> None:
        pinataUrl = "https://app.pinata.cloud/signin"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)



    def movePage_Pinata(self):
        pinataUrl = "https://app.pinata.cloud/signin"
        with open(r'pinatatext.txt','r') as info:
            Pinatatext = info.readlines()
        print(Pinatatext)
        self.driver.get("https://app.pinata.cloud/signin")

        self.logIn_Pinata()
        self.upLoad()
        
        ipfs_extract=self.uploadFolder()
        info.close()

        print('ipfs업로드 완료')
        if(ipfs_extract==True):
            autoprocess4 = KlaytnAutoProcess()
            autoprocess4.main()
            self.driver.quit()  
        else :
            print('오류')
            return 0

        
        

    def logIn_Pinata(self):
        pinataUrl = "https://app.pinata.cloud/signin"
        with open(r'pinatatext.txt','r') as info:
            Pinatatext = info.readlines()

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name('email').send_keys(Pinatatext[0])
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name('password').send_keys(Pinatatext[1])
       
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/button').click()
        print("complete")
        info.close()

    def upLoad(self):  
        pinataUrl = "https://app.pinata.cloud/signin"
        while(True):
            try:
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()
                print("+upload btn")
                break
            except:
                print('ipfs loading....')
                time.sleep(1)

        while(True):
            try:
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[2]').click()
                print("file btn")
                time.sleep(1)
                pinataAuto.uploadImageAuto()
                break
            except:
                print('find File btn')
                time.sleep(1)
            time.sleep(1)
            
            # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div/button']").send_keys(r"C:\Users\mvr\Desktop\JM\NFT/"+text.file_name) # 상대경로로 변경하기 사진 경로
            # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div/button']").click()
            # print("upLoad")

            
            # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
            time.sleep(1)
            # self.driver.implicitly_wait(10)
            # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
            print("image upload complete")

            time.sleep(1)
        while(1):
            try:
                imageipfs = self.copyPath(1)
                if(imageipfs==True):
                    break
            except:
                print('Json생성중')
                time.sleep(1)
    
    def copyPath(self,id):
        pinataUrl = "https://app.pinata.cloud/signin"
        global ipfs 
        
        if(id==1):
            ipfs = self.driver.find_element_by_link_text(text.file_name).get_attribute('href')
            last_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(window_name=last_tab)
            ipfs_split= ipfs.split('/')
            ipfs = ipfs_split[4]
            ipfs = 'ipfs://'+ipfs
            f = open('Pinata/ipfs.txt','w')
            f.write(ipfs)
            f.close()
            #text.ipfs = ipfs
            if(ipfs!=None):
                createJson.main()
                
                return True
        else:
            Json_ipfs = self.driver.find_element_by_link_text(text.username).get_attribute('href')
            last_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(window_name=last_tab)
            ipfs_split= Json_ipfs.split('/')
            Json_ipfs = ipfs_split[4]
            Json_ipfs = 'ipfs://'+Json_ipfs+'/'
            f = open('Pinata/ipfs.txt','w')
            f.write(Json_ipfs)
            f.close()
            with open(r'pinatatext.txt','r') as info:
                Pinatatext = info.readlines()
            print(Pinatatext)
            #print(text.json_ipfs)

    def uploadFolder(self):
        pinataUrl = "https://app.pinata.cloud/signin"
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()

        print("+upload btn")

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[1]').click()
        print('folder')

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
        print('select')

        pinataAuto.uploadPinataAutogui()
        #--upload
        with open('pinatatext.txt','r') as r:
                text = r.readlines()
        #self.driver.find_element_by_xpath('//*[@id="thresholdconfig"]').send_keys(text.username)
        self.driver.find_element_by_xpath('//*[@id="thresholdconfig"]').send_keys(text[3])
        r.close()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
        while(1):
            try:
                self.copyPath(2)
                return True
            except:
                print('cid추출중')
                time.sleep(3)
        
        #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/text()').click()
        #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/i').click()
        #여기서 json ipfs 추출하기


if __name__ == '__main__':
    pinataAutoProcess = PinataAutoProcess()
    
    pinataAutoProcess.movePage_Pinata()
