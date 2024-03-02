FROM python:3.11

RUN mkdir -p /root/server

WORKDIR /root/server

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py"]