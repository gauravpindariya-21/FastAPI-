FROM python:3.12-slim

WORKDIR /app

COPY blog11/requirements.txt /app/blog11/requirements.txt
RUN pip install --no-cache-dir -r /app/blog11/requirements.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "src.main2:app", "--host", "0.0.0.0", "--port", "8000"]
