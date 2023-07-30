import os
import posts
import facebook_api as fb
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the Facebook user access token from the environment
    user_access_token = os.environ.get("FACEBOOK_USER_ACCESS_TOKEN")

    # Your message to be posted on Facebook
    message_to_post = "Hello, this is an automated post using Facebook Graph API!"

    # Call the function to post on Facebook
    post_id = posts.post_message(user_access_token, message_to_post)

if __name__ == "__main__":
    main()
