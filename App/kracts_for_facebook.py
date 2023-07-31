#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import posts
import time

def print_facebook_logo():
    print("┬┌─┬─┐┌─┐┌─┐┌┬┐┌─┐   ┌─┐┌─┐┬─┐")
    print("├┴┐├┬┘├─┤│   │ └─┐   ├┤ │ │├┬┘")
    print("┴ ┴┴└─┴ ┴└─┘ ┴ └─┘   └  └─┘┴└─")
    print(" / _|                 | |                  | |   ")
    print("| |_  __ _   ___  ___ | |__    ___    ___  | | __")
    print("|  _|/ _` | / __|/ _ \| '_ \  / _ \  / _ \ | |/ /")
    print("| | | (_| || (__|  __/| |_) || (_) || (_) ||   < ")
    print("|_|  \__,_| \___|\___||_.__/  \___/  \___/ |_|\_|\n")

def print_help_menu():
    print("\nLIST OF FUNCTIONS:")
    print("type: 'post quotes' to post a number of different quotes between time intervals.")
    print("type: 'post image' to post an image with a random quote.")
    print("type: 'delete latest post' to delete the latest post.")
    print("type: 'delete n latest posts' to delete n number of latest posts.")
    print("type: 'clear posted quotes' to clear the list of posted quotes history")
    print("type: 'exit' to quit\n")

# Function to make number_of_posts posts in time_interval_inseconds time
# between posts.
def make_n_posts(access_token, number_of_posts=100, time_interval_inseconds=60, link=None):
    posts_made = 0
    while posts_made < number_of_posts:
        message_to_post = posts.get_quote()
        
        if message_to_post is None:
            print("[-] No more quotes to post")
            break
                
        latest_post_id = posts.post_message_with_link(access_token, caption=message_to_post, link=link)
               
        posts_made += 1
        if posts_made != number_of_posts:
            time.sleep(time_interval_inseconds) 

    print(f"[+] MADE TOTAL {posts_made} POST(S)!")
    return latest_post_id

def post_image(access_token, image_path, link=None):
    quote = posts.get_quote()

    if not quote:
        print("[-] No more quotes to post")
        return None
    
    post_id = posts.post_photo_with_link(access_token, image_path, caption=quote, link=link)
    return post_id

def main():

    print_facebook_logo()

    load_dotenv()
    user_access_token = os.environ.get("FACEBOOK_USER_ACCESS_TOKEN")
    
    link = "https://www.google.com/"
    image_path = "image.png"
    latest_post_id = None

    while True:
        user_input = input("\n(type 'help' for available functions)\nEnter a function: ")
        if (user_input == "exit"):
            break
        elif (user_input == "post quotes"):
            number_of_posts = input("Number of posts: ")
            time_between_posts = input("Time between posts (in seconds): ")
            include_link = input("Include link? (y/n): ")
            if include_link == 'y':
                latest_post_id = make_n_posts(user_access_token, int(number_of_posts), int(time_between_posts), link)
            elif include_link == 'n':
                latest_post_id = make_n_posts(user_access_token, int(number_of_posts), int(time_between_posts))
        elif (user_input == "post image"):
            include_link = input("Include link? (y/n): ")
            if include_link == 'y':
                latest_post_id = post_image(user_access_token, image_path, link)
            elif include_link == 'n':
                latest_post_id = post_image(user_access_token, image_path)
        elif (user_input == "help"):
            print_help_menu()
        elif (user_input == "delete latest post"):
            posts.delete_post(user_access_token, posts.get_latest_post_id_from_json())
        elif (user_input == "delete n latest posts"):
            number_of_posts_to_delete = input("Number of posts to delete: ")
            posts.delete_n_posts(user_access_token, number_of_posts=int(number_of_posts_to_delete))
        elif (user_input == "clear posted quotes"):
            posts.clear_file("posted_quotes.txt")
        else:
            print("[-] Unknown Command!")
    
if __name__ == "__main__":
    main()
