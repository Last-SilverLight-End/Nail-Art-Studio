
#-----------------------------
from selenium import webdriver
import time
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(r'Pinata\text.py'))))
from selenium.webdriver.chrome.options import Options
import klaytninfo as info
import klaytnAuto as auto
import Pinata.text as text

#-----------------------------

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver = webdriver.Chrome('chromedriver.exe', options=options)


url = 'https://ide.klaytn.com'
def main():
    IDEAuto()
    transaction()
    sendNFT()

def IDEAuto():
    driver.get(url)
    time.sleep(1)
    while(True):
        try:
            #driver.get('https://ide.klaytn.com/#optimize=false&runs=200&evmVersion=istanbul&version=soljson-v0.5.17+commit.d19bba13.js')
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="remixTourSkipbtn"]').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="plugins"]/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/p[2]/label').click()
            time.sleep(1)
            auto.path()
            time.sleep(1)
            break
        except:
            print('대기중')
            time.sleep(5)
    print('select complete by sol')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="fileExplorerView"]/div[1]/div/div[2]/div/div[1]/div/ul/li/div[2]/ul/li[5]/div/span/div/span').click()

    #0.5.17
    driver.find_element_by_xpath('//*[@id="verticalIconsKindsolidity"]/img').click()
    driver.find_element_by_xpath('//*[@id="versionSelector"]/option[37]').click()

    #istanbul
    driver.find_element_by_xpath('//*[@id="evmVersionSelector"]/option[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="compileBtn"]').click()
    time.sleep(1)
    while(True):
        try:
            driver.find_element_by_xpath('//*[@id="publishOnIpfs"]').click()
            time.sleep(2)
            while(True):
                try:
                    driver.find_element_by_xpath('//*[@id="compileTabView"]/div[1]/div/div/div[3]/span').click()
                    break
                except:
                    print('publish loading')
                    time.sleep(1)
            break
        except:
            print('ipfs loading')
            time.sleep(1)

    #여기에 publish on IPFS 버튼 클릭 try : except로 넣어서 timesleep 줄이기


def transaction():
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="verticalIconsKindudapp"]/img').click()
    time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="baobab-public-en"]"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="remixRunPlus"]').click()

    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="modal-body-id"]/div/div/div[1]/button[2]').click()
    #keystore
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="importKeyByKeystore"]/dl[1]/dd/label').click()
    auto.keyStore()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="keyStorePasswordField"]').send_keys('Graphics405!')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="modal-footer-ok"]').click()

    #AccToken
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[1]/select/option[12]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/i').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[1]/input').send_keys(info.NFTName)
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div[2]/input').send_keys(info.NFTName)
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[3]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="runTabView"]/div/div[2]/div[2]/div[3]/input').send_keys('0x8126c4ec212d3779a21bb40FB0b163E2beAad32F')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="runAndDeployAtAdressButton"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[1]/button').click()
    time.sleep(1)
    
    

def sendNFT():
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[1]/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[2]/div/div[2]/div/input').send_keys(text.json_ipfs)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[19]/div[1]/div[2]/div/div[3]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[1]/i').click()
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[1]/input').send_keys(info.walletAddress)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[2]/input').send_keys('1')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="instance0x8126c4ec212d3779a21bb40FB0b163E2beAad32F"]/div[2]/div[3]/div[1]/div[2]/div/div[3]/button').click()
    time.sleep(5)
    
    #이후 minting 자동화 하면 됩니다.

main()