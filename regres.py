from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "https://marketplace.digital.gov.bc.ca/"

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.status_code)
        

    @task
    def create_user(self):
        self.client.post("/api/users", data='''
        {"name": "morpheus", "job":"leader"}''')