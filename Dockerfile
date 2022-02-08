FROM python:3.8-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
  
CMD ["python3", "lines_task/manage.py", "runserver", "0.0.0.0:8000"]
