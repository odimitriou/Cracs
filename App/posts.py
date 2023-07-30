import json
import facebook_api as fb


def post_message(access_token, message):
    '''
    This function posts a message on facebook and saves
    the post id into the posts.json file.
    '''
    post_id = fb.post_message_to_facebook(access_token, message)
    #post_meta = fb.get_post_metadata(access_token, post_id)
    write_post_id_to_json(post_id)
    return post_id

# Function to delete the latest post from facebook.
def delete_post(access_token, post_id):
    '''
    This function deletes a post made to facebook
    using the corresponding facebook id of that post.
    '''
    fb.delete_post_from_facebook(access_token, post_id)
    delete_post_id_from_json(post_id)

# Function to delete n number of the latests posts from facebook.
def delete_n_posts(access_token, number_of_posts=1):
    latest_posts = get_recent_posts_from_json(number_of_posts)
    posts_deleted = 0
    if len(latest_posts) != 0:
        for id in latest_posts:
            delete_post(access_token, id)
            print(f"[+] Post with post id: {id} deleted!")
            posts_deleted = posts_deleted + 1
    print(f"[+] DELETED {posts_deleted} total posts!")

# Function to delete a post id from json
def delete_post_id_from_json(post_id):
    if post_id is not None:
        try:
            ids = dict()
            with open("posts.json") as file:
                ids = json.load(file)
                ids["post_ids"].remove(post_id)
            with open("posts.json", "w") as file:
                json.dump(ids, file, indent=4)
            #print("[+] Post id has been removed from the JSON file.")
        except Exception as e:
            print("[-] An error occurred:", e)

# Function to get the lastest post id
def get_latest_post_id_from_json():
    try:
        ids = dict()
        with open("posts.json") as file:
            ids = json.load(file)
        latest_id = ids["post_ids"][-1]
        if latest_id is not None:
            return latest_id
    except Exception as e:
        print("[-] An error occurred:", e)
    return None

# Function to save post id to the JSON file
def write_post_id_to_json(post_id):
    if post_id is not None:
        try:
            ids = dict()
            with open("posts.json") as file:
                ids = json.load(file)
                ids["post_ids"].append(post_id)
            with open("posts.json", "w") as file:
                json.dump(ids, file, indent=4)
            print("[+] Post id has been written to the JSON file.")
        except Exception as e:
            print("[-] An error occurred:", e)

# Function to get the most recent posts from the JSON file into list
def get_recent_posts_from_json(num_posts=10):
    try:
        ids = dict()
        recent_ids = []
        with open("posts.json") as file:
            ids = json.load(file)
            recent_ids = ids["post_ids"]
            if len(recent_ids) > num_posts:
                return recent_ids[:num_posts]
            else:
                return recent_ids
    except Exception as e:
        print("[-] An error occured:", e)

