FROM python
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp:app"]
