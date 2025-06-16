# Instagram Comment Bot

[![Python](https://img.shields.io/badge/Python-3.11.9-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-3119/)  
[![Instagram](https://img.shields.io/badge/Instagram-sterile.py-purple?style=flat-square&logo=instagram)](https://instagram.com/sterile.py/)  
[![dotenv](https://img.shields.io/badge/python--dotenv-v1.0.1-lightgreen.svg)](https://pypi.org/project/python-dotenv/)  
[![Pillow](https://img.shields.io/badge/Pillow-v10.3.0-yellow.svg)](https://pypi.org/project/pillow/)

> ⚠️ **Important Note**: This bot currently uses `instagrapi`, which relies on Instagram's private API. Recent changes by Instagram (e.g., query hash updates) have broken some functionalities, and the library is not actively maintained to address them. As a result, the bot may not function reliably until a fix or an alternative library is implemented.

---

Automate engagement on Instagram by monitoring and responding to comments using Python.

## Features

- 🔍 **Keyword Monitoring** – Detects and responds to comments containing specific keywords.
- 💬 **Comment Replies** – Sends customized replies on Instagram posts.
- 📩 **Direct Messaging** – Engages users further via DMs.
- 🔁 **Continuous Monitoring** – Periodically checks for new comments.

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sterile-Gaming/instabot.git
   cd instabot
   ```
2. **Run the Setup Script:**
   - On Unix-based systems:
     ```bash
     ./setup.sh
     ```
   - On Windows systems:
     ```bash
     setup.bat
     ```
3. **Configure Environment Variables:**

   - Create a .env file in the project root directory and add your Instagram credentials and other configuration settings:

     ```bash
     # Instagram username and password
     INSTA_USERNAME=your_username
     INSTA_PASSWORD=your_password

     # Instagram post URL (e.g., https://www.instagram.com/p/C8pT8GRSV-q/)
     INSTA_POST_URL=https://www.instagram.com/p/C8pT8GRSV-q/

     # Toggle to send DM based on whether the keyword is found in the comment
     # true - send DM only if the keyword is found
     # false - send DM regardless of the keyword
     SEND_DM_IF_KEYWORD=true

     # Keyword to look for in comments
     INSTA_KEYWORD=pack

     # Toggle to send DM based on whether the commenter is following the user
     # true - send DM only if the commenter is following
     # false - send DM only if the commenter is not following
     SEND_DM_IF_FOLLOWING=true

     # Reply text for comments containing the keyword
     # {keyword} - the keyword found in the comment
     # {username} - the username of the commenter
     REPLY_COMMENT_TEXT=Thank you for commenting '{keyword}', @{username}!

     # Direct message text to send to users who comment the keyword
     # {keyword} - the keyword found in the comment
     # {display_name} - the display name of the commenter
     REPLY_DM_TEXT=Hi {display_name}! Thank you for your comment '{keyword}'. How can I assist you?
     ```

4. **Run the Bot:**
   - On Unix-based systems:
     ```bash
     python3 bot.py
     ```
   - On Windows systems:
     ```bash
     python bot.py
     ```

## Requirements:

- **Python 3.11.9**
- **instagrapi**
- **python-dotenv**
- **Pillow**

## Contributing

- Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

- This project is licensed under the MIT License - see the LICENSE file for details.
