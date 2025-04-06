from typing import List

from base_api.api_client import *
from json_placeholder.Models.post import Post
from json_placeholder.endpoints import GET_POSTS_ENDPOINT


class JsonPlaceholderApi:
    @staticmethod
    def get_posts():
        response = ApiClient.get(GET_POSTS_ENDPOINT)
        json_content = response.json()
        posts = [Post.parse_obj(post_data) for post_data in json_content]
        print(f"Всего постов: {len(posts)}")
        return posts
