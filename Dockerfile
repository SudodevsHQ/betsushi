FROM python:alpine3.14
VOLUME /tmp
RUN mkdir -p /app
RUN apk add --update gcc libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]