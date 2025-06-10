FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /authorization-stub

COPY authorization-stub .

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

CMD ["waitress-serve", "--listen=0.0.0.0:5000", "app:app"]