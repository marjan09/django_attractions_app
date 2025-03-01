# Use the latest official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    npm \
    && apt-get clean

# Copy the project files first (before installing dependencies)
COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Tailwind dependencies
WORKDIR /app/theme

RUN python /app/manage.py tailwind install
RUN npm install --prefix /app/theme/static_src

# Run migrations
WORKDIR /app
RUN python manage.py migrate

# Build Tailwind CSS
RUN python manage.py tailwind build

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]