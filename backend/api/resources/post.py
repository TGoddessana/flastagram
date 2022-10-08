from flask_restful import Resource, request
from api.models.post import PostModel, db
from api.schemas.post import PostSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required
from flask import abort

post_schema = PostSchema()
post_list_schema = PostSchema(many=True)


class Post(Resource):
    @classmethod
    def get(cls, id):
        post = PostModel.find_by_id(id)
        if post:
            return post_schema.dump(post), 200
        else:
            return {"Error": "게시물을 찾을 수 없습니다."}, 404

    @classmethod
    @jwt_required()
    def put(cls, id):
        post_json = request.get_json()
        post = PostModel.find_by_id(id)
        # 게시물이 존재한다면 수정한다.
        if post:
            post.title = post_json["title"]
            post.content = post_json["content"]
        # 게시물이 존재하지 않는다면 새 게시물을 생성한다.
        else:
            try:
                post = post_schema.load(post_json)
            except ValidationError as err:
                return err.messages, 400

        post.save_to_db()

        return post_schema.dump(post), 200

    @classmethod
    @jwt_required()
    def delete(cls, id):
        post = PostModel.find_by_id(id)
        if post:
            post.delete_from_db()
            return {"message": "게시물이 성공적으로 삭제되었습니다."}, 200
        return {"Error": "게시물을 찾을 수 없습니다."}, 404


class PostList(Resource):
    """
    게시물 목록에 관한 GET, POST 요청을 처리
    GET : 모든 게시물의 목록을 보여줌
    POST : 게시물을 하나 생성함
    """

    @classmethod
    def get(cls):
        page = request.args.get("page", type=int, default=1)
        ordered_posts = PostModel.query.order_by(PostModel.id.desc())
        pagination = ordered_posts.paginate(page, per_page=10, error_out=False)
        result = post_list_schema.dump(pagination.items)
        return result

    @classmethod
    @jwt_required()
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
