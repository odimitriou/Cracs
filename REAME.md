# Facebook Auto-Poster



## Description

Facebook Auto-Poster is a simple Python application designed to run on a Raspberry Pi. It automates posting on Facebook using the Facebook Graph API. This application allows you to schedule and make posts on your Facebook account without manual intervention.

## Features

- Automated posting on Facebook using the Graph API.
- Easy-to-use and lightweight Python script.
- Securely handles sensitive data, such as Facebook user access tokens.
- Flexible scheduling options for automated posts.

## Getting Started

### Prerequisites

1. Raspberry Pi with a Linux-based operating system installed.
2. Python 3 installed on the Raspberry Pi.
3. Facebook user access token with appropriate permissions to post on the user's behalf.

### Installation

1. Clone or download this repository to your Raspberry Pi.

`git clone https://github.com/odimitriou/GraphAPI-test-app.git`


2. Install the required Python dependencies.

`cd GraphAPI-test-app
pip install -r requirements.txt`


### Configuration

1. Obtain a Facebook user access token from the Facebook for Developers website. Ensure the token has the necessary permissions to make posts on the user's feed.

2. Create a `.env` file in the project directory and add the following content:

`FACEBOOK_USER_ACCESS_TOKEN=your_facebook_access_token_here`

Replace `your_facebook_access_token_here` with the actual Facebook user access token you obtained.

### Usage

Run the Python script to make an automated post on your Facebook account:

`python facebook_auto_poster.py`

The script will automatically use the user access token from the `.env` file to authenticate with the Facebook Graph API and make the post.

### Scheduling (comming soon)

You can schedule the script to run at specific intervals using the built-in scheduling tools on your Raspberry Pi, such as `cron`.

1. Open the crontab configuration:

`crontab -e`

2. Add the following line to the crontab file to run the script every day at 8:00 AM:

`0 8 * * * /usr/bin/python /path/to/your/facebook_auto_poster.py`

Replace `/path/to/your/facebook_auto_poster.py` with the actual path to your Python script.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).






