FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY common.py .
COPY data_json.py .
COPY discord_poster.py .
COPY version_checker.py .
COPY main.py .
COPY entrypoint.sh .
RUN chmod 0700 ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
