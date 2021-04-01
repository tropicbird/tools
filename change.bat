echo off
for %%f in ( * ) do call :sub "%%f"
exit /b

:sub
set fname=%1
set fname=%fname:Mesh1km3dim2016_SetaiThresh025_=""%
ren %1 %fname%
goto :EOF