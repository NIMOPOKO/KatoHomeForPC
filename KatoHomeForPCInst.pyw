import os

cwd = os.getcwd()
save_path="C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\KatoHomeForPC.lnk"
file_path=cwd + "\\bin\\app.exe"
os.symlink(file_path, save_path)