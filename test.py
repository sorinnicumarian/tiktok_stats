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

def get_videos_by_hashtag(hashtag_name):

    response = api.public.hashtag(name=hashtag_name)
    hashtag_id = response.json()['challengeInfo']['challenge']['id']
    response = api.public.hashtag(id=hashtag_id)

    while(response):
        cursor = response.json().get('cursor')
        response = response.next_items()

def get_video_info_by_id(video_id):
    video_response = api.public.video(id=video_id)
    #TODO write code to get the following info: video number of views, likes, comments, creation date, author_username, author_verified, author_followers, author_following, author_likes_count, author_videos_count, author_creation_date
    return 

#TODO write code for a main function
#TODO get only the first 2 videos
get_videos_by_hashtag("echilibrusiverticalitate")