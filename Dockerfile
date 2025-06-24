FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app/backend
WORKDIR /app/backend
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
