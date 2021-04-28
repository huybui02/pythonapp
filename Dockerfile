FROM python:3.9

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "./src/server.py" ]