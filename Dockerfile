FROM python:3.9-slim

WORKDIR /build

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r build/requirements.txt

EXPOSE 8080


ENTRYPOINT ["sh", "run.sh"]