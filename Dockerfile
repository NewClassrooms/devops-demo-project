FROM python:3.10-slim-bullseye

#install security updates
RUN apt-get update && apt-get -y upgrade && apt-get -y install gcc libpq-dev

# fill out the rest of the Dockerfile to package and run demo_app
# demo_app is a Django app. Dependencies are in requirements.txt
