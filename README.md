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
- [Loading Test](#loading-test)
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

# when Read more is clicked first 100 words of the content are displayed(this can be customized)
![OnClickingReadMore](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/73e6dbd8-a815-4dc7-99ed-aafc2969a62b)

# When 'Read on Reddit' is clicked it is redirected to reddit.com where this post is available
![OnClickRedirectsToRedditWebsite](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/9a075fe7-b1c3-4caf-88cc-8637ded126dd)

## Features
Reddit WebPage Crawler allows users to effortlessly search for their desired subreddit and instantly access the top 10 hot threads within that subreddit. This feature enables users to explore trending discussions and valuable content from various communities.

# Comprehensive Thread Details
For each retrieved thread, the application provides a comprehensive set of details to enhance the user experience. These details include:

Thread Title: The title of the thread, grabbing user attention and summarizing the thread's content.
Author's Username: The username of the thread's author, facilitating identification of content creators.
Creation Timestamp: The date and time when the thread was created, offering insights into the thread's freshness.
Content Preview: A snippet of the thread's content, providing users with a concise preview of the thread's topic.
Read More Option: An interactive "Read More" link that expands the content preview for threads with longer content, allowing users to delve deeper into discussions.
Original Reddit Post Link: A direct link to the original Reddit post, enabling users to access the entire thread and its associated comments on Reddit's platform.
Image Display: Inclusion of images if available within the thread, offering a visual element to complement the textual content.
Intuitive Interaction
The application's user interface is designed with intuitiveness in mind. Users can effortlessly search for subreddits and retrieve thread information without the need for navigating Reddit's official site. The interactive "Read More" link provides seamless access to extended content, ensuring a smooth and user-friendly browsing experience.

# Visual Representation
Images associated with threads are visually displayed within the application's interface, enhancing the thread's visual appeal and enriching the browsing experience. This visual representation makes it easier for users to quickly grasp the essence of a thread's content.

# Seamless Integration with Reddit API
Reddit WebPage Crawler seamlessly integrates with the Reddit API through the praw library. This integration ensures accurate and up-to-date data retrieval, empowering users to stay informed about the latest and most popular discussions within their chosen subreddits.

# Cached Data for Swift Retrieval
To optimize user experience and expedite search results, Reddit WebPage Crawler employs a caching mechanism. Searched subreddit data is intelligently cached, allowing subsequent searches to retrieve information swiftly without redundant API calls. This caching strategy not only reduces load times but also conserves server resources, ensuring that users receive the latest threads promptly while benefiting from enhanced performance.

By intelligently storing and retrieving data from cache, the application minimizes latency and provides users with a seamless browsing experience. This feature enhances the overall efficiency of the application, making exploration of top threads from various subreddits both swift and effortless.

# Easy Installation and Configuration
The installation process for Reddit WebPage Crawler is straightforward. The provided instructions guide users through the process of setting up the project, installing dependencies, and configuring Reddit API credentials. This simplicity allows users to quickly set up the application and start exploring top threads.

# Error Handling and Responsiveness
The application is equipped with robust error handling mechanisms to gracefully manage unexpected scenarios that may arise during data retrieval or user interactions. Additionally, the interface is designed to be responsive, ensuring a consistent and engaging experience across different screen sizes and devices.

# Contact and Feedback
Reddit WebPage Crawler welcomes user engagement and feedback. The "Contact" section provides users with the means to reach out to the project maintainer, Vinesh Narayan Nadar, for questions, suggestions, or any assistance needed. This proactive approach encourages a sense of community and collaboration.

Feel free to explore the project's functionality and interface, and do not hesitate to reach out if you have any inquiries or suggestions for improvement. Your feedback is highly valued and contributes to the ongoing enhancement of the Reddit WebPage Crawler.



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

### Loading Test
<a id="loading-test"></a>
Successfully conducted a Loading Test for the designed API using Locust. Results are as follows for # peak concurrency 20 and Spawn Rate 5, RPS -> 10.1 : 
![LoadTestingLocust](https://github.com/progspac-vnn/RedditWrapperWebApp/assets/83080783/14201af6-ddee-4d93-996e-8b422d3a0e09)

## Dependencies
The project relies on the following external packages, which are listed in `requirements.txt`:
- asgiref==3.7.2
- certifi==2023.7.22
- charset-normalizer==3.2.0
- click==8.1.7
- colorama==0.4.6
- Django==3.2.20
- djangorestframework==3.14.0
- praw==7.7.1
- prawcore==2.3.0
- python-dotenv==0.21.1
- pytz==2023.3
- requests==2.31.0
- sqlparse==0.4.4
- typing_extensions==4.7.1
- tzdata==2023.3
- update-checker==0.18.0
- urllib3==2.0.4
- gunicorn==21.2.0(For Deployment)
- locust==2.16.1(For Load Testing)

Make sure you have these dependencies installed before running the application.

## Contact
For any questions, suggestions, or issues, please feel free to contact the project maintainer:
- Name: Vinesh Narayan Nadar
- Email: vineshnnadar@gmail.com
- GitHub: [My GitHub Profile](https://github.com/progspac-vnn)

