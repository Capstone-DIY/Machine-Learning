FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/ 
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
