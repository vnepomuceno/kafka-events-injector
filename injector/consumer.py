import logging

from kafka import KafkaConsumer

from inject_events import get_logger

logger = get_logger(__name__)

consumer = KafkaConsumer(
    "onfido_events", group_id="my-group", bootstrap_servers=["localhost:9092"]
)
for message in consumer:
    consumer.commit()
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    logger.info(
        "%s:%d:%d: key=%s value=%s"
        % (message.topic, message.partition, message.offset, message.key, message.value)
    )
