from flask import request
from app.post.serializers import PostSchema
from app.post.models import Post
from app.post import bp

post_schema = PostSchema()


@bp.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.get(1)
    print(posts)
    if posts:
        return post_schema.dumps(posts)
    else:
        return 'test'


@bp.route('/api/posts', methods=['POST'])
def insert_post():
    content = request.json()
    print(content)

