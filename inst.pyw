from ctypes import windll

def runas():

    windll.shell32.ShellExecuteW(
        None,
        "runas",
        "C:\\Users\\nimon\\Desktop\\valorant app\\KatoHome\\bin\\KatoHomeForPC.exe",
        None,
        None,
        0
        )

if __name__ == "__main__":
    runas()