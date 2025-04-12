from github import Github
import os
from dotenv import load_dotenv

def connect_to_github():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get GitHub token from environment variable
    token = os.getenv('GITHUB_TOKEN')
    
    if not token:
        print("Error: GITHUB_TOKEN not found in environment variables")
        print("Please create a .env file with your GitHub token:")
        print("GITHUB_TOKEN=your_github_token_here")
        return None
    
    try:
        # Create GitHub instance
        g = Github(token)
        
        # Test connection by getting the authenticated user
        user = g.get_user()
        print(f"Successfully connected to GitHub as {user.login}")
        return g
    except Exception as e:
        print(f"Error connecting to GitHub: {str(e)}")
        return None

if __name__ == "__main__":
    connect_to_github()
