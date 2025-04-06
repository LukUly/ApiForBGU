from json_placeholder.json_placeholder_api import JsonPlaceholderApi

def test_post_ids_are_unique():
    posts = JsonPlaceholderApi.get_posts()
    post_ids = [post.id for post in posts]
    assert len(post_ids) == len(set(post_ids)), "Найдены дубликаты ID постов"

