import pandas as pd
from TikTokApi import TikTokApi
from datetime import datetime, timedelta

# Initialize TikTok API
api = TikTokApi()

def get_videos_by_hashtag(hashtag, days=30):
    """
    Get videos for a specific hashtag in the last 'days' days.
    """
    print(f"Fetching videos for hashtag: #{hashtag}")
    videos = api.by_hashtag(hashtag, count=200)  # Fetch the top 200 videos
    filtered_videos = []
    
    # Filter videos by creation date
    time_limit = datetime.now() - timedelta(days=days)
    for video in videos:
        create_time = datetime.fromtimestamp(video['createTime'])
        if create_time >= time_limit:
            filtered_videos.append({
                "Video ID": video['id'],
                "Author": video['author']['uniqueId'],
                "Creation Date": create_time,
                "Likes": video['stats']['diggCount'],
                "Shares": video['stats']['shareCount'],
                "Comments": video['stats']['commentCount'],
                "Views": video['stats']['playCount'],
            })
    print(f"Found {len(filtered_videos)} videos in the last {days} days.")
    return filtered_videos

def analyze_accounts(videos):
    """
    Analyze accounts that shared the videos.
    """
    accounts = {}
    for video in videos:
        author = video["Author"]
        if author not in accounts:
            accounts[author] = {
                "First Post Date": video["Creation Date"],
                "Total Videos": 0,
                "Total Likes": 0,
                "Total Shares": 0,
                "Total Comments": 0,
                "Total Views": 0,
            }
        accounts[author]["Total Videos"] += 1
        accounts[author]["Total Likes"] += video["Likes"]
        accounts[author]["Total Shares"] += video["Shares"]
        accounts[author]["Total Comments"] += video["Comments"]
        accounts[author]["Total Views"] += video["Views"]
    return accounts

def generate_statistics(accounts):
    """
    Generate overview statistics for accounts.
    """
    total_accounts = len(accounts)
    total_first_posts = [account["First Post Date"] for account in accounts.values()]
    avg_creation_date = sum([post_date.timestamp() for post_date in total_first_posts]) / len(total_first_posts)
    avg_creation_date = datetime.fromtimestamp(avg_creation_date)
    
    # Bot detection heuristic: accounts with low engagement and high frequency
    suspected_bots = [
        account for account, details in accounts.items()
        if details["Total Videos"] > 10 and (details["Total Likes"] / details["Total Videos"]) < 10
    ]
    
    return {
        "Total Accounts": total_accounts,
        "Average Creation Date": avg_creation_date,
        "Suspected Bots": len(suspected_bots),
    }

def export_to_csv(videos, accounts, stats, output_file="TikTok_Analysis.xlsx"):
    """
    Export data to an Excel file with multiple sheets.
    """
    # Sheet 1: Overview statistics
    overview_df = pd.DataFrame([stats])
    
    # Sheet 2: Account details
    accounts_df = pd.DataFrame.from_dict(accounts, orient="index").reset_index()
    accounts_df.rename(columns={"index": "Account"}, inplace=True)
    
    # Sheet 3: Video details
    videos_df = pd.DataFrame(videos)
    
    # Write to Excel
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        overview_df.to_excel(writer, sheet_name="Overview", index=False)
        accounts_df.to_excel(writer, sheet_name="Accounts", index=False)
        videos_df.to_excel(writer, sheet_name="Videos", index=False)
    print(f"Data exported to {output_file}")

# Main Execution
HASHTAG = "echilibrusiverticalitate"
DAYS = 30

# Step 1: Get videos by hashtag
videos = get_videos_by_hashtag(HASHTAG, days=DAYS)

# Step 2: Analyze accounts
accounts = analyze_accounts(videos)

# Step 3: Generate statistics
stats = generate_statistics(accounts)

# Step 4: Export to CSV
export_to_csv(videos, accounts, stats)