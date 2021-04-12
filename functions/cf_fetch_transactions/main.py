import os
import requests

MONETIZZE_API_URL = os.environ.get(
    "MONETIZZE_API_URL", None
)
MONETIZZE_API_X_CONSUMER_KEY = os.environ.get(
    "MONETIZZE_API_X_CONSUMER_KEY", None
)

MONETIZZE_API_TOKEN = None


def execute(request):
    renew_token()

    return ("", 200)


def renew_token():
    url = f"{MONETIZZE_API_URL}/token"
    headers = {"X_CONSUMER_KEY": MONETIZZE_API_X_CONSUMER_KEY}

    response = requests.request("GET", url, headers=headers)
    print(f"renew_token_success: {response.json()}")
    fetch_transactions(api_token=response.json().get("token", None))


def fetch_transactions(api_token):
    url = f"{MONETIZZE_API_URL}/transactions"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "token": api_token,
    }

    response = requests.request("GET", url, headers=headers)

    print(f"fetch_transactions_success: {response.json()}")
