FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir pandas

COPY sxone_assemble.py /app

COPY entrypoint.sh /app
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
