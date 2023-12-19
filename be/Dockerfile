FROM python:3.11.2

ENV APP /app

RUN mkdir $APP

WORKDIR $APP

EXPOSE 5000

COPY ./source .

RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "/app/app.ini"]