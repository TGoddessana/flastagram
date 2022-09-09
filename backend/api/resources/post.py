from flask_restful import Resource, request
from api.models.post import PostModel, db
from api.schemas.post import PostSchema
from marshmallow import ValidationError


post_schema = PostSchema()
post_list_schema = PostSchema(many=True)


class Post(Resource):
    @classmethod
    def get(cls, id):
        post = PostModel.find_by_id(id)
        if post:
            return post_schema.dump(post), 200
        return {"Error": "게시물을 찾을 수 없습니다."}, 404

    @classmethod
    def put(cls, id):
        pass

    @classmethod
    def delete(cls, id):
        pass


class PostList(Resource):
    """
    게시물 목록에 관한 GET, POST 요청을 처리
    GET : 모든 게시물의 목록을 보여줌
    POST : 게시물을 하나 생성함
    """

    @classmethod
    def get(cls):
        return {"posts": post_list_schema.dump(PostModel.find_all())}, 200

    @classmethod
    def post(cls):
        post_json = request.get_json()
        try:
            new_post = post_schema.load(post_json)
        except ValidationError as err:
            return err.messages, 400
        try:
            new_post.save_to_db()
        except:
            return {"Error": "저장에 실패하였습니다."}, 500
        return post_schema.dump(new_post), 201
