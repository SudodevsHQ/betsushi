FROM quay.io/basisai/python-alpine-grpcio:3.9.9-3.14-1.41.1
VOLUME /tmp
RUN mkdir -p /app
RUN apk add --update gcc build-base libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]