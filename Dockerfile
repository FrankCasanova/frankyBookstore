#Pull base image
FROM python:3.8

#Set environment variables
ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

#Set work directory
WORKDIR /code

#Isnstall dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /code/



