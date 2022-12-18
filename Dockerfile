FROM python:3.8-slim

LABEL name ="slackbot-openai-pro-response" \
      version="1.0"

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the source code
COPY src /app/src

# Copy the main script
COPY main.py /app/main.py

# Set the entry point
ENTRYPOINT ["python", "main.py"]
