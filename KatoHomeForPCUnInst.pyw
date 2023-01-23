import os


delete_path="C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\KatoHomeForPC.lnk"
os.remove(delete_path)