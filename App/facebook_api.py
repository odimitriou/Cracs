import facebook

def post_message_to_facebook(access_token, message):
    try:
        graph = facebook.GraphAPI(access_token)
        post_response = graph.put_object("me", "feed", message=message)
        post_id = post_response["id"]
        print(f"Successfully created a post! Post ID: {post_id}")
    except facebook.GraphAPIError as e:
        print("An error occurred:", e)
