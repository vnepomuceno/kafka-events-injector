import logging
from dataclasses import dataclass
from json import dumps

import coloredlogs
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

KAFKA_HOST = "localhost"
KAFKA_PORT = "9092"
KAFKA_TOPIC = "onfido_events"


def get_logger(name: str) -> logging.Logger:
    coloredlogs.install()
    custom_logger = logging.getLogger(name)
    coloredlogs.install(
        level="INFO",
        logger=custom_logger,
        fmt="%(asctime)s [%(name)s] <%(levelname)s> %(message)s",
    )

    return custom_logger


logger = get_logger(__name__)


@dataclass
class ApplicantUpload:
    applicant_id: int
    media: str
    timestamp: str


def read_csv_events():
    with open("injector/resources/input_data.csv") as csvfile:
        csv_records = csvfile.readlines()
        return [
            ApplicantUpload(
                applicant_id=int(record.split(",")[0]),
                media=record.split(",")[1],
                timestamp=record.split(",")[2].strip(),
            )
            for record in csv_records
        ]


def create_kafka_topic():
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")
    topic_list = [NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1)]
    try:
        admin_client.create_topics(topic_list)
    except TopicAlreadyExistsError:
        logger.info(f"Kafka topic {KAFKA_TOPIC} already exists")

    logger.info(f"Successfully created Kafka topic {KAFKA_TOPIC}")


def main():
    kafka_server = f"{KAFKA_HOST}:{KAFKA_PORT}"

    create_kafka_topic()

    logging.info(f"Starting to inject Kafka events to server {kafka_server}...")
    producer = KafkaProducer(bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"])

    applicant_uploads = read_csv_events()
    for upload in applicant_uploads:
        serialized_event = dumps(upload, default=lambda o: o.__dict__).encode("utf-8")
        logger.info(f"Sending event to {KAFKA_TOPIC=}, {serialized_event=}")
        producer.send(topic=KAFKA_TOPIC, value=serialized_event)

    logging.info("Finished injecting Kafka events...")


if __name__ == "__main__":
    main()
