@echo off
if exist venv\ (
  echo
) else (
  echo No VENV, give me a second...
  py -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  cd lines_task
  py manage.py runserver
)

pause