FROM python
WORKDIR /app
COPY ./requirements.txt ./
COPY ./gunicorn_conf.py ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:8000", "myapp:app"]
