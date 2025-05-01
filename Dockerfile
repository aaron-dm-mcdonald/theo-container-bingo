# Use lightweight Python Alpine image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install dependencies
# Install pip dependencies and build tools for any compiled wheels (like rich)
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir --upgrade pip

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose a port (not required for CLI games, but kept if needed for UI later)
EXPOSE 80

# Default command
CMD ["python", "app.py"]
