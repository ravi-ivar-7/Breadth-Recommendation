FROM python:3.11

# RUN mkdir -p /root/<app-name>
WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["npm", "start", "app.js"]

# RUN only runs once and then stops, while cmd runs cont.

# docker build -t django-docker .  # building image
# docker image ls -a 
# docker run -p 8000:8000 django-docker  # running container
# docker ps -a # to check container running status
# docker exec I-ls ........  # to go inside docker 

#  docker prune -a  # to delete unnecessary files

# docker run -p 8000:8000 -d django-docker  # to run in background without this sorce code 