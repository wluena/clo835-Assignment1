# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file and install them
# Ensure you have a requirements.txt in the webapp folder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port (typically 8080 or 5000)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]