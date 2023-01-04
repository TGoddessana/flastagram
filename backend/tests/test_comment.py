from . import *


class CommentListTestaCase(CommonTestCaseSettings):
    """
    /posts 에 대한 GET, POST 요청을 테스트한다.
    """

    def test_get_comment_list(self):
        """
        댓글이 5개가 달려 있는 게시물이 있다면,
        해당 게시물에 접속했을 때에 댓글의 수는 5개여야 한다.
        """

    def test_post_comment_list(self):
        """
        1. 댓글이 0개인 게시물에 적절한 POST /posts/1/comments/ 요청을 보내면,
           해당 게시물에 접속했을 때에 댓글의 수는 1개여야 한다.

        2. 댓글 생성 요청을 보낼 때, request header 에 JWT가 첨부되지 않았다면
           해당 댓글에 대한 요청은 실패하고, 상태 코드는 401 이어야 한다.
        """
        pass
