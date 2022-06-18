from dictParse import Get_GUI_Dict
from WindowEvent import WindowEvent as winE
from Process import Process
import time
#ExePath= '"C:\Program Files\Snap Inc\Lens Studio\Lens Studio.exe"'
class LensStudio:
    __ExePath= '"C:\Program Files\Snap Inc\Lens Studio\Lens Studio.exe"'
    __GUI_Info_Location='locate.json'
    __ProcessName="Lens Studio"
    __PopUpProcessList=["Project Backup Recovery"]
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
    def openLens(self,filePath="C:/nailTracking",fileName="nailTracking.lsproj"):
        lensGUI=self.GUI_Dict["Lens Studio"]
        FileChoose=self.GUI_Dict["Choose project file"]
        winE.maximize().click(lensGUI["File"]).click(lensGUI["Open Project"])
        winE.maximize().click(FileChoose["Address_Bar"]
        ).setText(filePath).press("enter").click(FileChoose["FileName_Bar"]).setText(fileName
        ).click(FileChoose["Open"])
        try:
            if not Process.isAwakeUntilTime(lambda:Process.includes(fileName),1.0,8): Exception(f"Can't open {fileName} project")
            LensStudio.__ProcessName=f"{fileName} - {LensStudio.__ProcessName}"
            newProc=Process.getProcess(LensStudio.__ProcessName)
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