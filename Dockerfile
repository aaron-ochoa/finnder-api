FROM python:3

WORKDIR /usr/src/finnder

COPY . .

RUN pip install -r requirements.txt

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "api:app" ]
