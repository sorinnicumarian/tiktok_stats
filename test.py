import tikapi
import pandas as pd
from datetime import datetime, timedelta
import json
from tikapi import TikAPI, ValidationException, ResponseException


def load_config(config_file="config.json"):
    with open(config_file, 'r') as f:
        return json.load(f)

config = load_config()  # Load config data
api = tikapi.TikAPI(config["tikapi_key"])

def get_videos_by_id(id):
    try:
        response = api.public.video(
            id=id
        )

        print(response.json())

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)

def get_videos_by_hashtag():
    try:
        response = api.public.hashtag(
            name="echilibrusiverticalitate"
        )

        hashtagId = response.json()['challengeInfo']['challenge']['id']

        response = api.public.hashtag(
            id=hashtagId
        )

        print(response.json())

        while(response):
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)
            response = response.next_items()
            

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)

get_videos_by_id("7003402629929913605")