# First base image (host OS)
from python:3.8.9

# Working Directory
WORKDIR /code

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the content to local folder to the working directory
COPY . /code

# Run the application
CMD ["python3", "main.py"]


##### NOTE TO DO AFTER BUILDING THE IMAGE #####

# Then build the container with this comand 
# docker build -t tecfanbot .

# Then run the container with this command
# docker run -it tecfanbot 