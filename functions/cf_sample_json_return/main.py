from flask import app, request
import os
import requests


def execute():
    if request.method == "GET":
        DEFAULT_JSON_RETURN = os.environ.get("DEFAULT_JSON_RETURN", None)
        return DEFAULT_JSON_RETURN

    return False
