##Tells Docker to use the official python 3 image from dockerhub as a base image
#FROM python:3
## Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
#ENV PYTHONUNBUFFERED 1
## Sets the container's working directory to /app
#WORKDIR /project
## Copies all files from our local project into the container
#ADD . /project
## runs the pip install command for all packages listed in the requirements.txt file
#
#RUN pip install -r requirements.txt
#
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .