FROM python:latest

COPY . /app-home

RUN pip install -r /app-home/requirements.txt

EXPOSE 8080

CMD  ["python",  "/app-home/app.py"]
