# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Command to run the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
