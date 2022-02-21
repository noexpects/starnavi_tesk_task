from rest_framework import status
from rest_framework.exceptions import APIException


class AlreadyUpvoted(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'detail': 'You have already upvoted this post'}
    default_code = 'alredy_upvoted'


class DidNotUpvoted(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'detail': 'You have not upvoted this post yet'}
    default_code = 'did_not_upvoted'


class NeedLogin(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'detail': "You have to be logged in to perform post's upvote operation"}
    default_code = 'need_login'