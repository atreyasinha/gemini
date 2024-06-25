FROM python:slim-bullseye

# Set working directory
WORKDIR /app 

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy script
COPY alerts.py .

# Run script
CMD ["python", "alerts.py"]