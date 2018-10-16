# Use an official Python runtime as a parent image
FROM tensorflow/tensorflow

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in pylibs.txt
# RUN pip install --upgrade pip
RUN python -m pip install --trusted-host pypi.python.org -r pylibs.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]