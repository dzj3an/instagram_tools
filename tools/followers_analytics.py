from instagrapi import Client
from datetime import datetime, timedelta

async def followers_analytics(username, password):
    """
    Asynchronous function to analyze followers and following statistics.
    """
    cl = Client()

    try:
        # Log in to Instagram
        cl.login(username, password)
        print("✅ Successfully logged in.")

        # Get the user ID of the logged-in account
        user_id = cl.user_id

        # Get the list of followers and following
        print("⏳ Fetching followers and following data...")
        followers = cl.user_followers(user_id)
        following = cl.user_following(user_id)

        # Calculate basic statistics
        total_followers = len(followers)
        total_following = len(following)
        not_following_back = len([user for user in following if user not in followers])

        # Display statistics
        print(f"📊 Total Followers: {total_followers}")
        print(f"📊 Total Following: {total_following}")
        print(f"📊 Users Not Following Back: {not_following_back}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    finally:
        # Log out of the session
        cl.logout()
        print("🔐 Successfully logged out.")