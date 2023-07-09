FROM python:3.9
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install libgl1 -y
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
