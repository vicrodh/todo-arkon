FROM python:3.10.2
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements.txt ./
RUN apt update && apt -y install gettext
RUN /usr/local/bin/python -m pip install --upgrade pip \
 && pip install -r requirements.txt
COPY . ./
EXPOSE 8000
