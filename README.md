# KatoHomeForPC
EXEをスタートアップに設定することで、最速で配信リンクが表示されます。
setup.pyはexe化出来なかったので自分でビルドしてください。ビルドできない場合はスタートアップにkatohome.exeを追加してください。

# インストール
```
pip install  -r requirements.txt
```
# ビルド
```
pyinstaller .\katohome.py --icon=kato.ico --onefile
```
