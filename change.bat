@rem ファイル名の一部を削除するバッチファイル
echo off
for %%f in ( * ) do call :sub "%%f"
exit /b

:sub
set fname=%1
set fname=%fname:ここに削除する文字を記載=""%
ren %1 %fname%
goto :EOF
