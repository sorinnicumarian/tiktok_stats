import tikapi
import pandas as pd
from datetime import datetime
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
        
        # Initialize a counter for the videos
        video_count = 0
        
        while response and video_count < max_videos:
            items_list = response.json().get('itemList', [])

            for item in items_list:
                video_id = item.get('id')
                if video_id:
                    videos.append(video_id)
                    video_count += 1  # Increment the video count
                    if video_count >= max_videos:
                        break  # Stop if we've reached the max_videos limit
            if video_count < max_videos:
                # Fetch next page of results if there are more videos
                response = api.public.hashtag(id=hashtag_id, cursor=response.json().get('cursor'))
            else:
                break  # Exit while loop once we have enough videos

    return videos

def get_video_info_by_id(video_id):
    video_response = api.public.video(id=video_id)
    video_data = video_response.json()

    video_info = {
        "video_id": video_id,
        "views": video_data.get('itemInfo', {}).get('itemStruct', {}).get('stats', {}).get('playCount'),
        "likes": video_data.get('itemInfo', {}).get('itemStruct', {}).get('stats', {}).get('diggCount'),
        "comments": video_data.get('itemInfo', {}).get('itemStruct', {}).get('stats', {}).get('commentCount'),
        "isAd": video_data.get('itemInfo', {}).get('itemStruct', {}).get('isAd'),
        "creation_date": video_data.get('itemInfo', {}).get('itemStruct', {}).get('createTime'),
        "shareCount": video_data.get('itemInfo', {}).get('itemStruct', {}).get('stats', {}).get('shareCount'),
        "author_username": video_data.get('itemInfo', {}).get('itemStruct', {}).get('author', {}).get('uniqueId'),
        "author_verified": video_data.get('itemInfo', {}).get('itemStruct', {}).get('author', {}).get('verified'),
        "author_followers_count": video_data.get('itemInfo', {}).get('itemStruct', {}).get('authorStats', {}).get('followerCount'),
        "author_following_count": video_data.get('itemInfo', {}).get('itemStruct', {}).get('authorStats', {}).get('followingCount'),
        "author_friend_count": video_data.get('itemInfo', {}).get('itemStruct', {}).get('authorStats', {}).get('friendCount'),
        "author_heart_count": video_data.get('itemInfo', {}).get('itemStruct', {}).get('authorStats', {}).get('heartCount'),
        "author_video_count": video_data.get('itemInfo', {}).get('itemStruct', {}).get('authorStats', {}).get('videoCount')
    }

    # Convert timestamp to human-readable format
    creation_timestamp = video_info["creation_date"]
    if creation_timestamp:
        video_info["creation_date"] = datetime.utcfromtimestamp(creation_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    return video_info

def save_to_csv(video_data, file_name="tiktok_data.xlsx"):
    if not video_data:
        print("No data to save.")
        return

    # Convert video data into a pandas DataFrame for easy manipulation
    df_videos = pd.DataFrame(video_data)

    # Save the DataFrame to an Excel file
    df_videos.to_excel(file_name, index=False, sheet_name="Videos")

    print(f"Data saved to {file_name}")

def main():
    hashtag_name = "echilibrusiverticalitate"
    max_videos = 1  # Adjust to get more videos if needed

    # Get video IDs by hashtag
    video_ids = get_videos_by_hashtag(hashtag_name, max_videos)
    
    video_data = []

    if video_ids:
        # Fetch and store info for each video
        for video_id in video_ids:
            video_info = get_video_info_by_id(video_id)
            video_data.append(video_info)
            print(json.dumps(video_info, indent=4))
        
        # Save collected video data to a CSV/Excel file
        save_to_csv(video_data, file_name="tiktok_video_data.xlsx")
    else:
        print(f"No videos found for hashtag '{hashtag_name}'.")

if __name__ == "__main__":
    main()