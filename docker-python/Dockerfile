# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /var/docker-python

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./test.py" ]
