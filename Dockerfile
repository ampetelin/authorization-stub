FROM python:3.12-alpine

WORKDIR /authorization-stub
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "wsgi.py"]