# src

Run RUN.bat (for Windows) to create venv, install django and run server.

For Docker:
Go to the root (src) directory.
(sudo) docker build -t django-app .
(sudo) docker run -p8000:8000 django-app
