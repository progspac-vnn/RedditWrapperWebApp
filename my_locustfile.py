from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds between tasks
    
    @task
    def get_reddit_posts(self):
        subreddit = "your-subreddit-name"  # Replace with the subreddit you want to load test
        self.client.get(f"/reddit/view/{subreddit}/")