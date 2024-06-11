FROM python:3.11-alpine
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
#ENTRYPOINT ["python3", "app.py"] 