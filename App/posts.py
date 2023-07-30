import json
import facebook_api as fb


def post_message(access_token, message):
    post_id = fb.post_message_to_facebook(access_token=access_token, message=message)
    post_meta = fb.get_post_metadata(access_token=access_token, post_id=post_id)
    print(post_meta)

# Function to save post data to the JSON file
def save_post_to_json(post_data, filename):
    with open(filename, "a") as file:
        json.dump(post_data, file, indent=2)
        file.write("\n")

# Function to get the most recent posts from the JSON file into memory
def get_recent_posts_from_json(filename, num_posts=10):
    recent_posts = []
    with open(filename, "r") as file:
        for line in file:
            post_data = json.loads(line)
            recent_posts.append(post_data)
            if len(recent_posts) >= num_posts:
                break
    return recent_posts

