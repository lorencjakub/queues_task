@echo off
if exist venv\ (
  .\venv\Scripts\activate
  cd lines_task
  py manage.py runserver
) else (
  echo No VENV, give me a second...
  py -m venv venv
  .\venv\Scripts\activate
  echo Updating pip...
  python -m pip install --upgrade pip
  REM pip install -r requirements.txt
  pip install django==3.2.12
  cd lines_task
  py manage.py runserver
)

pause