import os
import posts
import facebook_api as fb
from dotenv import load_dotenv

def main():

    load_dotenv()
    user_access_token = os.environ.get("FACEBOOK_USER_ACCESS_TOKEN")
    
    link = "https://www.google.com/"
    message_to_post = "Hello, this is an automated post using Facebook Graph API!!"

    # latest_post_id = posts.post_message(user_access_token, message_to_post)

    # recent_posts = posts.get_recent_posts_from_json(2)
    # print(recent_posts)

    posts.delete_post(user_access_token, posts.get_latest_post_id_from_json)
    posts.delete_n_posts(user_access_token, number_of_posts=10)

    
if __name__ == "__main__":
    main()
