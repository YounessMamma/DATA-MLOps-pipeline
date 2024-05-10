from dagster import resource, Field, String
from confluent_kafka import Consumer
import os

# @resource(config_schema={
#     "bootstrap_servers": Field(String, description="Kafka broker addresses", default_value="my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092"),
#     "group_id": Field(String, description="Consumer group ID", default_value="my_consumer_group"),
#     "topic_name": Field(String, description="Kafka topic name", default_value="test_topic")
# })
# def kafka_consumer_resource(context):
#     bootstrap_servers = context.resource_config["bootstrap_servers"]
#     group_id = context.resource_config["group_id"]
#     topic_name = context.resource_config["topic_name"]

#     consumer = Consumer({
#       'bootstrap.servers': bootstrap_servers,
#       'group.id': group_id,
#       'topic_name': topic_name,
#       'auto.offset.reset': 'earliest'  
#   })

#     return consumer


@resource(config_schema={
    "bootstrap_servers": Field(String, description="Kafka broker addresses", default_value="kafka:9092"),
    "group_id": Field(String, description="Consumer group ID", default_value="my_consumer_group"),
    "input_topic_name": Field(String, description="Kafka Input topic name", default_value="test_topic"), 
    "output_topic_name": Field(String, description="Kafka Output topic name", default_value="transformed_data") 
})
def kafka_consumer_resource(context):

    bootstrap_servers = context.resource_config["bootstrap_servers"]
    group_id = context.resource_config["group_id"]
    input_topic_name = context.resource_config["input_topic_name"]
    output_topic_name = context.resource_config["output_topic_name"] # Handle optional parameter

    consumer_config = {
        "bootstrap.servers": bootstrap_servers,
        "group.id": group_id,
        "auto.offset.reset": "earliest",
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe([input_topic_name])  # Subscribe to the input topic

    return consumer