from flask import request, jsonify
from app.post.serializers import PostSchema
from app.post.models import Post
from app.post import bp
from app.helpers.extensions import db

post_schema = PostSchema()
post_schema = PostSchema(many=True)


@bp.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    if posts:
        results = post_schema.dumps(posts)
        return jsonify({
            'status': 'ok',
            'code': 200,
            'data': results
        }), 200
    else:
        return jsonify({
            'status': 'ok',
            'code': 200,
            'msg': 'No data found',
            'data': []
        }), 200


@bp.route('/api/posts', methods=['POST'])
def insert_post():
    content = request.get_json()
    try:
        post = Post(title=content['title'], body=content['body'], sub_body='test')
        data, errors = PostSchema().load(post.__dict__)
        if errors:
            return jsonify({
                'status': 'ko',
                'code': 422,
                'msg': errors
            }), 422
    except:
        return jsonify({
            'status': 'ko',
            'code': 415,
            'msg': 'Fail'
        }), 415
    try:
        db.session.add(post)
        db.session.commit()
        return jsonify({
            'status': 'ok',
            'code': 201,
            'msg': 'Create a new post successfully!'
        }), 201
    except:
        return jsonify({
            'status': 'ko',
            'code': 403,
            'msg': 'Fail'
        })
