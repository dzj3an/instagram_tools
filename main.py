import asyncio
import os
import platform
from colorama import Fore, Style, init
from tools import unfollow_non_followers
from tools import followers_analytics
from tools import profile_scraper

# Initialize colorama for colored text
init(autoreset=True)

def clear_console():
    """Clear the console screen (works on both Windows and Linux)."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

async def main():
    """
    Main function to interact with the user and execute the selected tool.
    """
    # Clear the console at the beginning
    clear_console()

    # Display a welcome message with colors
    print(Fore.CYAN + "🌟 Welcome to Instagram Tools! 🌟")
    print(Fore.YELLOW + "Created by: " + Fore.GREEN + "dzj3an (GitHub)")
    print(Style.RESET_ALL + "-" * 40)
    print("Please select the tool you want to use:\n")

    # Display available tools
    print(Fore.MAGENTA + "1. Unfollow Non-Followers")
    print(Fore.MAGENTA + "2. Followers/Following Analytics")
    print(Fore.MAGENTA + "3. Public Profile Scraper")
    print(Style.RESET_ALL + "-" * 40)

    # Get the user's choice
    choice = input(Fore.BLUE + "Enter the number of your choice: " + Style.RESET_ALL)
    clear_console()

    if choice == "1":

        # Get Instagram credentials
        print(Fore.CYAN + "🚀 Starting the Unfollow Non-Followers tool...\n")
        username = input(Fore.BLUE + "Enter your Instagram username: " + Style.RESET_ALL)
        password = input(Fore.BLUE + "Enter your Instagram password: " + Style.RESET_ALL)
        
        clear_console()
        print(Fore.CYAN + "🚀 Starting the Unfollow Non-Followers tool...\n")

        # Execute the unfollow tool
        await unfollow_non_followers(username, password)

    elif choice == "2":

        # Get Instagram credentials
        print(Fore.CYAN + "🚀 Starting the Followers/Following Analytics tool...\n")
        username = input(Fore.BLUE + "Enter your Instagram username: " + Style.RESET_ALL)
        password = input(Fore.BLUE + "Enter your Instagram password: " + Style.RESET_ALL)
        clear_console()
        print(Fore.CYAN + "🚀 Starting the Followers/Following Analytics tool...\n")

        # Execute the analytics tool
        await followers_analytics(username, password)

    elif choice == "3":
        clear_console()

        # Get Instagram credentials and target username
        print(Fore.CYAN + "🚀 Starting the Public Profile Scraper tool...\n")
        insta_username = input(Fore.BLUE + "Enter your Instagram username: " + Style.RESET_ALL)
        insta_password = input(Fore.BLUE + "Enter your Instagram password: " + Style.RESET_ALL)
        target_username = input(Fore.BLUE + "Enter the target Instagram username: " + Style.RESET_ALL)
        clear_console()
        print(Fore.CYAN + "🚀 Starting the Public Profile Scraper tool...\n")

        # Execute the profile scraper tool
        await profile_scraper(target_username, insta_username, insta_password)

    else:
        print(Fore.RED + "❌ Invalid choice. Please try again.")
    
    print(Fore.CYAN + "\n\n🌟 Thank you for using Instagram Tools! 🌟")
    print(Fore.YELLOW + "Created by: " + Fore.GREEN + "dzj3an (GitHub)")
    print(Fore.YELLOW + "If you found this tool useful, consider supporting the developer:")
    print(Fore.CYAN + "👉 Donate here: " + Fore.BLUE + "https://dzj3an.github.io/donate.html")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())