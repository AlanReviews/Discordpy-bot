FROM python:3.10-bullseye

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV ENVIRONMENT=production

CMD ["python", "main.py"]
