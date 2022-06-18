from pywinauto import application
import time
class noPopUp:
    def __CheckUpInvoke(self, dlg):
        try: dlg.window_text()
        except: return False
        else: return True
    def __init__(self, title):
        self.title = title
        self.app = None
        self.findAndRemove()
    def findAndRemove(self):
        procs = application.findwindows.find_elements(
            title_re=f".*{self.title}")
        try:
            if not procs: raise Exception(f"없는 element, title:{self.title}")
            for proc in procs:
                self.app = application.Application(
                    backend="uia").connect(process=proc.process_id)
                dlg = self.app[self.title]["Static"]
                if self.__CheckUpInvoke(dlg): Process.close(self.app,self.title)
        except Exception as e: print(e)

class Process:
    @staticmethod
    def getURL(Browser="Chrome",timeDelay=2,iterCylcle=10):
        for i in range(iterCylcle):
            try:
                proc=Process.getProcess(Browser)
                app=Process.getApp(proc)
                dlg=app.top_window()
                url=dlg.child_window(title="주소창 및 검색창", control_type="Edit").get_value()
                Process.close(app)
                return url
            except: time.sleep(timeDelay)
        print("Can't open browser")
        return None
    @staticmethod
    def __getProcs(ProcessName):
        procs=application.findwindows.find_elements(title_re= f'.*{ProcessName}.*')
        if procs: return procs
        else: return None
    @staticmethod
    def setActive(app): app.set_focus()

    @staticmethod
    def close(App,Title=None):
        if Title is not None:
            dlg = App[Title]["TitleBar"]
            dlg.child_window(title="닫기", control_type="Button").click()
        else:
            App.top_window().type_keys("%{F4}") # Alt-F4

    @staticmethod
    def isAwakeUntilTime(lambdaFn,sleepTime=2.0,cntMax=5):
        try:
            for i in range(cntMax):
                if lambdaFn(): return True
                else: time.sleep(sleepTime)
            Exception("Count is Over!!")
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def start(ExePath): application.Application(backend="uia").start(ExePath)
    @staticmethod
    def getApp(Proc):
        return application.Application(backend="uia").connect(process=Proc.process_id)
    @staticmethod
    def getProcess(ProcessName):
        procs=Process.__getProcs(ProcessName)
        if procs is None:
            print("There is NO Process")
            return procs
        elif len(procs)==1: return procs[0]
        else:
            print("Have many process in this process name")
            return None
    @staticmethod
    def includes(ProcessName): return True if Process.__getProcs(ProcessName) else False

    @staticmethod
    def allKill(ProcessName):
        procs=Process.__getProcs(ProcessName)
        if procs is not None:
            for proc in procs:
                app=application.Application(backend="uia").connect(process=proc.process_id)
                app.kill()
    @staticmethod
    def killPopUp(PopUpProcessList):
        try:
            if PopUpProcessList is not list: Exception("Is not list")
        except Exception as e:
            print(e)
        else:
            for i in PopUpProcessList:
                noPopUp(i)


                #if proc.name is not ProcessName:
                #    winE.close(app,proc.rich_text)
                #else: winE.close(app,proc.name)