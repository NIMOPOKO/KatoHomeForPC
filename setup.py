import comtypes.client
import os

#リンク先のファイル名
target_file=os.path.join(os.path.dirname(__file__), "katohome.exe")
#ショートカットを作成するパス
save_path=os.path.join(os.path.dirname(__file__),"C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\katohome.lnk")
#WSHを生成
wsh=comtypes.client.CreateObject("wScript.Shell",dynamic=True)
#ショートカットの作成先を指定して、ショートカットファイルを開く。作成先のファイルが存在しない場合は、自動作成される。
short=wsh.CreateShortcut(save_path)
#以下、ショートカットにリンク先やコメントといった情報を指定する。
#リンク先を指定
short.TargetPath=target_file
#コメントを指定する
short.Description="katohomeショートカット"
#引数を指定したい場合は、下記のコメントを解除して、引数を指定する。
#short.arguments="/param1"
#アイコンを指定したい場合は、下記のコメントを解除してアイコンのパスを指定する。
#short.IconLocation="C:\\test\\test.ico"
#作業ディレクトリを指定したい場合は、下記のコメントを解除してディレクトリのパスを指定する。
#short.workingDirectory="c:\\test\\"
#ショートカットファイルを作成する
short.Save()