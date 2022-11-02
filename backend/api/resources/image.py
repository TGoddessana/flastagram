from flask_restful import Resource
from flask_uploads import UploadNotAllowed
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity


from api.utils import image_upload
from api.schemas.image import ImageSchema

image_schema = ImageSchema()


class ImageUpload(Resource):
    @jwt_required()
    def post(self):
        """이미지를 업로드합니다."""
        data = image_schema.load(request.files)
        print(data)
        user_id = get_jwt_identity()
        folder = f"user_{user_id}"
        try:
            image_path = image_upload.save_image(data["image"], folder=folder)
            basename = image_upload.get_basename(image_path)
            return {"message": f"{basename}이미지가 성공적으로 업로드되었습니다."}, 201
        except UploadNotAllowed:
            extension = image_upload.get_extension(data["image"])
            return {"message": f"{extension} 는 적절하지 않은 확장자 이름입니다."}, 400
