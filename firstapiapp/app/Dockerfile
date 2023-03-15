# docker build . -f Dockerfile -t firstapp
# docker run -p 127.0.0.1:5000:5000/tcp firstapp
# docker run --name firstapp -p 5000:5000 -d firstapp

# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose port 8000 for Flask
EXPOSE 8000

# Run the command to build the DB
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]