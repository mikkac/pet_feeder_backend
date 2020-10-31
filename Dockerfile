FROM tiangolo/uwsgi-nginx-flask:python3.8

EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3", "python/server.py" ]