# Reddit WebPage Crawler

Reddit WebPage Crawler is a web application that allows users to search for a subreddit and view the top 10 (Hot) threads within that subreddit. 
The application fetches data using the Reddit API and displays relevant information such as post titles, authors, content previews, and more.

## Table of Contents
- [Overview](#overview)
- [Working](#working)
- [Features](#features)
- [Search and Display](#search-and-display)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contact](#contact)

## Overview
This project is a Django web application that utilizes the Reddit API through the `praw` library to retrieve and display the top 10 threads from a specified subreddit. 
Users can search for a subreddit by entering its name and clicking the search button. The fetched data is presented in a user-friendly format, showing key details of each thread, including titles, authors, content previews, images, and links to the original Reddit posts.

## Working
# Home Page
![HomePage](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/b6a3606a-5288-47ba-9234-4ef206abc161)

# Entered Java as a SubReddit and displayed 10 threads
![JavaSubReddit](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/aa9ff795-33ac-4993-aa99-9fbc1fee39c8)

# when Read more is clicked first 100 words of the content is displayed(this can be customized)
![OnClickingReadMore](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/73e6dbd8-a815-4dc7-99ed-aafc2969a62b)

# When 'Read on Reddit' is clicked it is redirected to reddit.com where this post is available
![OnClickRedirectsToRedditWebsite](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/9a075fe7-b1c3-4caf-88cc-8637ded126dd)

## Features

### Search and Display
Users can enter the name of a subreddit in the search box and click the search button to retrieve the top 10 threads from that subreddit. 
The application then displays relevant information for each thread, including:
- Thread title
- Author's username
- Date and time of creation
- Content preview with a "Read More" option for longer content
- Link to the original Reddit post
- Display of images if available

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (recommended) and activate it.
4. Install the required dependencies by running: `pip install -r requirements.txt`
5. Set up your Django project (if not done already).
6. Replace the `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` placeholders in your Django project's settings with your Reddit API credentials.

## Usage
1. Start your Django development server.
2. Open your web browser and navigate to the provided local address (usually `http://127.0.0.1:8000`).
3. Enter the name of the subreddit you want to search for in the input field and click the "Search" button.
4. The top 10 threads from the specified subreddit will be displayed with their relevant information.

## Dependencies
The project relies on the following external packages, which are listed in `requirements.txt`:
- asgiref
- certifi
- charset-normalizer
- Django
- djangorestframework
- praw
- prawcore
- python-dotenv
- pytz
- requests
- soupsieve
- sqlparse
- typing_extensions
- tzdata
- update-checker
- urllib3

Make sure you have these dependencies installed before running the application.

## Contact
For any questions, suggestions, or issues, please feel free to contact the project maintainer:
- Name: Your Name
- Email: your.email@example.com
- GitHub: [YourGitHubUsername](https://github.com/YourGitHubUsername)

