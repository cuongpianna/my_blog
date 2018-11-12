from flask import request, jsonify
from app.post.serializers import PostSchema, CategorySchema
from app.post.models import Post, Category
from app.post import bp
from app.helpers.extensions import db

# post_schema = PostSchema()
# post_schema = PostSchema(many=True)


@bp.route('/api/categories', methods=['GET'])
def get_categories():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Category.to_collection_dict(Category.query, page, per_page)
    if not data:
        return jsonify({
            'status': 'ok', 'code': 200, 'msg': 'No data found'
        })
    return jsonify(data), 200

@bp.route('/api/category', methods=['POST'])
def insert_category():
    content = request.get_json()
    try:
        print('ok')
        cate = Category(name=content['name'])
        data, errors = CategorySchema().load(cate.to_json())
        print(errors)
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
        db.session.add(cate)
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

@bp.route('/api/category/<id>', methods=['GET'])
def get_category(id):
    return

@bp.route('/api/category/<id>', methods=['PUT'])
def update_category(id):
    return

@bp.route('/api/category/<id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({
            'status': 'ok',
            'code': 200,
            'msg': 'No data found'
        })
    db.session.delete(category)
    db.session.commit()
    return jsonify({
            'status': 'ok',
            'code': 200,
            'msg': 'Delete successfully'
        })


@bp.route('/api/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Post.to_collection_dict(Post.query, page, per_page)
    if data:
        return jsonify([
            data
        ]), 200
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
        post = Post(title=content['title'], body=content['body'],
                    sub_body='test', category_id=content['category_id'])
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
