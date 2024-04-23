# Use Python 3.12.3 as base image
FROM python:3.12.3-slim
# Set the working directory in the container
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx xvfb \
    && rm -rf /var/lib/apt/lists/*
# Copy the current directory into the container at /app
COPY . /app
# Install required dependencies
RUN pip install -r requirements.txt
# Run the main.py file
CMD ["xvfb-run", "-s", "-screen 0 1024x768x24", "python", "main.py"]