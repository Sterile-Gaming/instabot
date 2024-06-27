import subprocess
import sys
import time
import os
import re

# Install required modules if not already installed
def install_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Ensure required modules are installed
try:
    import instagrapi
    from dotenv import load_dotenv
    from PIL import Image
except ImportError:
    install_module("instagrapi")
    install_module("python-dotenv")
    install_module("pillow")
    import instagrapi
    from dotenv import load_dotenv


import instagrapi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
username = os.getenv("INSTA_USERNAME").lower()
password = os.getenv("INSTA_PASSWORD")
post_url = os.getenv("INSTA_POST_URL")
keyword = os.getenv("INSTA_KEYWORD", "pack").lower()  # Default to "pack" if not set
reply_comment_text = os.getenv("REPLY_COMMENT_TEXT", "Thank you for commenting '{{keyword.upper()}}', @{{username}}!")
reply_dm_text = os.getenv("REPLY_DM_TEXT", "Hi {{display_name}}! Thank you for your comment '{{keyword.upper()}}'. How can I assist you?")



# Extract shortcode from the post URL using regex
shortcode_match = re.search(r'(?:/p/|/reel/|/tv/)([^/?]+)', post_url)
if not shortcode_match:
    raise ValueError("Invalid Instagram post URL format")
post_shortcode = shortcode_match.group(1)

# Initialize Instagram client
from instagrapi import Client
cl = Client()

# Attempt to login
try:
    cl.login(username=username, password=password)
    print(f"Logged in successfully as {username}")
except Exception as e:
    print(f"Failed to log in: {e}")
    exit()

processed_comments = set()
start_time = time.time()

def respond_to_comments():
    try:
        # Get the media ID from the shortcode
        post_id = cl.media_pk_from_url(f"https://www.instagram.com/p/{post_shortcode}/")
        # Fetch comments on the post
        comments = cl.media_comments(post_id)
        for comment in comments:
            # Check if the comment is new and contains the keyword
            if comment.pk not in processed_comments and comment.created_at_utc.timestamp() > start_time:
                if keyword in comment.text.lower():
                    processed_comments.add(comment.pk)
                    username_to_reply = comment.user.username if comment.user.username else "user"
                    reply_text = reply_comment_text.format(keyword=keyword.upper(), username=username_to_reply)
                    # Reply to the comment
                    cl.media_comment(post_id, reply_text, replied_to_comment_id=comment.pk)
                    # Like the comment
                    cl.comment_like(comment.pk)
                    # Fetch user information
                    commenter_info = cl.user_info(comment.user.pk)
                    commenter_display_name = commenter_info.full_name if commenter_info.full_name else "User"
                    # Send a direct message
                    dm_text = reply_dm_text.format(keyword=keyword.upper(), display_name=commenter_display_name)
                    cl.direct_send(dm_text, [comment.user.pk])
                    print(f"Replied and sent message to @{commenter_info.username} for comment '{keyword.upper()}'.")
    except Exception as e:
        print(f"Error while responding to comments: {e}")

try:
    while True:
        respond_to_comments()
        time.sleep(60)
except KeyboardInterrupt:
    print("Script interrupted and stopped by user.")
except Exception as e:
    print(f"Unexpected error: {e}")
