FROM python:3.9.10-alpine3.15


RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip


WORKDIR .

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["main.py"]