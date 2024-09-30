# Use an official Python runtime as a parent image
FROM python:3.9.19-slim

# Set the working directory in the container
WORKDIR /modelapi

# Copy the current directory contents into the container at /modelAPI
COPY ./requirements.txt /modelapi/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /modelapi/requirements.txt

# Copy the app directory into the container at /modelAPI/app
COPY ./ /modelapi/

# Launch app
CMD ["fastapi", "run", "main.py", "--port", "5000", "--workers", "4"]
