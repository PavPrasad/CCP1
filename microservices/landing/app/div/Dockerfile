# Use the official Python image as the base image
FROM python:3.8-alpine

# Copy the requirements file to the container
COPY ./app/requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install the required packages
RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Copy the app code to the container
COPY ./app /app

# Set the default command to run the app.py file
CMD ["python", "app.py"]