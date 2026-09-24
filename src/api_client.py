import requests


class CustomerAPI:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_customers(self):

        response = requests.get(
            self.base_url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()