FROM python:3.12-slim

WORKDIR /app

RUN pip install flask mysql-connector-python

COPY app.py /app/app.py

EXPOSE 5000

CMD ["python", "app.py"]