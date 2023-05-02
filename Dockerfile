FROM python
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "myapp:app"]
