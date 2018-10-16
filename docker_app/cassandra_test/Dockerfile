# Use an official Python runtime as a parent image
FROM cassandra

# Install any needed packages specified in requirements.txt
RUN cassandra

# Make port 80 available to the world outside this container
EXPOSE 9042

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]