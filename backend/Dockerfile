FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input  # Собираем статику при сборке образа
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "kittygram_backend.wsgi"]