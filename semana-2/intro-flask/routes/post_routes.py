from flask import Blueprint, jsonify, request
from controllers.post_controller import PostController
from flask_jwt_extended import jwt_required
from utils.token_manager import TokenManager

post_blueprint = Blueprint('posts', __name__)

@post_blueprint.route('/posts')
@jwt_required()
def get_posts():
    current_user_id = TokenManager.get_current_user_id()
    posts, error = PostController.get_all_post(int(current_user_id))

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "List de posts",
        "posts": posts
    })

@post_blueprint.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()

    post, error = PostController.create_post(data)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Post creado correctamente",
        "post": post
    })

@post_blueprint.route('/posts/<int:post_id>')
@jwt_required()
def get_post(post_id):
    post, error = PostController.get_post_by_id(post_id)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "message": "Post",
        "post": post
    })
