FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy EVERYTHING (including the templates folder)
COPY . . 
EXPOSE 8080
CMD ["python", "app.py"]