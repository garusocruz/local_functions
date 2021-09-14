
from pubsub import GCloudPubSub

import json
import os
import requests

MONETIZZE_API_URL = os.environ.get("MONETIZZE_API_URL", None)
MONETIZZE_API_X_CONSUMER_KEY = os.environ.get("MONETIZZE_API_X_CONSUMER_KEY", None)


def callback(message_future):
    queued = False
    message_future.exception(timeout=10)
    while message_future.running():
        print('running.')
    queued = True
    return queued


def execute():
    if request.method == "POST":
        try:
            request_json = request.get_json()
        except Exception:
            request_json = None

        token = renew_token(request_json=request_json)
        transactions = fetch_transactions(api_token=token, request_json=request_json)
        publish_message(message=transactions)
        return transactions


def publish_message(message):
    topic_name = "pub_transactions"
    publisher = GCloudPubSub()
    topic = publisher.client.topic_path(publisher.project_id, topic_name)
    message = dict(message)

    message_future = publisher.client.publish(
        topic, data=json.dumps(message).encode("UTF-8")
    )
    message_future.add_done_callback(callback)

def renew_token(request_json):
    try:
        url = f"{MONETIZZE_API_URL}/token"
        headers = {"X_CONSUMER_KEY": MONETIZZE_API_X_CONSUMER_KEY}

        response = requests.request("GET", url, headers=headers)
        print(f"renew_token_success: {response.json()}")
        return response.json().get("token", None)

    except Exception:
        return False


def compose_url(url, request_json):
    for item in request_json:
        url = f"{url}?{item}={request_json[item]}&"
    return url[:-1]


def fetch_transactions(api_token, request_json):
    try:
        url = f"{MONETIZZE_API_URL}/transactions"
        if request_json:
            url = compose_url(url=url, request_json=request_json)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "token": api_token,
        }

        response = requests.request("GET", url[:-1], headers=headers)

        print(f"fetch_transactions_success: {response.json()}")
        return response.json()

    except Exception:
        return False