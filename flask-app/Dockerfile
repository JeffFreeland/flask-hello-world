FROM python:alpine3.7

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY index.py /app

COPY config_file.txt .

EXPOSE 5000

CMD ["python",  "index.py"]