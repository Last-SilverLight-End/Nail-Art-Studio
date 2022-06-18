from snapWarn import LensStudio


    

if __name__=='__main__':
    app=LensStudio.run()
    app.maximize()
    app.openLens()
    app.maximize()
    publishCode=app.publishLens()
    print(publishCode)
    app.close()