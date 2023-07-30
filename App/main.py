from dotenv import load_dotenv
import os
import posts
import time


def make_n_posts(access_token, time_interval_inseconds):
    number_of_posts = 5
    posts_made = 0
    
    while posts_made < number_of_posts:
        message_to_post = posts.get_quote()
        
        if not message_to_post:
            print("[-] No more quotes to post")
            break
        
        latest_post_id = posts.post_message(access_token, message_to_post)
        posts_made = posts_made + 1
        time.sleep(time_interval_inseconds)
    
    print(f"[+] MADE TOTAL {number_of_posts} POSTS!")


def main():

    load_dotenv()
    user_access_token = os.environ.get("FACEBOOK_USER_ACCESS_TOKEN")
    
    #link = "https://www.google.com/"
    make_n_posts(user_access_token, 3)


    #posts.delete_n_posts(user_access_token, 5)

if __name__ == "__main__":
    main()
