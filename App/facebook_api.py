import facebook

def post_message_to_facebook(access_token, message):
    '''
    This function makes a facebook post with the message
    specified as argument.
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        post_response = graph.put_object("me", "feed", message=message)
        post_id = post_response["id"]
        print(f"[+] Successfully created a post! Post ID: {post_id}")
        return post_id
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
        return None

def post_message_with_link_to_facebook(access_token, caption, link=None, album=None):
    '''
    Function that make a post to facebook including a link in the caption.
    '''
    try:
        message = caption + "\n\n" + link if link else caption
        graph = facebook.GraphAPI(access_token)
        post_response = graph.put_object("me", "feed", message=message, album=album)
        post_id = post_response["id"]
        print(f"[+] Successfully created post with link! Post ID: {post_id}")
        return post_id
    except facebook.GraphAPIError as e:
        print("[-] An error occurred:", e)
        return None

def post_photo_to_facebook(access_token, photo_path, caption=None, album=None):
    '''
    This function makes a facebook post with a photo and caption (optional)
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        with open(photo_path, "rb") as photo_file:
            post_id = graph.put_photo(image=photo_file, message=caption, album_path=album)
        print("[+] Successfully posted the photo on Facebook!")
        return post_id
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
        return None

def post_photo_with_link_to_facebook(access_token, photo_path, caption=None, link=None):
    '''
    This function makes a facebook post with a photo with an optional caption.
    A link can also be added to the caption (also optional).
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        message = caption + "\n\n" + link if link else caption
        with open(photo_path, "rb") as photo_file:
            post_id = graph.put_photo(image=photo_file, message=message)
        print("[+] Successfully posted the photo with link on Facebook!")
        return post_id
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
        return None


def delete_post_from_facebook(access_token, post_id):
    '''
    This function deletes a post made to facebook
    using the corresponding facebook id of that post.
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        graph.delete_object(post_id)
        print("[+] Successfully deleted the post from Facebook!")
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)

def get_post_id(access_token, post_url):
    '''
    This function takes as arguments a post URL
    and returns the post id of that post.
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        post_data = graph.get_object(post_url, fields="id")
        post_id = post_data["id"]
        return post_id
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
        return None
    

def get_post_metadata(access_token, post_id):
    '''
    This function returns the post metadata
    using the post id.
    '''
    try:
        graph = facebook.GraphAPI(access_token)
        post_data = graph.get_object(post_id)
        return post_data
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
        return None

