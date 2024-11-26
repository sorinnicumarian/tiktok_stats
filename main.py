import asyncio
import tikapi
import pandas as pd
from datetime import datetime, timedelta
import sys
import json

def load_config(config_file="config.json"):
    with open(config_file, 'r') as f:
        return json.load(f)

# Function to fetch videos by hashtag
async def get_videos_by_hashtag(hashtag, count=100, days=7):
    # Initialize the TikAPI client with your credentials
    config = load_config()  # Load config data
    client = tikapi.TikAPI(config["tikapi_key"])

    try:
        # Fetch videos related to a hashtag
        response = await client.hashtag(hashtag).videos(count=count)  # Get videos by hashtag

        # Convert async generator to a list
        video_data = []
        async for video in response:
            video_info = video.as_dict
            stats = video_info.get('stats', {})
            author_info = video_info.get('author', {})

            # Only add videos that are within the time limit
            time_limit = datetime.now() - timedelta(days=days)
            create_time = datetime.utcfromtimestamp(video_info.get('createTime', 0))
            if create_time >= time_limit:
                video_data.append({
                    "video_id": video_info.get('id', ''),
                    "description": video_info.get('desc', ''),
                    "likes": stats.get('diggCount', 0),
                    "comments": stats.get('commentCount', 0),
                    "shares": stats.get('shareCount', 0),
                    "views": stats.get('playCount', 0),
                    "create_time": create_time,
                    "author_id": author_info.get('id', ''),
                    "author_username": author_info.get('uniqueId', ''),
                    "author_nickname": author_info.get('nickname', ''),
                    "author_verified": author_info.get('verified', False),
                    "author_followers": author_info.get('stats', {}).get('followerCount', 0),
                    "author_following": author_info.get('stats', {}).get('followingCount', 0),
                    "author_likes": author_info.get('stats', {}).get('heartCount', 0),
                    "author_videos": author_info.get('stats', {}).get('videoCount', 0),
                    "author_creation_date": author_info.get('createTime', 0),
                })

        # Check if no videos were returned
        if len(video_data) == 0:
            print("stopped")
            sys.exit(0)  # Exit the program gracefully

        return video_data

    except Exception as e:
        print(f"Error fetching videos: {e}")
        return []

# Save data to CSV
def save_to_csv(video_data, file_name="tiktok_data.xlsx"):
    if not video_data:
        print("No data to save.")
        return

    # First sheet: Overview statistics
    authors = {v['author_id']: v for v in video_data}.values()
    overview_data = {
        "Total Videos": len(video_data),
        "Total Accounts": len(authors),
        "Average Followers": sum(a["author_followers"] for a in authors) / len(authors),
        "Average Likes": sum(a["author_likes"] for a in authors) / len(authors),
    }

    # Prepare data for sheets
    df_videos = pd.DataFrame(video_data)
    df_accounts = pd.DataFrame(authors)
    df_overview = pd.DataFrame([overview_data])

    # Write to Excel
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
        df_overview.to_excel(writer, index=False, sheet_name="Overview")
        df_accounts.to_excel(writer, index=False, sheet_name="Accounts")
        df_videos.to_excel(writer, index=False, sheet_name="Videos")

    print(f"Data saved to {file_name}")

# Main execution
async def main():
    HASHTAG = "test"  # Replace with your desired hashtag
    TOTAL_VIDEOS_COUNT = 1  # Fetch this many videos
    DAYS = 7  # Fetch videos from the last 7 days
    videos = await get_videos_by_hashtag(HASHTAG, count=TOTAL_VIDEOS_COUNT, days=DAYS)
    save_to_csv(videos, file_name="tiktok_stats.xlsx")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())