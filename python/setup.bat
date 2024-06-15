@echo off

python -m venv venv
call venv\Scripts\activate.bat
pip install --user --upgrade pip 
@REM || (
@REM     echo Failed to upgrade pip. Retrying with elevated permissions...
@REM     runas /user:administrator "venv\Scripts\python.exe -m pip install --upgrade pip"
@REM )
pip install -r requirements.txt
pause

