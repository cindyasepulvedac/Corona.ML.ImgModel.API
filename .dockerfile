# Use an official Python runtime as a parent image
FROM python:3.9.19

# Set the working directory in the container
WORKDIR /modelAPI

# Copy the current directory contents into the container at /modelAPI
COPY ./requirements.txt /modelAPI/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /modelAPI/requirements.txt

# Copy the app directory into the container at /modelAPI/app
COPY ./app /modelAPI/app

# Launch app
CMD ["fastapi", "run", "app/main.py", "--port", "5000", "--workers", "4"]
