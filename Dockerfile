# Use lightweight Python Alpine image
FROM python:3.9-alpine

# Set maintainer label
LABEL maintainer="aaron.dm.mcdonald@gmail.com"

# Set GitHub repository label
LABEL github_repo="https://github.com/aaron-dm-mcdonald/theo-container-bingo"

# Set working directory
WORKDIR /app

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir --upgrade pip

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set the entrypoint to run the app
ENTRYPOINT ["python", "app.py"]


# CMD []
