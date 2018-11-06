from flask import request
from app.post.serializers import PostSchema
from app.post.models import Post
from app.post import bp
from app.helpers.extensions import db

post_schema = PostSchema()
post_schema = PostSchema(many=True)


@bp.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    print(posts)
    if posts:
        return post_schema.dumps(posts)
    else:
        return 'test'


@bp.route('/api/posts', methods=['POST'])
def insert_post():
    content = request.get_json()
    post = Post(title=content['title'], body=content['body'], sub_body='test')
    db.session.add(post)
    db.session.commit()
    return 'ok'

