# First base image (host OS)
from python:3.8.9

# Working Directory
WORKDIR /code

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content to local folder to the working directory
COPY . /code

# Run the application
CMD ["python3", "main.py"]