import json
import facebook_api as fb

# Function to post a message to facebook.
def post_message(access_token, message):
    post_id = fb.post_message_to_facebook(access_token, message)
    #post_meta = fb.get_post_metadata(access_token, post_id)
    if post_id:
        write_post_id_to_json(post_id)
        return post_id
    return None

# Function to post a message with link in facebook.
def post_message_with_link(access_token, caption, link=None, album=None):
    post_id = fb.post_message_with_link_to_facebook(access_token, caption, link, album)
    if post_id:
        write_post_id_to_json(post_id)
        return post_id
    return None

# This function posts a photo with caption to facebook. 
def post_photo(access_token, photo_path, caption=None, album=None):
    post_id = fb.post_photo_to_facebook(access_token, photo_path, caption, album)
    if post_id:
        write_post_id_to_json(post_id["post_id"])
        return post_id
    return None

# Function that posts a photo with a link in caption.
def post_photo_with_link(access_token, photo_path, caption=None, link=None):
    post_id = fb.post_photo_with_link_to_facebook(access_token, photo_path, caption, link)
    if post_id:
        write_post_id_to_json(post_id["post_id"]) 
        return post_id
    return None

# Function to delete the latest post from facebook.
def delete_post(access_token, post_id):
    fb.delete_post_from_facebook(access_token, post_id)
    delete_post_id_from_json(post_id)
    # print(f"[+] Post with post id: {id} deleted!")

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
            # print("[+] Post id has been written to the JSON file.")
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

# Function that determines if a line exists in a file.
# Returns True if exists, False otherwise.
def find_line_in_file(line, file_to_search):
    try:
        with open(file_to_search, "r") as search_file:
            for existing_line in search_file:
                if line == existing_line.strip():
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file_to_search}' not found.")
        return False
    except Exception as e:
        print("An error occurred:", e)
        return False

# This function reads from "quotes.txt" one line (quote), checks if the quote
# is already been posted (posted quotes are in the "posted_quotes.txt"). If it
# has been posted it reads the next one until it find one that was not posted yet.
# If no such quote found, it returns None, else it return the next quote to get posted.
def get_quote():
    try:
        with open("quotes.txt", "r") as read_file:
            read_file.seek(0)
            quote_to_post = read_file.readline().strip()
            while find_line_in_file(quote_to_post, "posted_quotes.txt"):
                quote_to_post = read_file.readline().strip()
        if quote_to_post:
            with open("posted_quotes.txt", "a") as write_file:
                write_file.write(quote_to_post + "\n")
            return quote_to_post
        return None
    except Exception as e:
        print("[-] An error occured:", e)

# Function that deletes the last line of file.
def delete_last_quote(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            file.writelines(lines[:-1])

        print("[+] Last quote has been deleted successfully.")
    except FileNotFoundError:
        print(f"[-] File '{filename}' not found.")
    except Exception as e:
        print("[-] An error occurred while deleting the last line:", e)

# Function that deletes all lines in a file.
def clear_file(filename):
    try:
        with open(filename, "w") as file:
            file.write("")

        print(f"[+] All lines have been deleted from '{filename}'. The file is now empty.")
    except Exception as e:
        print("[-] An error occurred while deleting all lines:", e)