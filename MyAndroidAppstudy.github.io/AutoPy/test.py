from pywinauto import application
import time
from WindowEvent import WindowEvent as winE
from Process import Process


Lens="Lens Studio"
a=application.findwindows.find_elements(title_re=f".*{Lens}.*")
a=a[0]
app=application.Application(backend="uia").connect(process=a.process_id)
print(app)