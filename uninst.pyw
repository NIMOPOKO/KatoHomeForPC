from ctypes import windll

def runas():

    windll.shell32.ShellExecuteW(
        None,
        "runas",
        ".\\bin\\KatoHomeForPCUnInst.exe",
        None,
        None,
        0
        )

if __name__ == "__main__":
    runas()