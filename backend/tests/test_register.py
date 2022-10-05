from . import *


class UserRegisterTestCase(CommonTestCaseSettings):
    """
    유저 회원가입에 대한 테스트
    CommonTestCaseSettings 의 setup() 에 의해서,
    테스트 데이터베이스에 있는 유저는 한 명 존재합니다.
    UserModel(username="test_user",
              password="12345",
              email="test@example.com").save_to_db()
    """

    def test_required_validation(self):
        """
        클라이언트에서 보낸 데이터 중, 누락된 것이 있다면,
        400 bad request 상태 코드를 응답해야 한다.
        """
        response = self.client.post("http://127.0.0.1:5000/register/").get_json()
        print(response)

    def test_not_null_validation(self):
        """
        클라이언트에서 보낸 데이터 중, null 값이 들어온다면,
        400 bad request 상태 코드를 응답해야 한다.
        """
        pass

    def test_password_confirm_field_validation(self):
        """
        클라이언트에서 보낸 데이터 중, passowrd 와 password_confirm 필드의 값이 다르다면,
        400 bad request 상태 코드를 응답해야 한다.
        """
        pass

    def test_unique_username_validation(self):
        """
        회원가입을 진행할 때에 이미 존재하는 유저의 이름으로 회원가입을 시도한다면,
        400 bad request 상태 코드를 응답해야 한다.
        """
        pass

    def test_unique_username_validation(self):
        """
        회원가입을 진행할 때에 이미 존재하는 이메일로 회원가입을 시도한다면,
        400 bad request 상태 코드를 응답해야 한다.
        """
        pass
