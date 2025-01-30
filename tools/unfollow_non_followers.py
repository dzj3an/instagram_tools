from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError

async def unfollow_non_followers(username, password):
    """
    Asynchronous function that takes an Instagram username and password,
    logs in, and unfollows users who do not follow back.

    Args:
        username (str): Instagram username.
        password (str): Instagram password.

    Returns:
        None
    """
    # Initialize the Instagram client
    cl = Client()

    try:
        # Log in to Instagram
        cl.login(username, password)
        print("✅ Successfully logged in.")  # Mensaje cuando inicia sesión

        # Get the user ID of the logged-in account
        user_id = cl.user_id

        # Get the list of users the account is following
        print("⏳ Fetching the list of users you are following...")  # Mensaje cuando obtiene seguidos
        following = cl.user_following(user_id)
        print(f"📋 You are following {len(following)} users.")  # Mensaje con el número de seguidos

        # Get the list of users following the account
        print("⏳ Fetching the list of users following you...")  # Mensaje cuando obtiene seguidores
        followers = cl.user_followers(user_id)
        print(f"📋 You have {len(followers)} followers.")  # Mensaje con el número de seguidores

        # Identify users who are not following back
        not_following_back = [user for user in following if user not in followers]
        print(f"🔍 Found {len(not_following_back)} users not following you back.")  # Mensaje con el número de usuarios que no siguen de vuelta

        # Unfollow users who are not following back
        for user in not_following_back:
            try:
                cl.user_unfollow(user)
                print(f"❌ Unfollowed {following[user].username}")  # Mensaje cuando deja de seguir
            except ClientError as e:
                # Solo maneja el error sin imprimir nada
                pass

    except LoginRequired as e:
        print("🔒 Login failed. Please check your credentials.")  # Mensaje de error al iniciar sesión
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")  # Mensaje de error inesperado
    finally:
        # Log out of the session
        cl.logout()
        print("🔐 Successfully logged out.")  # Mensaje cuando cierra sesión