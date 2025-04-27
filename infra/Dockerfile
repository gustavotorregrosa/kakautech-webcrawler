FROM --platform=linux/amd64 python:3

WORKDIR /usr/src/app/app

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium-driver

ENV PATH="/usr/src/app:${PATH}"

COPY ./requirements.txt ./
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

CMD [ "python", "main.py" ]