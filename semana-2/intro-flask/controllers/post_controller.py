from models.post import Post, db


class PostController:

    @staticmethod
    def get_all_post():
        try:
            posts = Post.query.all()
            return [post.to_dict() for post in posts], None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def create_post(data):
        try:
            new_post = Post(
                title=data.get('title'),
                content=data.get('content'),
                user_id=data.get('user_id')
            )

            db.session.add(new_post)
            db.session.commit()

            return new_post.to_dict(), None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_post_by_id(post_id):
        try:
            post = Post.query.get(post_id)
            print(post.author.name)
            return post.to_dict(), None
        except Exception as e:
            return None, str(e)
