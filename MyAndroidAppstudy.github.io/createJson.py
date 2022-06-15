
#------------------------------
import json
from collections import OrderedDict
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
    for i in range(0,text.count):
        makeJson["name"] = text.NFTname+'#'+str(i+1)
        makeJson["description"] = text.description
        makeJson["image"] = text.ipfs
        #with open(str(i+1)+'.json','w') as saveFile: 
        with open(FolderPath+'/'+str(i+1)+'.json','w') as saveFile: 
            json.dump(makeJson,saveFile,indent=4)
