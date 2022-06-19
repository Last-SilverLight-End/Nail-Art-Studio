
#-----------------------------
from selenium import webdriver
import time
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(r'Pinata\text.py'))))
from selenium.webdriver.chrome.options import Options
import klaytninfo as info
import klaytnAuto as auto
#import Pinata.text as text

#-----------------------------
class KlaytnAutoProcess:
    
    def __init__(self) -> None:
        url = 'https://ide.klaytn.com'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)


    def main(self):
        url = 'https://ide.klaytn.com'
        self.IDEAuto()
        self.transaction()
        complete = self.sendNFT()
        if(complete==True):
            print('send NFT complete')
            f = open('Pinata/ipfs.txt','w')
            f.write('clear')
            self.driver.quit()

        
    def IDEAuto(self):
        url = 'https://ide.klaytn.com'
        self.driver.get(url)
        time.sleep(1)
        while(True):
            try:
                #self.driver.get('https://ide.klaytn.com/#optimize=false&runs=200&evmVersion=istanbul&version=soljson-v0.5.17+commit.d19bba13.js')
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath('//*[@id="remixTourSkipbtn"]').click()
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="plugins"]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/p[2]/label').click()
                time.sleep(1)
                auto.path()
                time.sleep(1)
                break
            except:
                print('대기중')
                time.sleep(5)
        print('select complete by sol')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="fileExplorerView"]/div[1]/div/div[2]/div/div[1]/div/ul/li/div[2]/ul/li[5]/div/span/div/span').click()

        #0.5.17
        self.driver.find_element_by_xpath('//*[@id="verticalIconsKindsolidity"]/img').click()
        self.driver.find_element_by_xpath('//*[@id="versionSelector"]/option[38]').click()

        #istanbul
        self.driver.find_element_by_xpath('//*[@id="evmVersionSelector"]/option[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="compileBtn"]').click()
        time.sleep(1)
        while(True):
            try:
                self.driver.find_element_by_xpath('//*[@id="publishOnIpfs"]').click()
                time.sleep(2)
                while(True):
                    try:
                        self.driver.find_element_by_xpath('//*[@id="compileTabView"]/div[1]/div/div/div[3]/span').click()
                        break
                    except:
                        print('publish loading')
                        time.sleep(1)
                break
            except:
                print('ipfs loading')
                time.sleep(1)

        #여기에 publish on IPFS 버튼 클릭 try : except로 넣어서 timesleep 줄이기


    def transaction(self):
        url = 'https://ide.klaytn.com'
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="verticalIconsKindudapp"]/img').click()
        time.sleep(3)
        #self.driver.find_element_by_xpath('//*[@id="baobab-public-en"]"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="remixRunPlus"]').click()

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="modal-body-id"]/div/div/div[1]/button[2]').click()
        #keystore
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="importKeyByKeystore"]/dl[1]/dd/label').click()
        auto.keyStore()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="keyStorePasswordField"]').send_keys('Graphics405!')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-footer-ok"]').click()

        #AccToken
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[1]/select/option[12]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/i').click()
        time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]/input').send_keys(info.NFTName)
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/input').send_keys(info.NFTName)
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[3]/input').send_keys('0x8126c4ec212d3779a21bb40FB0b163E2beAad32F') #컨트랙트 주소로 설정 변경.
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="runAndDeployAtAdressButton"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[1]/button').click()
        time.sleep(1)
        
        

    def sendNFT(self):
        url = 'https://ide.klaytn.com'
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[1]/i').click()
        time.sleep(1)
        f = open('Pinata/ipfs.txt','r')
        Json_ipfs = f.readline()
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[2]/div/div[2]/div/input').send_keys(Json_ipfs)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[2]/div/div[3]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[1]/i').click()
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/input').send_keys(info.walletAddress)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[2]/input').send_keys('1')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[3]/button').click()
        time.sleep(5)
        return True

if __name__ == '__main__':
    klaytnAutoProcess = KlaytnAutoProcess()
    
    klaytnAutoProcess.main()