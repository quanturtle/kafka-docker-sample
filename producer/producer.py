from confluent_kafka.admin import AdminClient
from confluent_kafka import Consumer
from confluent_kafka import Producer
from sys import argv

def Produce(bootstrap_server, topic, source_data):
    p = Producer({'bootstrap.servers': bootstrap_server})

    def delivery_report(err, msg):
        if err is not None:
            print(f'There was an error: {err}')
        else:
            message = msg.value().decode('utf-8')
            print(f'{message}, {msg.topic()}, {msg.partition()}')

    for data in source_data:
        p.poll(0)
        p.produce(topic, data.encode('utf-8'), callback=delivery_report)

    r = p.flush(timeout=5)
    if 0 < r:
        print('Message delivery failed ({} message(s) still remain, did we timeout sending perhaps?)\n'.format(r))

def main():
    bootstrap_server = argv[1]
    topic = 'test_topic'

    Produce(bootstrap_server, topic, ['a', 'b', 'c', 'd', 'e'])

    return

if __name__ == '__main__':
    main()