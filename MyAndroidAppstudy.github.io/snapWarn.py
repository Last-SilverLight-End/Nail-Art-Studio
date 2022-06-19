from dictParse import Get_GUI_Dict
from WindowEvent import WindowEvent as winE
from Process import Process
import time
from selenium import webdriver
import time
#ExePath= '"C:\Program Files\Snap Inc\Lens Studio\Lens Studio.exe"'
class LensStudio:
    __ExePath= '"C:\Program Files\Snap Inc\Lens Studio\Lens Studio.exe"'
    __GUI_Info_Location='locate.json'
    __ProcessName="Lens Studio"
    __PopUpProcessList=["Project Backup Recovery"]
    __isLogin=False
    @staticmethod
    def run():
        Process.killPopUp(LensStudio.__PopUpProcessList)
        Process.allKill(LensStudio.__ProcessName)
        if not Process.isAwakeUntilTime(lambda:not Process.includes(LensStudio.__ProcessName),2.0,5): return None
        Process.start(LensStudio.__ExePath)
        if not Process.isAwakeUntilTime(lambda: Process.includes(LensStudio.__ProcessName),5.0,10): return None
        Process.killPopUp(LensStudio.__PopUpProcessList)
        return LensStudio(Process.getProcess(LensStudio.__ProcessName))
    def __init__(self, proc):
        try:
            if proc is None: raise Exception("None Process, can't init LensStudio")
        except Exception as e:
            print(e)
        else:
            self.app=Process.getApp(proc)
            self.dlg = self.app['Lens Studio']
            self.GUI_Dict=Get_GUI_Dict(LensStudio.__GUI_Info_Location)
            print(self.GUI_Dict)
            self.projectFile=None

    def close(self): Process.close(self.app)
    def maximize(self): winE.maximize()
    def getLogInURL(self):
        loginPosition=self.GUI_Dict["LogIn"]
        winE.click(loginPosition)
        LogInURL=Process.getURL()
        return LogInURL
    def LogIn(self,url):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        driver = webdriver.Chrome('chromedriver.exe', options=options)    
        driver.get(url)
        pass
    def openLens(self,url,filePath="C:/nailTracking",fileName="nailTracking"):
        self.LogIn(url)
        lensGUI=self.GUI_Dict["Lens Studio"]
        FileChoose=self.GUI_Dict["Choose project file"]
        winE.maximize().click(lensGUI["File"]).click(lensGUI["Open Project"]).click(FileChoose["Address_Bar"]
        ).setText(filePath).press("enter").click(FileChoose["FileName_Bar"]).setText(fileName
        ).click(FileChoose["Open"])
        try:
            if not Process.isAwakeUntilTime(lambda:Process.includes(fileName),1.0,8): Exception(f"Can't open {fileName} project")
            LensStudio.__ProcessName=f"{fileName} - {LensStudio.__ProcessName}"
            timeDelay=2
            iterCylcle=10
            newProc=Process.getProcess(LensStudio.__ProcessName)
            for i in range(iterCylcle):
                if newProc is None:
                    newProc=Process.getProcess(LensStudio.__ProcessName)
                    time.sleep(timeDelay)
            self.app=Process.getApp(newProc)
            self.dlg = self.app[LensStudio.__ProcessName]
            print(LensStudio.__ProcessName,"Process Name")
            #self.dlg.print_control_identifiers()
        except Exception as e:
            print(e)
    def publishLens(self):
        lensGUI=self.GUI_Dict["Lens Studio"]
        publishLens=self.GUI_Dict["Publish Lens"]
        winE.click(publishLens)
        publishCode=Process.getURL()
        return publishCode
    def LogOut(self):
        lensGUI=self.GUI_Dict["Lens Studio"]
        My_Lenses_Position=lensGUI["My Lenses"]
        Log_Out_Position=lensGUI["Log Out"]
        Done_Position=self.GUI_Dict["Done"]
        winE.click(Done_Position).click(My_Lenses_Position).click(Log_Out_Position)