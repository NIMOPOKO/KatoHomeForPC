import os


save_path="C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\KatoHomeForPC.lnk"
file_path="C:\\Users\\"+os.getlogin()+"\\Desktop\\valorant app\\KatoHome\\app\\app.exe"
os.symlink(file_path, save_path)