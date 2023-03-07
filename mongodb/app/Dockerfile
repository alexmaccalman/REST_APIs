
# docker build . -f Dockerfile -t mapapp
# docker run -p 127.0.0.1:5000:5000/tcp mapapp
# docker run --name mapappls -p 5000:5000 -d mapapp

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

# Expose port 5000 for Flask
EXPOSE 5000

# Run the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]