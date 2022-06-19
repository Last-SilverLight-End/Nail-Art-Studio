
#------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import text
import createJson
import time
import pinataAuto


#------------------------------------
#gvrlab05
#Graphics405!
#chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"


class PinataAutoProcess:
    pinataUrl = "https://app.pinata.cloud/signin"
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)



# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(chrome_driver, options= chrome_options)


with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()

def movePage_Pinata(self):
    with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()    
    self.driver.get(self.pinataUrl)

    logIn_Pinata()
    upLoad()
   
    complete = uploadFolder()
    print(complete)
    Pinatatext.close()
    print('ipfs업로드 완료')
    if(complete!=None):
        import klaytnMain
        klaytnMain.main()
    
    
    
    
def logIn_Pinata(self):
    with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()
    self.driver.implicitly_wait(3)
    self.driver.find_element_by_name('email').send_keys(text.email)
    self.driver.implicitly_wait(3)
    self.driver.find_element_by_name('password').send_keys(text.password)
    self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/button').click()
    print("complete")
    

def upLoad(self):
    with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()
    time.sleep(3)  
    while(True):
        time.sleep(3)
        try:
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()
            
            print("+upload btn")
            break
        except:
            print('ipfs loading....')
            time.sleep(3)

    while(True):
        try:
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[2]').click()
            print("file btn")
            break
        except:
            print('find File btn')
            time.sleep(3)
        time.sleep(3)
    while(True):
        try:
            pinataAuto.uploadImageAuto()
            time.sleep(3)
            break
        except:
            time.sleep(3)
            print('gui auto loading')
        
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div/button']").send_keys(r"C:\Users\mvr\Desktop\JM\NFT/"+text.file_name) # 상대경로로 변경하기 사진 경로
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div/button']").click()
        # print("upLoad")
        
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
        # print("image upload complete")
        while(True):
            try:
                time.sleep(3)
                self.driver.implicitly_wait(10)
                driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button").click()
                print("image upload complete")
                break
            except:
                print('load')
                time.sleep(3)        
    driver.implicitly_wait(5)

    while(1):
        try:
            copyPath()
            break
        except:
            print('로딩중..')
            time.sleep(3)
   
def copyPath():
    with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()
    '''
    global ipfs 
    ipfs = driver.find_element_by_link_text(text.file_name).get_attribute('href')
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    ipfs_split= ipfs.split('/')
    ipfs = ipfs_split[4]
    ipfs = 'ipfs://'+ipfs
sample_zepeto.png

    text.ipfs = ipfs
    createJson.main()
    '''
    global ipfs 
    if(text.ipfs==""):
        ipfs = driver.find_element_by_link_text(text.file_name).get_attribute('href')
        last_tab = driver.window_handles[-1]
        driver.switch_to.window(window_name=last_tab)
        ipfs_split= ipfs.split('/')
        ipfs = ipfs_split[4]
        ipfs = 'ipfs://'+ipfs
        text.ipfs = ipfs
        print(text.ipfs)
        createJson.main()
    else:
        ipfsinfo = open('ipfs.txt','w')
            
        Json_ipfs = driver.find_element_by_link_text(text.username).get_attribute('href')
        ipfs_split= Json_ipfs.split('/')
        Json_ipfs = ipfs_split[4]
        Json_ipfs = 'ipfs://'+Json_ipfs+'/'
        text.json_ipfs = Json_ipfs
        print('tlqkf')
        ipfsinfo.write(Json_ipfs)
        print(ipfsinfo)
        ipfsinfo.close()
        return Json_ipfs
        #print(text.json_ipfs)

def uploadFolder():
    with open(r'pinatatext.txt','r') as Pinatatext:
        Pinatatext.readlines()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/button').click()

    print("+upload btn")

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[4]/div/div/div/div/div[1]/div/div[1]/div/div/div/a[1]').click()
    print('folder')

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
    print('select')

    pinataAuto.uploadPinataAutogui()
    #--upload

    driver.find_element_by_xpath('//*[@id="thresholdconfig"]').send_keys(text.username)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/button').click()
    while(1):
        try:
            useripfs = copyPath()
            return useripfs
            break
        except:
            print('cid추출중')
            time.sleep(3)
        print('pinata종료')
    #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/text()').click()
    #driver.find_element_by_xpath('//*[@id="layout-wrapper"]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/button/i').click()
    #여기서 json ipfs 추출하기


if __name__ == '__main__':
    pinataAutoProcess = PinataAutoProcess()
    
    pinataAutoProcess.movePage_Pinata()

#uploadFolder()
#QmWj3vMLQg43Dp6nzSgMbRdVLE36euT57ro7RDAR2eGYZD