import boto3
import json
import os

import requests
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.metrics import MetricUnit

BUCKET_NAME = os.environ["BUCKET_NAME"]

logger = Logger()
tracer = Tracer()
metrics = Metrics()

s3_client = boto3.client("s3")


@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def handle_event(event, context):
    logger.info(f"Request received")

    # Retrieve some random advice from a helpful API
    response = requests.get("https://api.adviceslip.com/advice")
    slip = response.json()["slip"]
    if response.status_code == 200:
        metrics.add_metric(name="SuccessCount", unit=MetricUnit.Count, value=1)
        result = {
            "advice_slip": slip,
            "generated_by_request_id": context.aws_request_id
        }
        s3_client.put_object(Bucket=BUCKET_NAME,
                             Key="latest_advice.json", Body=json.dumps(result))
        return result
    else:
        logger.error(f"Failed to get advice",  extra={
                     "status_code": response.status_code, "text": response.text})
        raise Exception(
            f"Failed to get advice with status code {response.status_code}, message {response.text}")
