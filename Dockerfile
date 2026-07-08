FROM python:3.11-slim

ADD app.py .

RUN pip install airbyte snowflake pandas

CMD ["python", "app.py"]