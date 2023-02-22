from confluent_kafka.admin import AdminClient
from confluent_kafka import Consumer
from confluent_kafka import Producer
from sys import argv
from datetime import datetime

topic='test_topic'

def Consume(bootstrap_server, topic):
    c = Consumer({
        'bootstrap.servers': bootstrap_server,
        'group.id': 'rmoff',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe([topic])
    
    try:
        msgs = c.consume(num_messages=10, timeout=30)

        if len(msgs) == 0:
            print("No message(s) consumed (maybe we timed out waiting?)\n")
        else:
            for msg in msgs:
                message = msg.value().decode('utf-8')
                print(f'Message received: "{message}" from topic {msg.topic()}\n')
    except Exception as e:
        print("Consumer error: {}\n".format(e))
    
    c.close()


def main():
    bootstrap_server = argv[1]
    topic = 'test_topic'

    Consume(bootstrap_server, topic)

    return

if __name__ == '__main__':
    main()