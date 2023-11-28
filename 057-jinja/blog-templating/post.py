import requests
from pprint import pprint
N_P0INT_API = "https://api.npoint.io/c790b4d5cab58020d391"


class Post:
    def __init__(self):
        response = requests.get(url=N_P0INT_API)
        self.data = response.json()

    def display(self):
        """Display data content"""
        pprint(self.data)

    def get_all(self):
        """Return all posts"""
        return self.data

    def get_by_id(self, post_id):
        """Return only one post by ID
        post_id : the ID of the post tou fetch
        """
        for post in self.data:
            if int(post_id) == post['id']:
                return post
