
#------------------------------
import json
from collections import OrderedDict
import datetime
import text as text
import os
#------------------------------
makeJson = OrderedDict()
#folderPath = r'C:/Users/mvr/Desktop/JM/NFT/'+text.username
folderPath = text.username
#filePath = r"C:/Users/mvr/Desktop/JM/NFT/json"

def main():
    createFolder(folderPath)
    createJson(folderPath)
 
 

def createFolder(folderName):
    try:
        if not os.path.exists(folderName):
            os.makedirs(folderName)
    except OSError:
        print ('Error: Creating directory.' +  folderName)



def createJson(FolderPath):
    #makeJson["name"] = text.NFTname
    name = datetime.datetime.now()
    makeJson["name"] = str(name)
    makeJson["description"] = text.description
    with open('Pinata/ipfs.txt','r') as f:
        line = f.readlines()
    makeJson["image"] = line[0]
    #with open(str(i+1)+'.json','w') as saveFile: 

    for i in range(0,100):
        with open(FolderPath+'/'+str(i+1)+'.json','w') as saveFile: 
            json.dump(makeJson,saveFile,indent=4)