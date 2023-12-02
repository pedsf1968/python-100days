from os import environ
import requests

NPOINT_FAKE_BLOG = environ.get("NPOINT_FAKE_BLOG")
NPOINT_DEFAULT_BLOG_IMAGE = ""


class Post:
    def __init__(self, post_id=0, title="", subtitle="", body="", author="", date="", image_url=NPOINT_DEFAULT_BLOG_IMAGE):
        self.post_id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.author = author
        self.date = date
        self.image_url = image_url

    def get_json(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "subtitle": self.subtitle,
            "body": self.body,
            "author": self.author,
            "date": self.date,
            "image_url": self.image_url
        }


class Posts:
    def __init__(self):
        self.posts = {}
        self.upload_data()

    def upload_data(self):
        all_posts = requests.get(NPOINT_FAKE_BLOG).json()
        for post in all_posts:
            post_id = int(post['id'])
            new_post = Post(
                post_id=post_id,
                title=post['title'],
                subtitle=post['subtitle'],
                body=post['body'],
                author=post['author'],
                date=post['date'],
                image_url=post['image_url']
            )
            self.posts[post_id] = new_post

    def get_all(self):
        return (self.posts[key].get_json() for key in self.posts)

    def get_by_id(self, post_id):
        post = self.posts[int(post_id)]
        return post.get_json()
