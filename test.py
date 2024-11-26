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

def get_videos_by_hashtag(hashtag_name, max_videos=2):
    videos = []
    response = api.public.hashtag(name=hashtag_name)
    
    if 'challengeInfo' in response.json() and 'challenge' in response.json()['challengeInfo']:
        hashtag_id = response.json()['challengeInfo']['challenge']['id']
        response = api.public.hashtag(id=hashtag_id)
        
        while response:
            items_list = response.json().get('itemList', [])
            video_ids = []

            for item in items_list:
                video_id = item.get('id', [])
                video_ids.append(video_id)
    return videos

def get_video_info_by_id(video_id):
    video_response = api.public.video(id=video_id)
    video_data = video_response.json()
    
    # Extract the requested video info
    video_info = {
        "video_id": video_id,
        "views": video_data.get('stats', {}).get('playCount'),
        "likes": video_data.get('stats', {}).get('diggCount'),
        "comments": video_data.get('stats', {}).get('commentCount'),
        "creation_date": video_data.get('createTime'),
        "author_username": video_data.get('author', {}).get('uniqueId'),
        "author_verified": video_data.get('author', {}).get('verified'),
        "author_followers": video_data.get('author', {}).get('followerCount'),
        "author_following": video_data.get('author', {}).get('followingCount'),
        "author_likes_count": video_data.get('author', {}).get('heartCount'),
        "author_videos_count": video_data.get('author', {}).get('videoCount'),
        "author_creation_date": video_data.get('author', {}).get('createTime')
    }
    
    return video_info

def main():
    hashtag_name = "echilibrusiverticalitate"
    max_videos = 2  # Get only the first 2 videos

    # Get video IDs by hashtag
    video_ids = get_videos_by_hashtag(hashtag_name, max_videos)
    if video_ids:
        # Fetch and print info for each video
        for video_id in video_ids:
            video_info = get_video_info_by_id(video_id)
            print(json.dumps(video_info, indent=4))
    else:
        print(f"No videos found for hashtag '{hashtag_name}'.")

if __name__ == "__main__":
    main()