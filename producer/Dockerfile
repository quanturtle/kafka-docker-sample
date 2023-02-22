FROM python:3.8.10-slim

# We'll add netcat cos it's a really useful
# network troubleshooting tool
RUN apt-get update

# Install the Confluent Kafka python library
RUN pip install confluent_kafka

# Add our script
ADD producer.py /
ENTRYPOINT [ "python", "/producer.py"]