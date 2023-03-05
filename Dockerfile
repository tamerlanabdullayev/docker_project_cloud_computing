FROM python:3.10-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt
COPY /home/data /home/data
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py"]