from api.ma import ma, Method, String
from api.models.post import PostModel
from api.models.user import UserModel
from api.schemas.user import AuthorSchema
from marshmallow import fields


class PostSchema(ma.SQLAlchemyAutoSchema):
    """
    게시물 모델에 관한 직렬화 규칙을 정의합니다.
    """

    image = fields.String(required=True)
    created_at = fields.DateTime(format="%Y-%m-%d,%H:%M:%S")
    updated_at = fields.DateTime(format="%Y-%m-%d,%H:%M:%S")
    author = fields.Nested(AuthorSchema)
    liker_count = Method("get_liker_count")
    is_like = Method("get_is_like")

    def get_liker_count(self, obj):
        return obj.get_liker_count()

    def get_is_like(self, obj):
        return obj.is_like(self.context["user"])

    class Meta:
        model = PostModel
        exclude = ("author_id",)
        load_instance = True
        include_fk = True
        ordered = True
