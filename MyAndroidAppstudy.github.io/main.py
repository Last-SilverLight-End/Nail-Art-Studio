from snapWarn import LensStudio


    

#if __name__=='__main__':
#    app=LensStudio.run()
#    app.maximize()
#    app.openLens()
#    app.maximize()
#    publishCode=app.publishLens()
#    print(publishCode)
#    app.close()
publishCode=""

class AutoProcess3:
    def main(self):
        app=LensStudio.run()
        app.maximize()
        app.openLens()
        app.maximize()
        publishCode=app.publishLens()
        print(publishCode)
        app.close()
        return publishCode


if __name__=='__main__':
    autoprocess = AutoProcess3()
    autoprocess.main() 
