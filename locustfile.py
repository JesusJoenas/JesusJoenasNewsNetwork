from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home_page(self):
        self.client.get("/")

    @task
    def login_page(self):
        self.client.get("/login/")

    @task
    def search_technology(self):
        self.client.get("/search/?q=technology")
