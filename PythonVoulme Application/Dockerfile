# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY store.py /app/

# Create a directory for storing persistent data
VOLUME /app/data

# Set the command to run the Python script
CMD ["python", "store.py"]
