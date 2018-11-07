from flask import request, jsonify
from app.post.serializers import PostSchema, CategorySchema
from app.post.models import Post, Category
from app.post import bp
from app.helpers.extensions import db

post_schema = PostSchema()
post_schema = PostSchema(many=True)
category_schema = CategorySchema()
category_schema = CategorySchema(many=True)


@bp.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    if posts:
        results = post_schema.dump(posts)
        return jsonify({
            'status': 'ok',
            'code': 200,
            'data': results.data
        }), 200
    else:
        return jsonify({
            'status': 'ok',
            'code': 200,
            'msg': 'No data found',
            'data': []
        }), 200


@bp.route('/api/posts/<slug>', methods=['GET'])
def get_post_by_slug(slug):
    post = Post.query.filter_by(slug_title=slug)
    if post:
        result = post_schema.dump(post)
        return jsonify({
            'status': 'ok',
            'code': 200,
            'data': result.data
        }), 200
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
        post = Post(title=content['title'], body=content['body'])
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


@bp.route('/api/categories', methods=['GET'])
def get_category():
    categories = Category.query.all()
    if categories:
        results = category_schema.dump(categories)
        return jsonify({
            'status': 'ok',
            'code': 200,
            'data': results.data
        }), 200
    return jsonify({
        'status': 'ok',
        'code': 200,
        'msg': 'No data found',
        'data': []
    }), 200


@bp.route('/api/categories', methods=['POST'])
def insert_categories():
    content = request.get_json()
    try:
        category = Category(name=content['name'])
        data, errors = PostSchema().load(category.__dict__)
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
        db.session.add(category)
        db.session.commit()
        return jsonify({
            'status': 'ok',
            'code': 201,
            'msg': 'Create new category successfully!'
        }), 201
    except:
        return jsonify({
            'status': 'ko',
            'code': 403,
            'msg': 'Fail'
        })
