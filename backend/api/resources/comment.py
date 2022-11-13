from flask_restful import Resource, request
from marshmallow import ValidationError
from api.models.comment import CommentModel
from api.models.post import PostModel
from api.models.user import UserModel
from api.schemas.comment import CommentSchema

from flask_jwt_extended import jwt_required, get_jwt_identity

comment_schema = CommentSchema()
comment_list_schema = CommentSchema(many=True)


class CommentList(Resource):
    @classmethod
    def get(cls, post_id):
        """
        1. 게시물 id 를 URL 로부터 얻어옵니다.
        2. 게시물 id에 달려 있는 전체 댓글을 조회합니다.
        """
        # URL 로부터 게시물의 ID 를 얻어와 게시물을 특정하고,
        post = PostModel.find_by_id(post_id)
        # 해당 게시물에 달려 있는 모든 댓글들을 ID의 역순으로 정렬한 다음,
        ordered_comment_list = post.comment_set.order_by(
            CommentModel.id.desc()
        )
        # 그것을 직렬화하여 반환!
        return comment_list_schema.dump(ordered_comment_list)

    @classmethod
    @jwt_required()
    def post(cls, post_id):
        """
        1. 게시물 id 를 URL 로부터 얻어옵니다.
        2. 게시물 id를 외래키로 하여 새로운 댓글을 작성합니다.
        """
        comment_json = request.get_json()
        # jwt로부터 작성자의 정보를 얻어와 작성자 id 를 특정하고,
        username = get_jwt_identity()
        author_id = UserModel.find_by_username(username).id
        try:
            # 댓글 인스턴스를 생성하고,
            new_comment = comment_schema.load(comment_json)
            new_comment.author_id = author_id  # 작성자를 추가해 준다.
            new_comment.post_id = post_id  # 어떤 게시물에 달린 댓글인지를 추가해 준다.
        except ValidationError as err:
            return err.messages, 400
        try:
            # 새 댓글을 데이터베이스에 저장한다.
            new_comment.save_to_db()
        except:
            return {"Error": "저장에 실패하였습니다."}, 500
        return comment_schema.dump(new_comment), 201


class CommentDetail(Resource):
    @classmethod
    def put(cls, post_id, comment_id):
        pass

    @classmethod
    def delete(cls, post_id, comment_id):
        pass
