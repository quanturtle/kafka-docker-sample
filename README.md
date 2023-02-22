# kafka-docker-sample
## What's inside
Sample docker compose app, consists of 4 services:
* `zookeeper`: centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services
* `kafka` (broker): distributed event streaming platform
* `consumer`: python script that connects to the broker and consumes queue
* `producer`: python script that connects to the broker and produces a series of messages

### get the project
Clone it
```
git clone git@github.com:quanturtle/kafka-docker-sample.git
```

Run it
```
docker compose up --build
```

`zookeper` starts
```
zookeeper  | ===> User
zookeeper  | uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)
zookeeper  | ===> Configuring ...
```

`kafka` broker starts
```
broker     | ===> User
broker     | uid=0(root) gid=0(root) groups=0(root)
broker     | ===> Configuring ...
```

`consumer` and `producer` start
```
producer   | Giving Kafka a bit of time to start up…
consumer   | Giving Kafka a bit of time to start up…
```

after `consumer` is ready, `producer` should send 5 messages
```
producer   | a, test_topic, 0
producer   | b, test_topic, 0
producer   | c, test_topic, 0
producer   | d, test_topic, 0
producer   | e, test_topic, 0
producer exited with code 0
```

that should be received by `consumer`
```
consumer   | Message received: "a" from topic test_topic
consumer   |
consumer   | Message received: "b" from topic test_topic
consumer   |
consumer   | Message received: "c" from topic test_topic
consumer   |
consumer   | Message received: "d" from topic test_topic
consumer   |
consumer   | Message received: "e" from topic test_topic
consumer   |
consumer exited with code 0
```