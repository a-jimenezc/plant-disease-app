FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements_app.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
