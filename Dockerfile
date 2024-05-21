FROM python:3.11.3-alpine

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python","-u","kome_auto.py"]