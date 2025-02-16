from locust import HttpUser, task, between

class ChatbotUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def chat(self):
        self.client.get("/chat?message=Hello")

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py --host=http://127.0.0.1:8000")
