# Use an official Python runtime as a parent image
FROM python:3.6-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# RUN make /app
# RUN apt-get install python

# Install any needed packages specified in pylibs.txt
# RUN pip install --upgrade pip
RUN python -m pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install redis -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install cassandra-driver -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install opencv_python -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python -m pip install keras -i https://pypi.tuna.tsinghua.edu.cn/simple

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD python /app/app.py