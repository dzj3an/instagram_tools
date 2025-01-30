from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientJSONDecodeError
import json
async def profile_scraper(username, insta_username, insta_password):
    """
    Function to scrape public profile information from Instagram.
    Requires Instagram credentials to avoid login_required errors.
    """
    cl = Client()

    try:
        # Log in to Instagram
        cl.login(insta_username, insta_password)
        print("✅ Successfully logged in.")

        # Get public profile information
        print("⏳ Fetching profile information...")
        try:
            profile = cl.user_info_by_username(username)
        except ClientJSONDecodeError:
            # Silently handle JSONDecodeError
            pass

        # Display profile information
        print(f"📊 Username: {profile.username}")
        print(f"📊 Full Name: {profile.full_name}")
        print(f"📊 Biography: {profile.biography}")
        print(f"📊 Posts: {profile.media_count}")
        print(f"📊 Followers: {profile.follower_count}")
        print(f"📊 Following: {profile.following_count}")
        print(f"📊 Profile Picture URL: {profile.profile_pic_url}")

    except LoginRequired as e:
        print("🔒 Login failed. Please check your credentials.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    finally:
        # Log out of the session
        cl.logout()
        print("🔐 Successfully logged out.")