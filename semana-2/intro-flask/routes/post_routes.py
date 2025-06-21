from flask import Blueprint, jsonify, request
from controllers.post_controller import PostController

post_blueprint = Blueprint('posts', __name__)

@post_blueprint.route('/posts')
def get_posts():
    posts, error = PostController.get_all_post()

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "List de posts",
        "posts": posts
    })

@post_blueprint.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    post, error = PostController.create_post(data)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Post creado correctamente",
        "post": post
    })
