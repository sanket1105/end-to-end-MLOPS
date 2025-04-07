FROM python:3.10

WORKDIR /app

COPY app.py .
COPY models/ ./models/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

## So app:app tells uvicorn: “Open the app.py file, and inside that file, run the app variable.”

