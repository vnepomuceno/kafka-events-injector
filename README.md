# Kafka Events Injector

## Getting Started

### Run Kafka cluster

```bash
docker-compose up -d zookeeper kafka
```

### Run consumer

```bash
poetry run python injector/consumer.py
```

```bash
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:198: key=None value=b'{"applicant_id": 1, "media": "front", "timestamp": "1637060225000"}'
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:199: key=None value=b'{"applicant_id": 1, "media": "back", "timestamp": "1637060225010"}'
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:200: key=None value=b'{"applicant_id": 1, "media": "front", "timestamp": "1637060227010"}'
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:201: key=None value=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067426000"}'
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:202: key=None value=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067428000"}'
2021-11-20 22:56:59 [__main__] <INFO> onfido_events:0:203: key=None value=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067435000"}'
```

### Run events injector

```bash
poetry run python injector/inject_events.py
```

```bash
Ξ Workspace/kafka-events-injector git:(master) ▶ poetry run python injector/inject_events.py
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: connecting to localhost:9092 [('::1', 9092, 0, 0) IPv6]
2021-11-20 22:53:15 [kafka.conn] <INFO> Probing node bootstrap-0 broker version
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connection complete.
2021-11-20 22:53:15 [kafka.conn] <INFO> Broker version identified as 2.5.0
2021-11-20 22:53:15 [kafka.conn] <INFO> Set configuration api_version=(2, 5, 0) to skip auto check_version requests on startup
2021-11-20 22:53:15 [kafka.conn] <INFO> Probing node bootstrap-0 broker version
2021-11-20 22:53:15 [kafka.conn] <INFO> Broker version identified as 2.5.0
2021-11-20 22:53:15 [kafka.conn] <INFO> Set configuration api_version=(2, 5, 0) to skip auto check_version requests on startup
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=1001 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: connecting to localhost:9092 [('::1', 9092, 0, 0) IPv6]
2021-11-20 22:53:15 [kafka.conn] <INFO> Probing node 1001 broker version
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=1001 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connection complete.
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connected> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection.
2021-11-20 22:53:15 [kafka.conn] <INFO> Broker version identified as 2.5.0
2021-11-20 22:53:15 [kafka.conn] <INFO> Set configuration api_version=(2, 5, 0) to skip auto check_version requests on startup
2021-11-20 22:53:15 [__main__] <INFO> Kafka topic onfido_events already exists
2021-11-20 22:53:15 [__main__] <INFO> Successfully created Kafka topic onfido_events
2021-11-20 22:53:15 [root] <INFO> Starting to inject Kafka events to server localhost:9092...
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: connecting to localhost:9092 [('::1', 9092, 0, 0) IPv6]
2021-11-20 22:53:15 [kafka.conn] <INFO> Probing node bootstrap-0 broker version
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connection complete.
2021-11-20 22:53:15 [kafka.conn] <INFO> Broker version identified as 2.5.0
2021-11-20 22:53:15 [kafka.conn] <INFO> Set configuration api_version=(2, 5, 0) to skip auto check_version requests on startup
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "front", "timestamp": "1637060225000"}'
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "back", "timestamp": "1637060225010"}'
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "front", "timestamp": "1637060227010"}'
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067426000"}'
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067428000"}'
2021-11-20 22:53:15 [__main__] <INFO> Sending event to KAFKA_TOPIC='onfido_events', serialized_event=b'{"applicant_id": 1, "media": "back", "timestamp": "1637067435000"}'
2021-11-20 22:53:15 [root] <INFO> Finished injecting Kafka events...
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=1001 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: connecting to localhost:9092 [('::1', 9092, 0, 0) IPv6]
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=1001 host=localhost:9092 <connecting> [IPv6 ('::1', 9092, 0, 0)]>: Connection complete.
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=bootstrap-0 host=localhost:9092 <connected> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection.
2021-11-20 22:53:15 [kafka.conn] <INFO> <BrokerConnection node_id=1001 host=localhost:9092 <connected> [IPv6 ('::1', 9092, 0, 0)]>: Closing connection.
```