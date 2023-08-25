from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_reddit_posts(self):
        subreddit = "java"  
        self.client.get(f"api/reddit/view/{subreddit}")