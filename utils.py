from typing import Union


def get_user_id_by_cookie(request, users: list) -> Union[int, None]:
    login_key = request.cookies.get('login_key', None)
    user_id = request.cookies.get('user_id', None)

    if login_key and user_id:
        for user in users:
            if users.index(user) == int(user_id) and user['key'] == login_key:
                return int(user_id)

    return None

