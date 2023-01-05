FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk add python3-dev \
                        gcc \
                        g++ \
                        postgresql-dev \
                        libc-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]